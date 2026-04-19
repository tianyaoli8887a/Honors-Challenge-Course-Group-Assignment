import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Loneliness Project", layout="wide")

SUPABASE_URL = "https://mkdvrtnedxlwwgsdittp.supabase.co"
SUPABASE_KEY = "sb_publishable_3JxtHu0cEXGphAvOVAoa-A_Ho9lG4jF"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
}

def load_messages():
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/messages?select=*&order=created_at.desc",
            headers=HEADERS,
            timeout=10,
        )
        if response.status_code == 200:
            return response.json()
        return []
    except:
        return []

def save_message(name, contact, message):
    payload = {
        "name": name.strip() if name.strip() else "Anonymous",
        "contact": contact.strip(),
        "message": message.strip(),
    }
    try:
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/messages",
            headers=HEADERS,
            json=payload,
            timeout=10,
        )
        return response.status_code in [200, 201]
    except:
        return False

st.title("Group: Carina, Alexis, RJ, Tian")
st.write("This page collects our current literature review materials and provides a place for students to leave a message if they feel isolated or want connection.")

tab1, tab2, tab3, tab4 = st.tabs(["Landing Page", "Literature Review", "Why This Matters", "Leave a Message"])

with tab1:
    st.write("Credit: Carina, Alexis, RJ")

with tab2:
    st.write("Credit: Carina, Alexis, RJ")

with tab3:
    st.write("Credit: Carina, Alexis, RJ")

with tab4:
    st.write("Credit: Carina, Alexis, RJ")
    st.header("Leave a Message")
    st.write("If someone feels isolated, they can leave a short message below.")

    with st.form("message_form"):
        name = st.text_input("Your name or username")
        contact = st.text_input("Your contact (optional)")
        message = st.text_area("Your message")
        submitted = st.form_submit_button("Post Message")

        if submitted:
            if message.strip():
                success = save_message(name, contact, message)
                if success:
                    st.success("Your message has been posted.")
                else:
                    st.error("Failed to post message. Please try again.")
            else:
                st.warning("Please enter a message before posting.")

    st.subheader("Recent Messages")
    messages = load_messages()

    if messages:
        for msg in messages:
            st.markdown("---")
            st.write(f"**Name:** {msg.get('name', '')}")
            if msg.get("contact", ""):
                st.write(f"**Contact:** {msg.get('contact', '')}")
            st.write(f"**Message:** {msg.get('message', '')}")
            st.write(f"**Time:** {msg.get('created_at', '')}")
    else:
        st.info("No messages yet.")
