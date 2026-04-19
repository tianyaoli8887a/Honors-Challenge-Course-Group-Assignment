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
    st.markdown("""
### Loneliness epidemic (broad)

Loneliness is defined as being a situation in which an individual feels an unpleasant lack of quality relationships (Batsleer and Duggan 17). Since loneliness was first formally quantified in the 1960s, the urgency of the loneliness epidemic has continued to increase, despite advances in technology that have reduced the cost and increased the ease of communicating with loved ones. A survey conducted by Cigna in 2018 of more than 20,000 U.S. adults ages 18 years and older revealed that almost half of Americans report sometimes or always feeling alone or left out, one in four Americans rarely or never feel as though there are people who really understand them, and one in five people report they rarely or never feel close to people.

### Loneliness in college students (broad)

Many students experience significant social, emotional, and financial challenges during the transition from high school to college. This period is often marked by major lifestyle changes, including leaving established support systems, adjusting to new academic expectations, and forming entirely new social networks. Among these challenges, loneliness has emerged as a particularly important concern, as many students struggle to build meaningful peer relationships in an unfamiliar environment.

### Loneliness at AU

Many college freshmen, and especially those at American University, enter college without having close relationships with their peers. For a majority of students, these bonds start to develop over the first two weeks as friend groups begin to form. However, there is a significant number of students for whom these bonds don’t develop over this crucial period, or those whose friend groups dissolve, leaving them feeling socially isolated. Many colleges, such as American University offer social activities and promote clubs during this initial time period in an effort to encourage social bonding, but not all students are able to connect with others during this time, or feel isolated later in the semester after these activities and the socially-ideal time to form friend groups has ended. After this period is over, it is difficult for many of these students to join existing social groups, contributing to loneliness in the campus environment. This loneliness, besides contributing to the higher rate of college transfers at American University compared to other private schools in the DMV area, is detrimental to student mental health and wellbeing overall (American University, 2024; CollegeRaptor, 2026).
""")

