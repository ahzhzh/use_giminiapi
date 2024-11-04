import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyA4cVA7LiVSXm3JlzWJwhYbawmACPsnMYE"

genai.configure(api_key=GOOGLE_API_KEY)

#model = genai.GenerativeModel('gemini-pro')

#chat = model.start_chat(history=[])

#st.title("오토코더 웹앱")
#message = st.text_input("무엇이든 물어보세요")

#if st.button("전송"):
#    response = chat.send_message(message)
#    st.write("질문에 대한 답변입니다")
#    st.write(response.text)


st.title("챗봇")

@st.cache_resource
def load_model():
    model = genai.GenerativeModel('gemini-pro')
    return model

model = load_model()

if "chat_session" not in st.session_state:
    st.session_state["chat_session"] = model.start_chat(history=[])

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메세지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("메시지 처리 중입니다"):
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response)