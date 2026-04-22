import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Loneliness Project", layout="wide")

# =========================
# storage
# =========================
MESSAGE_FILE = "messages.json"

def load_messages():
    if os.path.exists(MESSAGE_FILE):
        try:
            with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_messages(messages):
    with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)

# =========================
# header
# =========================
st.markdown("## Group: Carina, Alexis, RJ, Tian")

st.write(
    "This page collects our current literature review materials and provides a place for students to leave a message if they feel isolated or want connection."
)

st.divider()

# =========================
# navigation
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "Landing Page",
    "Literature Review",
    "Why This Matters",
    "Leave a Message"
])

# =========================
# LANDING PAGE
# =========================
with tab1:
    st.write("Credit: Carina, Alexis")

    st.header("Loneliness Epidemic (Broad)")
    st.write("""
Loneliness is defined as being a situation in which an individual feels an unpleasant lack of quality relationships (Batsleer and Duggan 17). Since loneliness was first formally quantified in the 1960s, the urgency of the loneliness epidemic has continued to increase, despite advances in technology that have reduced the cost and increased the ease of communicating with loved ones. A survey conducted by Cigna in 2018 of more than 20,000 U.S. adults ages 18 years and older revealed that almost half of Americans report sometimes or always feeling alone or left out, one in four Americans rarely or never feel as though there are people who really understand them, and one in five people report they rarely or never feel close to people.
""")

    st.header("Loneliness in College Students (Broad)")
    st.write("""
Many students experience significant social, emotional, and financial challenges during the transition from high school to college. This period is often marked by major lifestyle changes, including leaving established support systems, adjusting to new academic expectations, and forming entirely new social networks. Among these challenges, loneliness has emerged as a particularly important concern, as many students struggle to build meaningful peer relationships in an unfamiliar environment.
""")

    st.header("Loneliness at AU")
    st.write("""
Many college freshmen, and especially those at American University, enter college without having close relationships with their peers. For a majority of students, these bonds start to develop over the first two weeks as friend groups begin to form. However, there is a significant number of students for whom these bonds don’t develop over this crucial period, or those whose friend groups dissolve, leaving them feeling socially isolated. Many colleges, such as American University offer social activities and promote clubs during this initial time period in an effort to encourage social bonding, but not all students are able to connect with others during this time, or feel isolated later in the semester after these activities and the socially-ideal time to form friend groups has ended. After this period is over, it is difficult for many of these students to join existing social groups, contributing to loneliness in the campus environment. This loneliness, besides contributing to the higher rate of college transfers at American University compared to other private schools in the DMV area, is detrimental to student mental health and wellbeing overall (American University, 2024; CollegeRaptor, 2026).
""")

# =========================
# LITERATURE REVIEW
# =========================
with tab2:
    st.write("Credit: Carina, Alexis")

    st.header("Biological Effects of Loneliness on College Students")
    st.write("""
Loneliness is not only a social or emotional experience but also a biological condition that has measurable effects on the brain and body. A central mechanism underlying these effects is the hypothalamic-pituitary-adrenal (HPA) axis, the body’s primary stress response system. When individuals perceive themselves as socially isolated, the brain interprets this as a potential threat, activating the HPA axis and leading to the release of cortisol, a key stress hormone (Freilich et al., 2024; Mavrych et al., 2025).

In the short term, this response can be adaptive, increasing alertness and mobilizing energy. However, chronic loneliness can lead to dysregulation of cortisol rhythms. Studies of college students have found that loneliness is associated with changes in daily cortisol activity, including flatter diurnal slopes and heightened cortisol awakening responses.

Beyond hormonal changes, loneliness also affects immune functioning. Chronic activation of the HPA axis can disrupt normal immune processes, contributing to increased inflammation and reduced immune efficiency (Pourriyahi et al., 2021; Cacioppo & Cacioppo et al., 2016).

These biological responses can influence behavior, creating a feedback loop that reinforces loneliness over time.
""")

    st.header("Financial Health and Loneliness")
    st.write("""
Beyond social changes, many students experience financial stress. College often requires students to manage their own finances, and many lack financial education.

Financial health is linked to mental health. Limited financial resources can restrict social participation and bonding opportunities. Additionally, stigma around financial struggles can negatively affect mental wellbeing (The Economist, 2018; Xiong & Zhai, 2025).
""")

    st.header("What Previous Research Shows")
    st.write("""
Some studies suggest that financial health and loneliness are correlated rather than causally linked (Egaña-Marcos et al., 2025). Additionally, many studies focus on older populations or non-U.S. contexts, which may limit their applicability.
""")

    st.header("Purpose of Our Study")
    st.write("""
We aim to examine whether financial health, physical health, and social connection are linked to loneliness among college students.
""")

# =========================
# WHY THIS MATTERS
# =========================
with tab3:
    st.write("Credit: Carina, Alexis")

    st.header("Project Direction")
    st.write("""
At this stage, the project focuses on:

- summarizing research
- presenting it in a website format
- providing a space for user interaction

This serves as an early prototype for a larger system.
""")

# =========================
# LEAVE MESSAGE
# =========================
with tab4:
    st.header("Leave a Message")

    st.write("If someone feels isolated, they can leave a message below.")

    with st.form("message_form", clear_on_submit=True):
        name = st.text_input("Your name or username")
        contact = st.text_input("Your contact (optional)")
        message = st.text_area("Your message")

        submitted = st.form_submit_button("Post Message")

        if submitted:
            if message.strip() == "":
                st.error("Please enter a message.")
            else:
                all_messages = load_messages()

                new_message = {
                    "name": name if name else "Anonymous",
                    "contact": contact,
                    "message": message,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                all_messages.append(new_message)
                save_messages(all_messages)

                st.success("Message posted.")

    st.subheader("Messages")

    messages = load_messages()

    if len(messages) == 0:
        st.info("No messages yet.")
    else:
        for msg in reversed(messages):
            st.markdown(f"**{msg['name']}**  \n*{msg['time']}*")
            if msg["contact"]:
                st.write(f"Contact: {msg['contact']}")
            st.write(msg["message"])
            st.divider()
