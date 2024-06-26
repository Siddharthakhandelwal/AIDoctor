import streamlit as st
import backend as sb
import home
import ML

def session(user_id):
    st.session_state["logged_in"] = True
    st.session_state["user_id"] = user_id
    home.main(user_id, [])

def sign_check(name, mail, password):
    col = sb.check()
    user_ids = [record["id"] for record in col]
    passwords = [record["Password"] for record in col]

    user_id = mail
    if mail in user_ids:
        st.error("This user already exists")
    else:
        sb.sign_up(user_id, name, mail, password)
        session(mail)

def login_check(mail, password):
    col = sb.check()
    user_ids = [record["id"] for record in col]
    passwords = [record["Password"] for record in col]

    if mail in user_ids:
        index = user_ids.index(mail)
        if password == passwords[index]:
            session(mail)
        else:
            st.error("Wrong Password")
    else:
        st.error("Please Sign Up first")

def main():
    st.title("Welcome to AI Doctor")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        with st.sidebar:
            st.title("Upload your Reports")
            pdf_docs = st.file_uploader("Upload PDF documents", accept_multiple_files=True, type=["pdf", "jpeg", "png"])
            submit = st.button("Submit")

        if pdf_docs and submit:
            pdf_texts = [ML.extract_text_from_pdf(doc) for doc in pdf_docs]
            home.main(st.session_state["user_id"], pdf_texts)
    else:
        action = st.sidebar.radio("Choose action", ["Sign Up", "Log In"])

        if action == "Sign Up":
            with st.form("signup_form"):
                name = st.text_input("Name")
                mail = st.text_input("Mail")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Sign Up")
                if submitted:
                    sign_check(name, mail, password)

        elif action == "Log In":
            with st.form("login_form"):
                mail = st.text_input("Mail")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Log In")
                if submitted:
                    login_check(mail, password)

if __name__ == "__main__":
    main()
