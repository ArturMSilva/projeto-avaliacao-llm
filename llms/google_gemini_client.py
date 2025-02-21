import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Erro: A chave da API do Google Gemini não foi encontrada. Verifique o arquivo .env.")

genai.configure(api_key=GOOGLE_API_KEY)



def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash") 
        response = model.generate_content(prompt)

        return response.text if response else "Nenhuma resposta gerada."
    except Exception as e:
        return f"Erro ao chamar a API do Gemini: {e}"