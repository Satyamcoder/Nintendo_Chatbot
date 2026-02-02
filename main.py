from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tavily import TavilyClient
import os
from pathlib import Path
from knowledge_base import SWITCH_2_KNOWLEDGE

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

# Initialize Tavily search client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

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

def search_web(query: str) -> str:
    """Search the web using Tavily and return clean answer"""
    try:
        search_result = tavily_client.search(
            query=f"Nintendo Switch 2 {query}",
            search_depth="advanced",
            max_results=5,
            include_answer=True
        )
        
        # Get the direct answer from Tavily
        if search_result.get('answer'):
            return search_result['answer']
        
        # If no direct answer, extract from top result
        if search_result.get('results') and len(search_result['results']) > 0:
            top_result = search_result['results'][0]
            content = top_result.get('content', '')
            if content:
                # Clean up the content - take first meaningful sentence/paragraph
                sentences = content.split('. ')
                # Return first 2-3 sentences
                return '. '.join(sentences[:2]) + '.'
        
        return "I couldn't find current information about that. Please try rephrasing your question."
        
    except Exception as e:
        print(f"Search error: {e}")
        return "I couldn't search for that information right now. Please try again."

def check_knowledge_base(query: str) -> str:
    """Check if query is about specs that are in knowledge base"""
    query_lower = query.lower()
    
    # Specs keywords that are in knowledge base
    specs_responses = {
        "ram": "The Nintendo Switch 2 has 12GB LPDDR5 RAM.",
        "memory": "The Nintendo Switch 2 has 12GB LPDDR5 RAM.",
        "cpu": "The Nintendo Switch 2 is powered by the NVIDIA Tegra T239 processor with an 8-core ARM Cortex-A78C CPU running at 2.5GHz.",
        "processor": "The Nintendo Switch 2 is powered by the NVIDIA Tegra T239 processor with an 8-core ARM Cortex-A78C CPU running at 2.5GHz.",
        "gpu": "The Nintendo Switch 2 features an NVIDIA Ampere GPU with 1536 CUDA cores, DLSS 2.0 support, and ray tracing capabilities.",
        "graphics": "The Nintendo Switch 2 features an NVIDIA Ampere GPU with 1536 CUDA cores, DLSS 2.0 support, and ray tracing capabilities.",
        "storage": "The Nintendo Switch 2 comes with 256GB UFS 3.1 internal storage, expandable via microSD cards up to 2TB.",
        "display": "The Nintendo Switch 2 has an 8-inch 1080p OLED display with 120Hz capability and HDR support.",
        "screen": "The Nintendo Switch 2 has an 8-inch 1080p OLED display with 120Hz capability and HDR support.",
        "battery": "The Nintendo Switch 2 has a 6500mAh battery that provides 4-9 hours of battery life. It supports USB-C Power Delivery with 45W fast charging.",
        "price": "The Nintendo Switch 2 is priced at $449.99 USD.",
        "cost": "The Nintendo Switch 2 is priced at $449.99 USD."
    }
    
    for keyword, response in specs_responses.items():
        if keyword in query_lower:
            return response
    
    return None

@app.post("/chat", response_model=ChatResponse)
async def chat(question: Question):
    """Main chat endpoint - returns clean answers without sources"""
    try:
        # Initialize conversation history
        if question.session_id not in conversation_history:
            conversation_history[question.session_id] = []
        
        # First check knowledge base for specs
        kb_answer = check_knowledge_base(question.message)
        
        if kb_answer:
            response_text = kb_answer
        else:
            # Search the web for current information
            print(f"Searching web for: {question.message}")
            response_text = search_web(question.message)
        
        # Store in history
        user_message = {"role": "user", "content": question.message}
        assistant_message = {"role": "assistant", "content": response_text}
        
        conversation_history[question.session_id].append(user_message)
        conversation_history[question.session_id].append(assistant_message)
        
        return ChatResponse(
            response=response_text,
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
        "provider": "Tavily Web Search",
        "knowledge_base": "loaded",
        "search_enabled": True,
        "ai_model": "None - Direct search answers",
        "active_sessions": len(conversation_history)
    }

@app.get("/api/knowledge")
async def get_knowledge_summary():
    """Knowledge base summary"""
    return {
        "topics": [
            "Hardware Specifications",
            "Real-time Release Information",
            "Pricing and Availability",
            "Battery and Charging Details"
        ],
        "provider": "Tavily Search API",
        "response_style": "Clean answers without source citations"
    }

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=PORT)