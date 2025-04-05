import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar chave da API do Gemini do arquivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Verificar se a chave da API foi carregada corretamente
if not os.getenv("GEMINI_API_KEY"):
    st.error("A chave da API do Gemini não foi encontrada. Verifique o arquivo .env.")
    st.stop()

# Criar o modelo Gemini
modelo = genai.GenerativeModel('models/gemini-1.5-pro-001')  # Substitua pelo modelo correto

# Criar a interface do Streamlit
st.set_page_config(page_title="Chatbot de tecnologia Gemini", page_icon="🤖")
st.title("🤖 Chatbot de Tecnologia Gemini")
st.markdown("Digite sua dúvida sobre tecnologia e receba uma resposta da IA Gemini.")

# Inicializar o histórico de mensagens
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Botão para limpar conversa
if st.button("🧹 Limpar Conversa"):
    st.session_state.mensagens = []  # Limpa o histórico de mensagens
    st.rerun() # Força a atualização da interface

# Entrada do usuário
pergunta = st.text_input("Você:", key="input")

# Se a pergunta for enviada
if pergunta:
    with st.spinner("Pensando..."):
        try:
            # Enviar a pergunta para o modelo Gemini
            resposta = modelo.generate_content(f"Responda como um especialista em tecnologia: {pergunta}")
            st.session_state.mensagens.append(("Você", pergunta))
            st.session_state.mensagens.append(("Bot", resposta.text.strip()))
        except Exception as e:
            st.error(f"Erro ao acessar a API do Gemini: {e}")

# Exibir o histórico de mensagens
for autor, texto in reversed(st.session_state.mensagens):
    st.write(f"**{autor}:** {texto}")
