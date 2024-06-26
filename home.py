# home.py
import streamlit as st
import ML

def main(user_id, pdf_texts):
    # st.set_page_config(page_title="Doctor", page_icon=" ")

    def chat_doc():
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        st.title("Chat with AI Interviewer")

        # Process each PDF text
        for pdf_text in pdf_texts:
            health_info = ML.extract_health_info(pdf_text)
            st.session_state["chat_history"].append({"user_health_history": pdf_text})
            st.session_state["chat_history"].append({"Health_Info": health_info})
        
        # Text input for user messages
        user_input = st.text_input("Your message")

        if user_input:
            # Get response from OpenAI
            ai_response = ML.extract_health_info(user_input)

            # Append user message and AI response to chat history
            st.session_state["chat_history"].append({"user": user_input, "ai": ai_response})
        
        # Display chat history
        for chat in st.session_state["chat_history"]:
            with st.container():
                if "user_health_history" in chat:
                    st.markdown(f"<div style='text-align: right;'>{chat['user_health_history']}</div>", unsafe_allow_html=True)
                if "Health_Info" in chat:
                    st.markdown(f"<div style='text-align: left;'>{chat['Health_Info']}</div>", unsafe_allow_html=True)
                if "user" in chat:
                    st.markdown(f"<div style='text-align: right;'>User: {chat['user']}</div>", unsafe_allow_html=True)
                if "ai" in chat:
                    st.markdown(f"<div style='text-align: left;'>AI: {chat['ai']}</div>", unsafe_allow_html=True)

    st.session_state["id"] = user_id

    # Display chat interface
    chat_doc()
