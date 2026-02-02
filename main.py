from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from pathlib import Path
from knowledge_base import SWITCH_2_KNOWLEDGE, SYSTEM_PROMPT

# Initialize FastAPI
app = FastAPI(title="Nintendo Switch 2 Chatbot", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client (FREE!)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation history storage
conversation_history = {}

# Pydantic models
class Question(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str
    success: bool
    session_id: str

# Serve static files
static_path = Path("static")
if static_path.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main chatbot interface"""
    index_file = Path("static/index.html")
    if index_file.exists():
        return FileResponse(index_file)
    return HTMLResponse(content="<h1>Static files not found</h1>")

@app.post("/chat", response_model=ChatResponse)
async def chat(question: Question):
    """Main chat endpoint with Groq AI"""
    try:
        # Initialize conversation history
        if question.session_id not in conversation_history:
            conversation_history[question.session_id] = []
        
        # Build system prompt
        system_message = {
            "role": "system",
            "content": SYSTEM_PROMPT.format(knowledge_base=SWITCH_2_KNOWLEDGE)
        }
        
        # Build messages
        messages = [system_message]
        messages.extend(conversation_history[question.session_id][-10:])
        user_message = {"role": "user", "content": question.message}
        messages.append(user_message)
        
        # Call Groq API (FREE and FAST!)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Best free model
            messages=messages,
            max_tokens=600,
            temperature=0.3,
            top_p=0.9,
        )
        
        # Extract response
        assistant_message = response.choices[0].message.content
        
        # Update history
        conversation_history[question.session_id].append(user_message)
        conversation_history[question.session_id].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return ChatResponse(
            response=assistant_message,
            success=True,
            session_id=question.session_id
        )
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.delete("/chat/history/{session_id}")
async def clear_history(session_id: str):
    """Clear conversation history"""
    if session_id in conversation_history:
        conversation_history[session_id] = []
        return {"message": "Conversation history cleared", "session_id": session_id}
    return {"message": "Session not found", "session_id": session_id}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "provider": "Groq",
        "model": "llama-3.3-70b-versatile",
        "knowledge_base": "loaded",
        "active_sessions": len(conversation_history)
    }

@app.get("/api/knowledge")
async def get_knowledge_summary():
    """Knowledge base summary"""
    return {
        "topics": [
            "Release Information",
            "Hardware Specifications",
            "Display Features",
            "Controllers & Input",
            "Confirmed Games",
            "Backward Compatibility",
            "Comparison with Original Switch"
        ],
        "last_updated": "February 2026",
        "provider": "Groq (Free)",
        "model": "Llama 3.3 70B"
    }

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=PORT)