with tab2:
    st.write("Credit: Carina, Alexis, RJ")
    st.markdown("""
### Biological effects of loneliness on college students

Loneliness is not only a social or emotional experience but also a biological condition that has measurable effects on the brain and body. A central mechanism underlying these effects is the hypothalamic-pituitary-adrenal (HPA) axis, the body’s primary stress response system. When individuals perceive themselves as socially isolated, the brain interprets this as a potential threat, activating the HPA axis and leading to the release of cortisol, a key stress hormone (Freilich et al., 2024; Mavrych et al., 2025).

In the short term, this response can be adaptive, increasing alertness and mobilizing energy. However, chronic loneliness–such as that experienced by some students during the transition to college–can lead to dysregulation of cortisol rhythms, including elevated overall cortisol levels and altered daily patterns of secretion (Mavrych et al., 2025). Studies of college students specifically have found that loneliness is associated with changes in daily cortisol activity, including flatter diurnal slopes and heightened cortisol awakening responses, both of which are indicators of chronic stress exposure (Drake et al., 2016; Matias et al., 2011). These disruptions suggest that even everyday experiences of social isolation can produce sustained physiological stress responses during this critical developmental period.

Beyond hormonal changes, loneliness also has significant effects on immune functioning and physical health. Chronic activation of the HPA axis can disrupt normal immune processes, contributing to increased inflammation and reduced immune efficiency. Research has shown that loneliness is associated with changes in gene expression that promote pro-inflammatory activity while reducing the body’s ability to regulate inflammation effectively (Pourriyahi et al., 2021; Cacioppo & Cacioppo et al., 2016). These immune changes are particularly concerning because they have been linked to a range of negative health outcomes, including poorer cardiovascular health, sleep disturbances, and increased susceptibility to illness (Hawkley et al., 2010).

Importantly, these biological responses do not occur in isolation–they can directly influence behavior and social functioning. Elevated stress hormones and increased threat sensitivity may make it more difficult for students to engage in social interactions, contributing to avoidance behaviors or negative perceptions of peers. This creates a feedback loop in which loneliness leads to physiological stress responses, which in turn make it more difficult to form social connections, thereby reinforcing loneliness over time.

For college students, particularly those navigating the transition to a new environment, these findings highlight the importance of understanding loneliness as both a psychological and physiological experience. The biological consequences of loneliness suggest that factors which contribute to social isolation–such as difficulty forming friendships or external stressors like financial strain–may have broader implications for student health and wellbeing. Understanding these mechanisms provides a foundation for examining how different aspects of students' lives, including financial and physical health, may interact with loneliness in this population.

### Financial health and loneliness

Beyond the social changes associated with the transition from high school to college, many students undergo financial changes as well. While the extent to which students are reliant on their own ability to manage their finances varies based on family income, parental choices, school-covered expenses, and other factors, for many students, college is a time where they make their own money and cover their own, larger amount of expenses, and are less reliant upon familial funds and financial guidance. This can lead to financial stress, as budgeting and financial skills in general are not universally taught or of a standard quality in high school, and few universities make an effort to teach students this vital skill. American University, where our survey participants are enrolled, offers for-credit financial courses and resources through their library and financial aid office (American University, n.d.). However, it does not prioritize these skills, and does not include such courses as part of their required first-year curriculum as of 2024 (American University, 2019).

Financial health is linked in some capacity to mental health. One way in which these conditions are linked is through how poor financial wellbeing limits socializing. A study conducted by the London newspaper The Economist demonstrated that financial resources make it easier to bond over activities, relax, and maintain friendships (The Economist, 2018). Beyond these effects on socialization, the stigma and feelings of shame associated with poverty also have an adverse effect on mental health and increase feelings of loneliness, as a study published in the Journal of American College Health shows (Xiong & Zhai, 2025).

### What previous research shows

Of course, some studies rebuke that there is a strong interaction between financial health and loneliness, suggesting correlation rather than causation (Egaña-Marcos et al., 2025). In addition to this, several of the studies that had found a strong cause-and-effect relationship between financial health and loneliness were examining older populations and countries other than the United States, and as our work will focus on college-age students in the US, the findings may not be applicable.

### Purpose of our study

The purpose of this study was to better understand and address loneliness among college students by examining how social behaviors, financial health, and biological well-being interact to shape overall connection and isolation. Rather than viewing loneliness as just an emotional state, this study approaches it as a multidimensional issue influenced by how students engage with others (through reciprocation, endurance, and proactivity), as well as external stressors like financial strain and effects on physical and mental health. Using a 43-question survey and a mathematical model of group dynamics, we aimed to identify patterns that explain why some students feel more connected while others experience persistent loneliness. By integrating social, financial, and biological dimensions, this research provides a more comprehensive framework for understanding loneliness in college settings and highlights practical ways students and communities can work to reduce isolation and improve overall well-being.
""")

