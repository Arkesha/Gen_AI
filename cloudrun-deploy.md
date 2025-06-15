# GCP Cloud Run Deployment Instructions

## 1. Build Docker Image
docker build -t chatbot:v2 .

## 2. Tag Image for Artifact Registry
docker tag chatbot:v2 us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2

## 3. Push Image to Artifact Registry
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2

## 4. Deploy to Cloud Run
gcloud run deploy chatbot \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/chatbot-repo/chatbot:v2 \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
