from datetime import datetime
from zoneinfo import ZoneInfo

import requests
import streamlit as st

st.set_page_config(page_title="Loneliness Project", layout="wide")

SUPABASE_URL = "https://mkdvrtnedxlwwgsdittp.supabase.co"
SUPABASE_KEY = "sb_publishable_3JxtHu0cEXGphAvOVAoa-A_Ho9lG4jF"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
}

ABSTRACT = """
Loneliness is an overlooked component within the lives of young adults attending college who often must manage multiple stressors in totality for the first time in their life. In addition to improving psychological well-being it can further the resilience of the students attending universities to have their loneliness not treated as an afterthought but a core component of their time at an institution. This study, centered around the overarching theme of loneliness among college students, places a particular focus on the student population at American University. In exploring loneliness within this community through the lenses of social behavior patterns such as reciprocation, endurance, and proactivity, biological mechanisms including HPA axis dysregulation and pro-inflammatory immune activity, financial health factors such as familial support and the burden of self-managed expenses, and a mathematical model of group dynamics applied to survey responses, we aim to communicate a near-holistic portrait of loneliness as a group-level phenomenon shaped by the distribution of sociality traits rather than individual misfortune alone.
"""

LANDING_BROAD = """
Loneliness is defined as being a situation in which an individual feels an unpleasant lack of quality relationships (Batsleer and Duggan 17). Since loneliness was first formally quantified in the 1960s, the urgency of the loneliness epidemic has continued to increase, despite advances in technology that have reduced the cost and increased the ease of communicating with loved ones. A survey conducted by Cigna in 2018 of more than 20,000 U.S. adults ages 18 years and older revealed that almost half of Americans report sometimes or always feeling alone or left out, one in four Americans rarely or never feel as though there are people who really understand them, and one in five people report they rarely or never feel close to people.
"""

LANDING_COLLEGE = """
Many students experience significant social, emotional, and financial challenges during the transition from high school to college. This period is often marked by major lifestyle changes, including leaving established support systems, adjusting to new academic expectations, and forming entirely new social networks. Among these challenges, loneliness has emerged as a particularly important concern, as many students struggle to build meaningful peer relationships in an unfamiliar environment.
"""

LANDING_AU = """
Many college freshmen, and especially those at American University, enter college without having close relationships with their peers. For a majority of students, these bonds start to develop over the first two weeks as friend groups begin to form. However, there is a significant number of students for whom these bonds do not develop over this crucial period, or those whose friend groups dissolve, leaving them feeling socially isolated. Many colleges, such as American University, offer social activities and promote clubs during this initial time period in an effort to encourage social bonding, but not all students are able to connect with others during this time, or feel isolated later in the semester after these activities and the socially ideal time to form friend groups has ended.
"""

BIOLOGY_TEXT = [
    """
Loneliness is not only a social or emotional experience but also a biological condition that has measurable effects on the brain and body. A central mechanism underlying these effects is the hypothalamic-pituitary-adrenal (HPA) axis, the body's primary stress response system. When individuals perceive themselves as socially isolated, the brain interprets this as a potential threat, activating the HPA axis and leading to the release of cortisol, a key stress hormone.
""",
    """
In the short term, this response can be adaptive, increasing alertness and mobilizing energy. However, chronic loneliness can lead to dysregulation of cortisol rhythms, including elevated overall cortisol levels and altered daily patterns of secretion. Studies of college students specifically have found that loneliness is associated with changes in daily cortisol activity, including flatter diurnal slopes and heightened cortisol awakening responses, both of which are indicators of chronic stress exposure.
""",
    """
Beyond hormonal changes, loneliness also has significant effects on immune functioning and physical health. Chronic activation of the HPA axis can disrupt normal immune processes, contributing to increased inflammation and reduced immune efficiency. Research has shown that loneliness is associated with changes in gene expression that promote pro-inflammatory activity while reducing the body's ability to regulate inflammation effectively.
""",
    """
Importantly, these biological responses do not occur in isolation. They can directly influence behavior and social functioning. Elevated stress hormones and increased threat sensitivity may make it more difficult for students to engage in social interactions, contributing to avoidance behaviors or negative perceptions of peers. This creates a feedback loop in which loneliness leads to physiological stress responses, which in turn make it more difficult to form social connections, thereby reinforcing loneliness over time.
""",
]

