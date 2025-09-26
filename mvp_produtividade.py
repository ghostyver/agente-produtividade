# mvp_produtividade.py
import streamlit as st
import openai

# Coloque sua chave da OpenAI aqui
openai.api_key = "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"

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
        prompt = f"""
        Você é um assistente de produtividade.
        Usuário: {nome}
        Objetivos: {objetivos}
        Tarefas/Hábitos: {tarefas}
        Gere um plano diário/semanal detalhado, incluindo horários sugeridos e dicas rápidas de produtividade.
        """

        try:
            # Nova API compatível com openai>=1.0.0, usando GPT-3.5
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente de produtividade muito organizado."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            plano = response.choices[0].message.content
            st.subheader("Seu Plano Personalizado 📋")
            st.write(plano)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
