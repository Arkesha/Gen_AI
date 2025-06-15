# 🛂 US Visa Consultant Chatbot 🤖🇺🇸

An AI-powered **Streamlit-based GUI chatbot** built using **LangChain** and the **Groq LLM API**
to provide conversational assistance on U.S. visa categories, eligibility, application steps, and documentation. 
The application can be run locally, in Docker, and is deployed serverlessly using **Google Cloud Run**.

---

## 🚀 Demo

👉 [Live Chatbot URL](https://chatbot-283872020917.us-central1.run.app) 

---

## 🔧 Tech Stack

| Layer            | Technology                             |
|------------------|----------------------------------------|
| 💬 LLM Backend    | [Groq API](https://groq.com/)          |
| 🧠 Framework      | [LangChain](https://www.langchain.com/)|
| 🎛️ GUI Frontend   | [Streamlit](https://streamlit.io/)     |
| 🐍 Programming    | Python 3.9+                            |
| 📦 Container      | Docker                                 |
| ☁️ Cloud Services | Google Cloud Platform (GCP)            |
| ⤴️ Deploy         | Google Cloud Run (serverless)          |
| 📦 Image Registry | GCP Artifact Registry                  |
| ⚙️ Build          | GCP Cloud Build                        |

---

## 📦 Features

- 🔍 Answers questions about U.S. visa types (B1, B2, H1B, F1, etc.)
- 📄 Guides users on required documents and eligibility
- ⚡ Groq LLM for ultra-fast responses
- 🎛️ Interactive Streamlit-based chatbot UI
- 🐳 Dockerized to run locally and on any container platform
- ☁️ Scalable deployment using GCP Cloud Run

---

## 📁 Project Structure

```bash
.
├── app.py                  # Main Streamlit app with LangChain logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container configuration
├── cloudrun-deploy.md      # GCP deployment instructions
├── cloudrun-service.yaml   # (Optional) GCP Cloud Run YAML config
