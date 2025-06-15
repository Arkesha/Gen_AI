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

- 🔍 Answers questions about any U.S. visa types (B1, B2, H1B, F1, etc.)
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
├── cloudrun-service.yaml   #  GCP Cloud Run YAML config


🛠️ Installation (Local)

# 1. Clone the repo
git clone https://github.com/Arkesha/Us-visa-consultant-chatbot.git
cd visa-consultant-chatbot

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run with Streamlit
python app.py
streamlit run app.py

🐳 Docker Build & Run (Local)

# Build Docker image
docker build -t chatbot:v2 .

# Run Docker container
docker run -p 8051:8051 chatbot:v2

# Then access at: http://localhost:8051

☁️ GCP Deployment (Cloud Run)
See cloudrun-deploy.md for full deployment steps.

# Tag and push image to Artifact Registry
docker tag chatbot:v2 us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2

# Deploy on Cloud Run
gcloud run deploy chatbot \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2 \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

📄 License
This project is licensed under the MIT License.

🤝 Contributions
Feel free to fork the repo and open PRs or issues for enhancements or bug fixes.

✉️ Contact
For questions or collaboration inquiries, email: arkeshadesai@gmail.com