FINANCIAL_TEXT = [
    """
Beyond the social changes associated with the transition from high school to college, many students undergo financial changes as well. While the extent to which students are reliant on their own ability to manage their finances varies based on family income, parental choices, school-covered expenses, and other factors, for many students, college is a time where they make their own money and cover their own, larger amount of expenses, and are less reliant upon familial funds and financial guidance.
""",
    """
Financial health is linked in some capacity to mental health. One way in which these conditions are linked is through how poor financial wellbeing limits socializing. Financial resources make it easier to bond over activities, relax, and maintain friendships. Beyond these effects on socialization, the stigma and feelings of shame associated with poverty can also have an adverse effect on mental health and increase feelings of loneliness.
""",
    """
Some studies rebuke that there is a strong interaction between financial health and loneliness, suggesting correlation rather than causation. In addition to this, several of the studies that found a strong cause-and-effect relationship between financial health and loneliness were examining older populations and countries other than the United States, so the findings may not be fully applicable to college-age students in the U.S.
""",
]

PURPOSE_TEXT = """
The purpose of this study was to better understand and address loneliness among college students by examining how social behaviors, financial health, and biological well-being interact to shape overall connection and isolation. Rather than viewing loneliness as just an emotional state, this study approaches it as a multidimensional issue influenced by how students engage with others through reciprocation, endurance, and proactivity, as well as by external stressors like financial strain and effects on physical and mental health.
"""

METHODS_TEXT = """
The study combines a 43-question survey, score normalization, and a group-dynamics model to understand how connection patterns may help explain loneliness among college students. The questionnaire was designed to measure three core sociality traits and then test how those patterns interact with financial stress and loneliness-related wellbeing outcomes.
"""

SOCIALITY_TEXT = {
    "Reciprocation": """
Reciprocation is the quality of being open when someone reaches out for connection, regardless of one's preferences, and without reducing the other party to a mere means. It asks whether someone responds in kind when others attempt to build connection.
""",
    "Endurance": """
Endurance is the quality of withstanding being let down by people without disconnecting from an attempted connection right away. It reflects resilience to rejection, delay, awkwardness, and temporary distance.
""",
    "Proactivity": """
Proactivity is the quality of being quick to make an attempt to forge bonds with others. Having high proactivity means someone is relatively quick to reach out and connect, rather than not attempting to make a connection at all.
""",
}

FORMULA_EXPLANATION = [
    "dS/dt = S(1-S)[(beta_0 + delta_-)sigma(S - theta_iso) - delta_-]",
    "S is the aggregate sociality of a population or group and ranges from 0 to 1.",
    "dS/dt is the rate of change in aggregate sociality over time.",
    "S(1-S) keeps the system bounded between 0 and 1.",
    "theta_iso is the isolation threshold, approximately 0.54.",
    "theta_growth is the growth threshold, approximately 0.51.",
]

SIGNIFICANCE_TEXT = [
    """
The sociality scores are significant because they help explain why some students experience stronger connection while others may be more vulnerable to loneliness. High scores represent individuals who actively stabilize and strengthen social networks. Moderate scores suggest students who are capable of maintaining connections but may still experience periods of loneliness without stronger social anchors.
""",
    """
Financial health scores were not a statistically significant predictor of sociality scores and explained only a limited portion of their variance in this student sample. This suggests that financial health may still matter for loneliness, but not necessarily through the same mechanisms captured by the sociality scale.
""",
    """
By using sociality as a tool for observing and forming groups, this project argues that belonging need not be left to random chance. Group composition can be engineered to increase the likelihood of creating connection and reducing isolation.
""",
]

LIMITATIONS_TEXT = """
While this study provides insight into loneliness as a structured and measurable phenomenon, it has several limitations. The model treats social groups as closed systems, does not yet fully account for barriers such as homophily, and is limited by the absence of high-sociality individuals in the sample. Future research should examine open social systems, longitudinal change, and whether these traits can be strengthened over time.
"""

