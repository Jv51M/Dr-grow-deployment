# 🌱 Dr-Grow (Deployment Repository)

**Dr-Grow** is an AI-powered plant identification web app built by **Akshay, Winnie, Vishnu, and Me**.
This repository is focused solely on **deploying the trained model** via **Streamlit**, making the application accessible to users.

> 💡 *For the complete source code, dataset, and model development details, please visit the main repository:*
> 👉 [**Dr-Grow Main Repository**](https://github.com/Jv51M/Dr-grow)

---

## 🧠 Project Overview

**Dr-Grow** identifies different plant species using an image of a plant’s leaf.
It also features an **offline AI chatbot** for interactive guidance, powered by **Ollama**.

The app is divided into two major stages:

1. **Model Development** – Creating and training a deep learning model in Python (available in the main repo).
2. **Deployment** – Delivering the model through an interactive Streamlit web interface (this repository).

Currently, the model supports **7 plant species**, based on the available dataset.

---

## ⚙️ Tech Stack

* **Streamlit** – Frontend web interface for deployment
* **TensorFlow** – Deep learning model
* **Scikit-learn** – Preprocessing and model evaluation
* **Ollama** – Offline chatbot integration (`llama3.2:1b`, `phi`)
* **Ngrok** – Secure tunneling and public access
* **QRCode**, **OpenCV**, **Matplotlib**, **NumPy**, **Pandas**, **PIL**, **Datetime** – Supporting utilities

---

## 🧩 System Requirements

* **Python version:** 3.12.9

  > ⚠️ TensorFlow may have compatibility issues with newer Python versions.
  > Use Python **3.12.9** for best performance.

---

## 🌿 Features

* Leaf-based plant identification
* Interactive, user-friendly interface
* Offline chatbot for plant care advice
* QR code generation for easy sharing
* Local or tunneled online access (via Ngrok)

---

## 🔗 Main Repository

This deployment repository contains only the code and assets necessary to **serve the trained model**.
For training scripts, datasets, and detailed implementation, visit:
👉 [**https://github.com/Jv51M/Dr-grow**](https://github.com/Jv51M/Dr-grow)

---

## 🧾 License

This project is open source and available under the **MIT License**.

---
