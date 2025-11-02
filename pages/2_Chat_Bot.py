import streamlit as st
import requests

# ----------------------------- #
# 🌱 CONFIGURATION
# ----------------------------- #
st.set_page_config(page_title="Dr.Grow Chat", layout="centered")
st.title("🪴 Dr.Grow AI Chatbot")

# Load Hugging Face API token securely from Streamlit secrets
# (Set this in Streamlit Cloud → Settings → Secrets)
try:
    HF_API_TOKEN = st.secrets["HF_TOKEN"]
except Exception:
    st.error("❌ Missing Hugging Face API token. Please set 'HF_TOKEN' in Streamlit secrets.")
    st.stop()

HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# ----------------------------- #
# 🧠 MODEL SELECTION
# ----------------------------- #
selectoption = st.selectbox(
    "Select a model",
    ("🦙 LLaMA (Mistral-7B)", "🤖 Phi-2"),
)

if selectoption == "🦙 LLaMA (Mistral-7B)":
    MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
else:
    MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/phi-2"

# ----------------------------- #
# 💬 INITIALIZE CHAT HISTORY
# ----------------------------- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# ----------------------------- #
# 🗣️ USER INPUT
# ----------------------------- #
user_input = st.chat_input("Ask me about plants, gardening, or care tips...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation context
    context = "\n".join([f"User: {u}\nBot: {b}" for u, b in st.session_state.chat_history])
    full_prompt = f"{context}\nUser: {user_input}\nBot:"

    # ----------------------------- #
    # 🤖 HUGGING FACE API CALL
    # ----------------------------- #
    with st.spinner("Thinking... 🌿"):
        try:
            response = requests.post(
                MODEL_URL,
                headers=HEADERS,
                json={"inputs": full_prompt},
                timeout=60,
            )

            if response.status_code != 200:
                st.error(f"Error {response.status_code}: {response.text}")
                bot_response = "Sorry, I couldn’t process that right now."
            else:
                result = response.json()

                # Handle output depending on model response type
                if isinstance(result, list) and "generated_text" in result[0]:
                    bot_response = result[0]["generated_text"].split("Bot:")[-1].strip()
                elif isinstance(result, dict) and "error" in result:
                    bot_response = f"Error: {result['error']}"
                else:
                    bot_response = str(result)

        except requests.exceptions.RequestException as e:
            bot_response = f"Network error: {e}"

    # Display response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Save to session state
    st.session_state.chat_history.append((user_input, bot_response))
