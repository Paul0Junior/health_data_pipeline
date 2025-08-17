import streamlit as st

#Basic interface:

st.set_page_config(page_title="Interface Básica", layout="centered")

st.title("Bem vindos à análise sobre HealthCare ")
st.write("Esta é uma interface simples criada com Streamlit.")
st.write("🚀 Teste de reload automático - edite este arquivo e veja as mudanças!")

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! Seja bem-vindo(a).")

numero = st.slider("Escolha um números", 0, 100, 50)
st.write(f"Você selecionou o número: {numero}")

if st.button("Clique aqui"):
    st.info("Você clicou no botão!")