SURVEY_QUESTIONS = {
    "Reciprocation": [
        "Does your friend group mostly look or sound like you?",
        "When someone initiates a conversation, do you provide engaging responses rather than one-word answers?",
        "Are you open to meeting and connecting with people who have very different interests from your own?",
        "Do you avoid ghosting people who are making a sincere effort to connect?",
    ],
    "Endurance": [
        "If a friend cancels plans last minute, are you able to stay positive and suggest a new time later?",
        "Can you stay interested in a connection even if the other person takes a day or two to text back?",
        "Can you tolerate a period of low communication in a friendship without assuming the bond is broken?",
        "Are you able to distinguish between someone being busy and someone being intentionally hurtful?",
    ],
    "Proactivity": [
        "Are you usually the first person in your friend group to suggest a plan or a get-together?",
        "Do you introduce yourself to new people when you enter a room or join a new group?",
        "Do you actively look for new opportunities to form connections in your daily life?",
        "Do you consistently follow up with people you have recently met to keep the momentum going?",
    ],
}

FINANCIAL_QUESTIONS = [
    "How would you describe your current financial situation?",
    "How often do you worry about having enough money to pay for your basic monthly expenses (rent, food, bills)?",
    "How confident are you that you can pay for next semester's educational expenses (tuition, fees, books)?",
    "Because of my money situation, I feel stress that affects my daily life and wellbeing.",
    "How would you describe your family's overall financial situation?",
    "How often can your family provide you with financial help if you really need it?",
]

RESULT_SUMMARY = [
    {"Metric": "Analyzed sample", "Value": 30},
    {"Metric": "Mean raw score", "Value": 44.2},
    {"Metric": "Median raw score", "Value": 45.0},
    {"Metric": "Score range", "Value": "29 to 53"},
    {"Metric": "High sociality", "Value": "0 students (0%)"},
    {"Metric": "Moderate sociality", "Value": "27 students (90%)"},
    {"Metric": "Low sociality", "Value": "3 students (10%)"},
]

GROUP_SUMMARY = [
    {"Group": 1, "Average Raw Score": 44.0, "Average Normalized S": 0.667, "Members": 6},
    {"Group": 2, "Average Raw Score": 44.0, "Average Normalized S": 0.667, "Members": 6},
    {"Group": 3, "Average Raw Score": 44.3, "Average Normalized S": 0.671, "Members": 6},
    {"Group": 4, "Average Raw Score": 44.5, "Average Normalized S": 0.674, "Members": 6},
    {"Group": 5, "Average Raw Score": 44.2, "Average Normalized S": 0.670, "Members": 6},
]

TEAM_NOTES = [
    "Carina: add significance information and find pictures.",
    "RJ: finish methods section and add significance and limitations information.",
    "Alexis: add significance and limitations information.",
    "Tianyao: transfer new text onto website and add colors and pictures to website.",
]


def load_messages():
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/messages?select=*&order=created_at.desc",
            headers=HEADERS,
            timeout=10,
        )
        if response.status_code == 200:
            return response.json()
        return 
    except Exception:
        return 


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
    except Exception:
        return False


def format_time(utc_time_str):
    try:
        dt = datetime.fromisoformat(utc_time_str.replace("Z", "+00:00"))
        local_dt = dt.astimezone(ZoneInfo("America/New_York"))
        return local_dt.strftime("%Y-%m-%d %I:%M:%S %p")
    except Exception:
        return utc_time_str


def write_list(items):
    for item in items:
        st.write(item)


st.title("Loneliness Project")
st.caption("Group: Carina, Alexis, RJ, Tian")
st.write(
    "This website collects the group's current literature review materials, survey design, results summary, and a place for students to leave a message if they feel isolated or want connection."
)

