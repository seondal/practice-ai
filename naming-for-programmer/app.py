import streamlit as st
import openai

st.set_page_config(
    page_title="Naming for Programmer",
)

openai.api_key = st.secrets["api_key"]

st.title("Naming for Programmer")
st.text("변수나 함수를 설명하면 변수명과 함수명을 추천해드릴게요")

select = st.radio("", ("variable", "function"))

with st.form("form"):
    if select is "variable":
        vars = st.text_input("Tell me about your variables")
    elif select is "function":
        args = st.text_input("Args")
        returns = st.text_input("Returns")
    submit = st.form_submit_button("submit")

user_prompt = ""
if(select is "variable" and vars):
    user_prompt = vars
elif(select is "function" and args and returns):
    user_prompt = "a function that takes " + args + " factor and returns " + returns
        
if submit and user_prompt != "":
    GPT_Prompt = [{
        "role": "system",
        "content": "Tell me in one short word so that I can use it as a variable or function name"
    }]
    GPT_Prompt.append({
        "role": "user",
        "content" : user_prompt
    })
    GPT_response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = GPT_Prompt
    )
    prompt = GPT_response["choices"][0]["message"]["content"]
    st.write(prompt)