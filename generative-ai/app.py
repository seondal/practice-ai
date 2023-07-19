import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("Generative AI")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", [ "256x256", "512x512", "1024x1024"])
    submit = st.form_submit_button("submit")

if submit and user_input:
    GPT_Prompt = [{
        "role": "system",
        "content": "영어 한 단어로 바꿔줘"
    }]
    GPT_Prompt.append({
        "role": "user",
        "content": user_input
    })
    with st.spinner("Translating..."):
        GPT_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = GPT_Prompt
        )
    word_eng = GPT_response["choices"][0]["message"]["content"]

    prompt_dalle = f"Please draw {word_eng} in Claude Monet's style"

    with st.spinner("Wating for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt = prompt_dalle,
            size = size
        )
    st.image(dalle_response["data"][0]["url"])