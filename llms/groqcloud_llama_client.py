import requests
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_LLM_API_KEY = os.getenv('GROQ_LLM_API_KEY')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

if not GROQ_LLM_API_KEY:
    raise ValueError("Erro: A chave da API da GroqCloud não foi carregada. Verifique o arquivo .env.")


def get_llama_response(prompt):
    headers = {
        'Authorization': f'Bearer {GROQ_LLM_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile", 
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        resposta = response.json()
        return resposta['choices'][0]['message']['content']
    else:
        print(f"Erro: {response.status_code}, {response.text}")
        return None