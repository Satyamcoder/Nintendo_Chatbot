Project Overview
----------------
A web search-powered chatbot that provides accurate, real-time information 
about the Nintendo Switch 2 console. Built with FastAPI, Tavily Search API, 
and deployed on Google Cloud Run.


FEATURES
=

✓ Real-Time Information: Always up-to-date with live web search results
✓ Accurate Knowledge Base: Curated specs for instant technical answers
✓ Web Search Integration: Uses Tavily API for current release dates, pricing
✓ Clean Responses: Direct answers without source clutter
✓ Conversation Memory: Maintains context within chat sessions
✓ Modern UI: Fullscreen, responsive design with smooth animations
✓ Fast & Free: 1000 free searches per month with Tavily



LIVE DEMO
=

Visit: https://switch-chatbot-445337785844.asia-south1.run.app



TECH STACK
=

Backend:
--------
- Framework: FastAPI 0.109
- Web Search: Tavily API (1000 free searches/month)
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



INSTALLATION & SETUP
=

Prerequisites:
--------------
- Python 3.11+
- Docker (for containerization)
- Google Cloud CLI (for deployment)
- Tavily API Key (free from tavily.com)

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
   export TAVILY_API_KEY="your_tavily_api_key_here"

   # Windows PowerShell
   $env:TAVILY_API_KEY="your_tavily_api_key_here"

5. Run the application
   python main.py

   Visit: http://localhost:8080


Docker Deployment (Local):
---------------------------

# Build image
docker build -t switch-chatbot .

# Run container
docker run -p 8080:8080 -e TAVILY_API_KEY="your_key" switch-chatbot


CLOUD DEPLOYMENT (GOOGLE CLOUD RUN)
=

Prerequisites:
--------------
- GCP account with billing enabled
- Google Cloud CLI installed and configured
- Tavily API key from tavily.com

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
    --set-env-vars TAVILY_API_KEY=your_tavily_api_key \
    --memory 512Mi \
    --cpu 1 \
    --timeout 300 \
    --max-instances 10

The deployment will return a URL like:
https://switch-chatbot-xxxxx.asia-south1.run.app



API ENDPOINTS
=

1. Chat Endpoint
   -------------
   POST /chat
   Content-Type: application/json

   Request Body:
   {
     "message": "When does it release in India?",
     "session_id": "user_123"
   }

   Response:
   {
     "response": "The Nintendo Switch 2 launched globally on June 5, 2025...",
     "success": true,
     "session_id": "user_123"
   }

2. Health Check
   ------------
   GET /health

   Response:
   {
     "status": "healthy",
     "provider": "Tavily Web Search",
     "knowledge_base": "loaded",
     "search_enabled": true,
     "active_sessions": 5
   }

3. Clear History
   -------------
   DELETE /chat/history/{session_id}

4. Knowledge Summary
   -----------------
   GET /api/knowledge


HOW IT WORKS
=

The chatbot uses a hybrid approach:

1. Specs Questions (RAM, CPU, GPU, Storage, etc.)
   - Answered instantly from the curated knowledge base
   - No web search needed for technical specifications
   - Example: "What's the RAM?" → "12GB LPDDR5"

2. Current Information (Release dates, prices, availability, games)
   - Searches the web in real-time using Tavily API
   - Returns clean, direct answers without showing sources
   - Example: "When does it release in India?" → Gets latest info from web

3. Response Format
   - Clean, conversational answers
   - No source citations or "Answer:" prefixes
   - Direct and to the point