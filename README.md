Project Overview
----------------
An AI-powered chatbot that provides accurate, up-to-date information about 
the Nintendo Switch 2 console. Built with FastAPI, Groq AI (Llama 3.3 70B), 
and deployed on Google Cloud Run.

Status: Live
Python Version: 3.11
Framework: FastAPI 0.109
AI Provider: Groq (Free)
Cloud Platform: Google Cloud Run


=
FEATURES
=

✓ Accurate Knowledge Base: Curated information about Switch 2 specs, pricing, and games
✓ AI-Powered Responses: Uses Groq's Llama 3.3 70B model (FREE)
✓ Hallucination Prevention: Strict prompt engineering to prevent misinformation
✓ Conversation Memory: Maintains context within chat sessions
✓ Modern UI: Fullscreen, responsive design with smooth animations
✓ Fast & Free: Lightning-fast responses with zero API costs


=
LIVE DEMO
=

Visit: https://switch-chatbot-445337785844.asia-south1.run.app


=
TECH STACK
=

Backend:
--------
- Framework: FastAPI 0.109
- AI Model: Groq (Llama 3.3 70B Versatile)
- Python: 3.11
- HTTP Server: Uvicorn

Frontend:
---------
- HTML5 + CSS3 + Vanilla JavaScript
- Responsive Design: Mobile-first approach
- Modern UI: Purple gradient theme, smooth animations

Infrastructure:
---------------
- Cloud Platform: Google Cloud Platform (GCP)
- Deployment: Cloud Run (Container-based)
- Region: Asia South 1 (Mumbai)
- Containerization: Docker


=
PROJECT STRUCTURE
=

switch-chatbot/
├── main.py              # FastAPI backend with Groq integration
├── knowledge_base.py    # Curated Switch 2 facts and system prompt
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
├── .dockerignore        # Files to exclude from Docker build
├── README.txt           # Project documentation (this file)
└── static/
    └── index.html       # Fullscreen chat interface


=
INSTALLATION & SETUP
=

Prerequisites:
--------------
- Python 3.11+
- Docker (for containerization)
- Google Cloud CLI (for deployment)
- Groq API Key (free from console.groq.com)

Local Development:
------------------

1. Clone the repository
   git clone <your-repo-url>
   cd switch-chatbot

2. Create virtual environment
   python -m venv venv

   # Activate (Linux/Mac)
   source venv/bin/activate

   # Activate (Windows)
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Set environment variable

   # Linux/Mac
   export GROQ_API_KEY="your_groq_api_key_here"

   # Windows PowerShell
   $env:GROQ_API_KEY="your_groq_api_key_here"

5. Run the application
   python main.py

   Visit: http://localhost:8080


Docker Deployment (Local):
---------------------------

# Build image
docker build -t switch-chatbot .

# Run container
docker run -p 8080:8080 -e GROQ_API_KEY="your_key" switch-chatbot


=
CLOUD DEPLOYMENT (GOOGLE CLOUD RUN)
=

Prerequisites:
--------------
- GCP account with billing enabled
- Google Cloud CLI installed and configured

Deploy to Cloud Run:
--------------------

# Authenticate
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Deploy (Mumbai region)
gcloud run deploy switch-chatbot \
    --source . \
    --platform managed \
    --region asia-south1 \
    --allow-unauthenticated \
    --set-env-vars GROQ_API_KEY=your_groq_api_key \
    --memory 512Mi \
    --cpu 1 \
    --timeout 300 \
    --max-instances 10

The deployment will return a URL like:
https://switch-chatbot-xxxxx.asia-south1.run.app


=
API ENDPOINTS
=

1. Chat Endpoint
   -------------
   POST /chat
   Content-Type: application/json

   Request Body:
   {
     "message": "What are the Switch 2 specs?",
     "session_id": "user_123"
   }

   Response:
   {
     "response": "The Nintendo Switch 2 features...",
     "success": true,
     "session_id": "user_123"
   }

2. Health Check
   ------------
   GET /health

   Response:
   {
     "status": "healthy",
     "provider": "Groq",
     "model": "llama-3.3-70b-versatile",
     "knowledge_base": "loaded",
     "active_sessions": 5
   }

3. Clear History
   -------------
   DELETE /chat/history/{session_id}

4. Knowledge Summary
   -----------------
   GET /api/knowledge
