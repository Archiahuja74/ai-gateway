import os
import requests
from fastapi import FastAPI
from router import decide_model
from cache import get_from_cache, save_to_cache
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -------- GROQ FUNCTION --------
def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
       "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Groq response:", response.text)  # debug

    try:
        res_json = response.json()
    except:
        return "Error: Could not parse Groq response"

    if "choices" not in res_json:
        return "Error from Groq API: " + str(res_json)

    return res_json["choices"][0]["message"]["content"]


# -------- GEMINI FUNCTION --------
def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(url, json=data)

    print("Gemini response:", response.text)  # debug

    try:
        res_json = response.json()
        return res_json["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Error from Gemini API"


# -------- MAIN ROUTE --------
@app.post("/chat")
def chat(prompt: str):
    cached = get_from_cache(prompt)

    if cached:
        return {
            "response": cached,
            "model": "CACHE",
            "reason": "retrieved from cache"
        }

    model, reason = decide_model(prompt)

    if model == "FAST":
        response = call_groq(prompt)
    else:
        response = call_gemini(prompt)

    save_to_cache(prompt, response)

    return {
        "response": response,
        "model": model,
        "reason": reason
    }