with tab3:
    st.write("Credit: Carina, Alexis, RJ")
    st.markdown("""
### Methods (survey description) (Separate page from landing)

### How I came up with the equation and how the scores were calculated

I came up with the idea of sociality while studying the concept of virtue in philosophy. The beginnings of this process involved me testing conceptual explanations of the loneliness epidemic. Initially, the same hypothetical scenario came to mind. After asking passersby and acquaintances alike, it became clear that my initial conceptions of the category were hitting something real rather than something I imagined; however, this needed testing. My hypothetical went something like this: “Imagine you and 99 other people are sitting in a conference hall. You’re all on the brink of starvation and need to eat as soon as possible. Luckily, the room you’re stuck in is attached to a fully stocked kitchen. What needs to happen for people to be fed?” Sans some overthought responses, the simplest answer was that someone needed to cook the food, and once they started, it just made sense to cook for others. This was my pre-thesis. Everyone was “hungry,” but nobody wanted to do the work of cooking the food. This is itself an issue of virtue that many philosophers might recognize immediately. And after testing it out, it at least seemed to make sense. If merely one or two or a few people were lonely, it could just be chalked up to noise. But if the loneliness epidemic is actually an epidemic, it would follow that everyone being lonely is more a matter of failure to want to do the work of creating and ensuring connection. Could it be that people, for whatever reason, viewed relationships as something to extract from as opposed to something to build with the other person? This was something to be aware of, but a hunch alone is not enough to build any rigorous body of evidence. This became even more important when viewed through the lens of college students who, for the first time, are free to form or neglect social relationships on their own terms, unimpeded by stricter environments. It stands to reason that one’s ability to manage a social life in college alongside other obligations is a skill that pays dividends not just in the social realm but also for health. Using the skills of formal logic, I isolated a few key variables to test distinct traits I initially viewed as central to the idea of an individual who would solve the problem I was noticing. Here are the definitions of what I was tracking:

Sociality: The unified amalgam of three eusocial traits that, when taken together, form a cohesive quality that trends a group's connectivity upward as opposed to downward. The three traits are Reciprocation, Endurance, and Proactivity.

Reciprocation is the quality of being open when someone reaches out for connection, regardless of one’s preferences, and without reducing the other party to a mere means. Does someone’s friend group look like them? Do they think like them? Does this person’s friend group follow a particular trend? Do they tend to respond in kind when someone shows interest in connecting with them? These questions can be used to gauge reciprocation.

Endurance is the quality of withstanding being let down by people. That is to say, being stood up, left on read, or generally being excluded for a limited amount of time, and not taking it personally or disconnecting from an attempted connection right away. Those with low endurance have no tolerance for the numerous excuses a potential friend might have for not texting back within a respectable time frame. It is very important to note that endurance is not the same as having no boundaries. Rather, it is having a reasonable boundary.

Proactivity is similar to extraversion but is not necessarily possessed by solely extraverts. It is the quality of being quick to make an attempt to forge bonds with others. Having high proactivity means someone is relatively quick to reach out and connect, rather than not attempting to make a connection. Someone high in this trait is typically going to be consistent in facilitating opportunities to connect, exchange information, or hang out.

With those definitions I devised this formal equation which I will explain below.

dS/dt = S(1-S)[(β₀ + δ₋)σ(S - θ_iso) - δ₋]

S is the aggregate sociality of a population or group in this case: the mean of individual sociality scores, where each individual's sociality is itself a composite of component capacities: initiation willingness, reciprocation capacity, resilience to rejection, persistence in maintaining connections. S ranges from 0 to 1.

dS/dt is the rate of change in aggregate sociality over time. Positive means the population is becoming more virtuous (self-sustaining growth); negative means decay toward an isolation equilibrium.

S(1-S) is a boundary constraint. It ensures sociality stays bounded between 0 and 1, and that change slows as you approach either extreme. Populations can't become infinitely virtuous or infinitely degraded.

σ(S - θ_iso) is a sigmoid function centered on the isolation threshold. When S is below θ_iso (approximately 0.54), this term approaches zero; interactions become unlikely because there aren't enough people to reciprocate. When S is above θ_iso, this term approaches one, interactions happen, and sustainable positive dynamics become possible. Ideally, we should also see the recalibration of networks, which may open up for a higher social load.

β₀ is the benefit rate. When positive interactions occur, sociality increases at this rate. It captures what individuals gain from successful connections.

δ₋ is the damage rate. Failed interactions, rejection, non-reciprocation, and burnout degrade sociality at this rate.

θ_iso (approximately 0.54) is the isolation threshold. Below it, populations collapse into disconnection. Above it, connection networks can form.

θ_growth (approximately 0.51, derived as θ_iso - τ·ln(β₀/δ₋)) is the sociality growth threshold. Below it, even if connections form, sociality still declines on net. Above it, sociality grows, and the population improves itself.

The two thresholds explain why populations can be connected yet still declining (between 0.51 and 0.54), and why crossing 0.51 initiates a self-sustaining positive feedback loop.

With these specific metrics in mind, I crafted the initial draft of a questionnaire to assess a person's sociality, so they could be placed in groups that would allow eusocial traits to influence each other positively. The initial goal here is for universities to use this when assigning room recommendations or forming class groups.

### Significance (Separate page from landing)

The sociality scores are significant because they help explain why some students experience stronger connection while others may be more vulnerable to loneliness. High scores (55-66) represent individuals who actively stabilize and strengthen social networks, helping reduce loneliness not only for themselves but for others around them. Moderate scores (34-54), which were the most common in this study, suggest students who are capable of maintaining connections but may still experience periods of loneliness without the presence of stronger social anchors. Low scores (below 34) indicate a higher risk of isolation, where patterns of interaction may not be sufficient to sustain meaningful relationships. In this dataset, the absence of high-sociality individuals and the clustering of scores in the moderate range indicate a group dynamic where loneliness may persist due to a lack of strong stabilizers. However the abundance of those in the moderate range suggests that if this dataset were to be depicted it would show a slightly left skewed bell curve. These scores highlight that loneliness is not just an individual issue, but a group-level outcome shaped by the distribution of social behaviors within a community.

Financial health scores were not a statistically significant predictor of sociality scores and explained only 24% of their variance in this student sample. Aspects of financial health included in the survey, such as familial support, financial burden, and the impact of finances on socializing, were largely unrelated to the sociality traits measured, like being open to connection, initiating new bonds, and remaining resilient after interpersonal disappointment. Poor financial health therefore appears unlikely to be systematically linked to the interaction patterns captured by the sociality scale. However, because low sociality does not necessarily imply loneliness, it remains possible that financial health could still relate to loneliness through other pathways not captured here. Given that the sociality results point to group-level social behaviors as the main drivers of loneliness, efforts to improve students’ financial health alone are unlikely to directly resolve loneliness in this community of college students.

By using sociality as a tool for observing and forming groups, we demonstrate that what we define as sociality need not be random but can be engineered to increase the likelihood of creating a sense of belonging. This is an important result because it shows us that the loneliness epidemic is not simply a matter of ill fortune but of poorly optimized groupings. The philosophical basis of this is that it takes the concept of relationships from resources to be mined to shared spaces that allow for connections and expansion of networks. Sociality allows us to create systems that make up for the individual obstacles that prevent connection and instead focus on the group. In social situations, people do not need to change their behavior at all to facilitate connection. Instead, trait contagion occurs through exposure to highly social people within groups, which can encourage these traits to be adopted more widely.

### Limitations and future research (Separate page from landing)

While this study provides insight into loneliness as a structured and measurable phenomenon, it has several limitations. The model treats social groups as closed systems, meaning it does not fully capture how new relationships or external communities might help reduce loneliness over time. Additionally, the lack of high-sociality individuals in the sample limits our ability to observe how strong social stabilizers might buffer against loneliness in a group setting. Another limitation is that the model does not yet account for social barriers such as homophily, which may reinforce loneliness by restricting people to familiar or similar social circles. Future research should expand on this by incorporating these factors and examining open social systems where connections can grow beyond initial groups. Longitudinal studies would also be valuable in understanding how traits like endurance and proactivity develop over time and whether increasing these traits can actively reduce loneliness. By addressing these limitations, future work can build a more complete understanding of how loneliness forms–and how it can be effectively reduced–within college environments.

Get group picture to put on page?

(Add in another page explaining survey methods, landing page general loneliness epidemic, then transition to other pages, look into GitHub formatting)

(Add in page summarizing the links we found between fin health and loneliness and physical health and loneliness?)

(Start off with broad loneliness epidemic, then switch to our work on college students in general, then college students at AU, maybe break it up into different pages? Make sure citations are consistent, emphasize how our work is new and significant, add limitations/future research section, “meet the researchers” tab)

(Need to add what problem survey is solving, how it helps college students)
""")

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
