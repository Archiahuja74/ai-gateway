# AI Gateway System

# Overview
This project implements an AI Gateway that intelligently routes user queries to different AI models based on the complexity of the prompt. It also includes caching to improve performance and reduce redundant API calls.

# Problem Statement
In real-world AI applications, sending all queries to a single model is inefficient and costly.  
This project solves that by:
- Routing simple queries to a fast, low-cost model  
- Routing complex queries to a more capable model  
- Caching responses to avoid repeated computation  

# Features
- Intelligent model routing (FAST vs CAPABLE)
- Integration with real AI APIs (Groq / Gemini)
- Response caching for efficiency
- FastAPI backend
- Streamlit UI for interaction
- Error handling for API failures

# Architecture
User → Streamlit UI → FastAPI Backend → Router → AI Model → Response → Cache

# Tech Stack
- Python
- FastAPI
- Streamlit
- Requests
- Python-dotenv
- Groq API (LLaMA)
- Google Gemini API

# Project Structure
ai-gateway/
│── main.py          # Backend (FastAPI)
│── router.py        # Model selection logic
│── cache.py         # Cache implementation
│── ui.py            # Frontend (Streamlit)
│── .env             # API keys (not shared)
│── README.md

# Setup Instructions
Clone the repository
git clone <your-repo-link>  
cd ai-gateway  

Install dependencies
pip install fastapi uvicorn streamlit requests python-dotenv  

Add API Keys
Create a .env file:

GROQ_API_KEY=your_groq_key  
GEMINI_API_KEY=your_gemini_key  

# Run the Project
Start Backend
python -m uvicorn main:app --reload  

Start UI
python -m streamlit run ui.py  

# Example Usage

- Input: "What is AI?" → Routed to FAST model  
- Input: "Write a Python program for Dijkstra's algorithm" → Routed to CAPABLE model  
- Repeated query → Served from CACHE  

# Key Learnings
- Model routing improves efficiency and cost
- Caching reduces redundant API calls
- Handling API failures is critical in production systems
- Combining backend + UI gives full system understanding

# Future Improvements
- Add rate limiting
- Add authentication
- More advanced routing logic (token-based / semantic)
- Logging & monitoring

# Author
Archi Ahuja
