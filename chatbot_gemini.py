import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar a chave do Gemini da variável de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Atualize o nome do modelo com base na saída de ListModels
modelo = genai.GenerativeModel('models/gemini-1.5-pro-001')  # Substitua pelo modelo correto

def perguntar_ao_chatbot(pergunta):
    try:
        resposta = modelo.generate_content(f"Responda como um especialista em tecnologia: {pergunta}")
        return resposta.text.strip()
    except Exception as e:
        return f"Erro ao acessar a API do Gemini: {e}"

def iniciar_chat():
    print("🤖 Chatbot de Tecnologia (IA Gemini) | Digite 'sair' para encerrar.")
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() == "sair":
            print("Encerrando o chat. Até logo!")
            break
        resposta = perguntar_ao_chatbot(pergunta)
        print(f"Bot: {resposta}")

if __name__ == "__main__":
    iniciar_chat()