with st.sidebar:
    st.header("Project Snapshot")
    st.markdown(
        """
Pages: 6
Survey length: 43 questions
Analyzed sample: 30 students
Engineered groups: 5
"""
    )

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Landing Page",
        "Literature Review",
        "Methods and Model",
        "Survey and Results",
        "Project Notes",
        "Leave a Message",
    ]
)

with tab1:
    st.write("Credit: Carina, Alexis, RJ")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Survey Questions", 43)
    c2.metric("Analyzed Sample", 30)
    c3.metric("Mean Score", 44.2)
    c4.metric("Engineered Groups", 5)

    st.header("Abstract")
    st.write(ABSTRACT)

    st.header("Loneliness Epidemic (Broad)")
    st.write(LANDING_BROAD)

    st.header("Loneliness in College Students (Broad)")
    st.write(LANDING_COLLEGE)

    st.header("Loneliness at AU")
    st.write(LANDING_AU)

    st.header("Why This Matters")
    st.write(
        "This project treats loneliness as more than an individual feeling. It frames loneliness as a group-level outcome influenced by social behavior, biology, and financial strain."
    )
    st.write(
        "The practical goal is not only to describe loneliness, but also to create a model that could help universities make better group assignments, room recommendations, and student support interventions."
    )

with tab2:
    st.write("Credit: Carina, Alexis, RJ")

    st.header("Biological Effects of Loneliness on College Students")
    write_list(BIOLOGY_TEXT)

    st.header("Financial Health and Loneliness")
    write_list(FINANCIAL_TEXT[:2])

    st.header("What Previous Research Shows")
    st.write(FINANCIAL_TEXT[2])

    st.header("Purpose of Our Study")
    st.write(PURPOSE_TEXT)

with tab3:
    st.write("Credit: Carina, Alexis, RJ")

    st.header("Methods")
    st.write(METHODS_TEXT)

    st.header("The Three Sociality Traits")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Reciprocation")
        st.write(SOCIALITY_TEXT["Reciprocation"])
    with col2:
        st.subheader("Endurance")
        st.write(SOCIALITY_TEXT["Endurance"])
    with col3:
        st.subheader("Proactivity")
        st.write(SOCIALITY_TEXT["Proactivity"])

    st.header("Mathematical Model")
    st.latex(r"\frac{dS}{dt} = S(1-S)\left[(\beta_0 + \delta_-) \sigma(S - \theta_{iso}) - \delta_-\right]")
    for line in FORMULA_EXPLANATION:
        st.write(line)

    st.header("Significance")
    write_list(SIGNIFICANCE_TEXT)

    st.header("Limitations and Future Research")
    st.write(LIMITATIONS_TEXT)

with tab4:
    st.write("Credit: Carina, Alexis, RJ")

    a, b, c, d = st.columns(4)
    a.metric("Low Sociality", 3)
    b.metric("Moderate Sociality", 27)
    c.metric("High Sociality", 0)
    d.metric("Groups", 5)

    st.header("Results Summary")
    st.dataframe(RESULT_SUMMARY, use_container_width=True, hide_index=True)

    st.header("Engineered Group Stability")
    st.dataframe(GROUP_SUMMARY, use_container_width=True, hide_index=True)

    st.header("Survey Design")
    sub1, sub2, sub3 = st.tabs(["Reciprocation", "Endurance", "Proactivity"])
    with sub1:
        for question in SURVEY_QUESTIONS["Reciprocation"]:
            st.markdown(f"- {question}")
    with sub2:
        for question in SURVEY_QUESTIONS["Endurance"]:
            st.markdown(f"- {question}")
    with sub3:
        for question in SURVEY_QUESTIONS["Proactivity"]:
            st.markdown(f"- {question}")

    st.subheader("Additional Financial Health Questions")
    for question in FINANCIAL_QUESTIONS:
        st.markdown(f"- {question}")


with tab5:
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
            st.write(f"Name: {msg.get('name', '')}")
            if msg.get("contact", ""):
                st.write(f"Contact: {msg.get('contact', '')}")
            st.write(f"Message: {msg.get('message', '')}")
            st.write(f"Time: {format_time(msg.get('created_at', ''))}")
    else:
        st.info("No messages yet.")
