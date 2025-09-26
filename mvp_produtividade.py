# mvp_produtividade.py
import streamlit as st
import openai

# Coloque sua chave da OpenAI aqui
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Agente de Organização Pessoal 🚀")
st.write("Insira suas tarefas, hábitos e compromissos e receba um plano diário/semanal personalizado.")

# Inputs do usuário
nome = st.text_input("Seu nome")
objetivos = st.text_area("Seus principais objetivos (ex: estudar, trabalhar, se exercitar)")
tarefas = st.text_area("Liste suas tarefas/hábitos principais, separadas por vírgula")

# Captura de email para leads
st.subheader("Receba novidades e ofertas")
email = st.text_input("Digite seu email para receber atualizações")

if st.button("Cadastrar email"):
    if email:
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        st.success("Email cadastrado! ✅")
    else:
        st.warning("Digite um email válido.")

# Botão para gerar plano
if st.button("Gerar plano"):
    if not tarefas or not objetivos:
        st.warning("Por favor, preencha objetivos e tarefas antes de gerar o plano.")
    else:
        try:
            # Simulação de resposta enquanto a OpenAI não está disponível
            plano = f"""
Plano de Produtividade Simulado para {nome}:

Objetivos: {objetivos}
Tarefas/Hábitos: {tarefas}

- 08:00 – 09:00: Início do dia e planejamento
- 09:00 – 12:00: Trabalho/Estudo focado
- 12:00 – 13:00: Pausa/Almoço
- 13:00 – 16:00: Trabalho/Estudo focado
- 16:00 – 16:30: Alongamento e descanso
- 16:30 – 18:00: Revisão de tarefas e preparação para amanhã

Dicas rápidas:
- Priorize tarefas mais importantes primeiro
- Use blocos de 90 minutos para foco máximo
- Registre progresso e celebre pequenas vitórias
"""
            st.subheader("Seu Plano Personalizado 📋")
            st.write(plano)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
