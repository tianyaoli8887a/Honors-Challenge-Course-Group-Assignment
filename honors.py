import json
import statistics
from datetime import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Honors Project", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
MESSAGE_FILE = BASE_DIR / "messages.json"
MATERIALS_FILE = BASE_DIR / "hnrs_materials_extracted.json"
CONNECTION_FILE = BASE_DIR / "connection_requests.json"

MAIN_TITLE = "Honors Project"
SUBTITLE = "Reducing Loneliness in College-Age Individuals Through Sociality Dynamics"
GROUP_LINE = "Group: Carina Parsons, River Jordan Pugh, Alexis Mercado, TL"
TAB_CREDIT = "Credit: Carina, Alexis, River Jordan"

ABSTRACT = """
Loneliness is an overlooked component within the lives of young adults attending college who often must manage multiple stressors in totality for the first time in their life. In addition to improving psychological well-being it can further the resilience of the students attending universities to have their loneliness not treated as an afterthought but a core component of their time at an institution. This study, centered around the overarching theme of loneliness among college students, places a particular focus on the student population at American University. In exploring loneliness within this community, through the lenses of social behavior patterns such as reciprocation, endurance, and proactivity, biological mechanisms including HPA axis dysregulation and pro-inflammatory immune activity that link chronic isolation to measurable physiological stress, financial health factors such as familial support and the burden of self-managed expenses during the transition from high school to college, and a mathematical model of group dynamics applied to survey responses from 43 questions that help to explicate why some students form meaningful connections while others experience persistent isolation while acknowledging the differing sociopolitical and economic contexts that these students come from, we aim to communicate a near-holistic portrait of loneliness as a group-level phenomenon shaped by the distribution of sociality traits rather than individual misfortune or financial strain alone. By using our study to show that loneliness is not an inherent part of the university experience and can be accounted for with attentive measures we aim to show how this can help reduce the health outcomes and financial risks associated with loneliness. Our method of analyzing sociality can be used to help form dorm assignments, class assignments, groups for projects and other means for university faculty to account for and aid their students.
"""

LANDING_BROAD = """
Loneliness is defined as being a situation in which an individual feels an unpleasant lack of quality relationships (Batsleer and Duggan 17). Since loneliness was first formally quantified in the 1960s, the urgency of the loneliness epidemic has continued to increase, despite advances in technology that have reduced the cost and increased the ease of communicating with loved ones. A survey conducted by Cigna in 2018 of more than 20,000 U.S. adults ages 18 years and older revealed that almost half of Americans report sometimes or always feeling alone or left out, one in four Americans rarely or never feel as though there are people who really understand them, and one in five people report they rarely or never feel close to people.
"""

LANDING_COLLEGE = """
Many students experience significant social, emotional, and financial challenges during the transition from high school to college. This period is often marked by major lifestyle changes, including leaving established support systems, adjusting to new academic expectations, and forming entirely new social networks. Among these challenges, loneliness has emerged as a particularly important concern, as many students struggle to build meaningful peer relationships in an unfamiliar environment.
"""

LANDING_AU = """
Many college freshmen, and especially those at American University, enter college without having close relationships with their peers. For a majority of students, these bonds start to develop over the first two weeks as friend groups begin to form. However, there is a significant number of students for whom these bonds do not develop over this crucial period, or those whose friend groups dissolve, leaving them feeling socially isolated. Many colleges, such as American University offer social activities and promote clubs during this initial time period in an effort to encourage social bonding, but not all students are able to connect with others during this time, or feel isolated later in the semester after these activities and the socially-ideal time to form friend groups has ended. After this period is over, it is difficult for many of these students to join existing social groups, contributing to loneliness in the campus environment. This loneliness, besides contributing to the higher rate of college transfers at American University compared to other private schools in the DMV area, is detrimental to student mental health and wellbeing overall (American University, 2024; CollegeRaptor, 2026).
"""

BIOLOGY_TEXT = [
    """
Loneliness is not only a social or emotional experience but also a biological condition that has measurable effects on the brain and body. A central mechanism underlying these effects is the hypothalamic-pituitary-adrenal (HPA) axis, the body's primary stress response system. When individuals perceive themselves as socially isolated, the brain interprets this as a potential threat, activating the HPA axis and leading to the release of cortisol, a key stress hormone (Freilich et al., 2024; Mavrych et al., 2025).
""",
    """
In the short term, this response can be adaptive, increasing alertness and mobilizing energy. However, chronic loneliness such as that experienced by some students during the transition to college can lead to dysregulation of cortisol rhythms, including elevated overall cortisol levels and altered daily patterns of secretion (Mavrych et al., 2025). Studies of college students specifically have found that loneliness is associated with changes in daily cortisol activity, including flatter diurnal slopes and heightened cortisol awakening responses, both of which are indicators of chronic stress exposure (Drake et al., 2016; Matias et al., 2011). These disruptions suggest that even everyday experiences of social isolation can produce sustained physiological stress responses during this critical developmental period.
""",
    """
Beyond hormonal changes, loneliness also has significant effects on immune functioning and physical health. Chronic activation of the HPA axis can disrupt normal immune processes, contributing to increased inflammation and reduced immune efficiency. Research has shown that loneliness is associated with changes in gene expression that promote pro-inflammatory activity while reducing the body's ability to regulate inflammation effectively (Pourriyahi et al., 2021; Cacioppo & Cacioppo et al., 2016). These immune changes are particularly concerning because they have been linked to a range of negative health outcomes, including poorer cardiovascular health, sleep disturbances, and increased susceptibility to illness (Hawkley et al., 2010).
""",
    """
Importantly, these biological responses do not occur in isolation. They can directly influence behavior and social functioning. Elevated stress hormones and increased threat sensitivity may make it more difficult for students to engage in social interactions, contributing to avoidance behaviors or negative perceptions of peers. This creates a feedback loop in which loneliness leads to physiological stress responses, which in turn make it more difficult to form social connections, thereby reinforcing loneliness over time.
""",
    """
For college students, particularly those navigating the transition to a new environment, these findings highlight the importance of understanding loneliness as both a psychological and physiological experience. The biological consequences of loneliness suggest that factors which contribute to social isolation such as difficulty forming friendships or external stressors like financial strain may have broader implications for student health and wellbeing. Understanding these mechanisms provides a foundation for examining how different aspects of students' lives, including financial and physical health, may interact with loneliness in this population.
""",
]

FINANCIAL_TEXT = [
    """
Beyond the social changes associated with the transition from high school to college, many students undergo financial changes as well. While the extent to which students are reliant on their own ability to manage their finances varies based on family income, parental choices, school-covered expenses, and other factors, for many students, college is a time where they make their own money and cover their own, larger amount of expenses, and are less reliant upon familial funds and financial guidance. This can lead to financial stress, as budgeting and financial skills in general are not universally taught or of a standard quality in high school, and few universities make an effort to teach students this vital skill. American University, where our survey participants are enrolled, offers for-credit financial courses and resources through their library and financial aid office (American University, n.d.). However, it does not prioritize these skills, and does not include such courses as part of their required first-year curriculum as of 2024 (American University, 2019).
""",
    """
Financial health is linked in some capacity to mental health. One way in which these conditions are linked is through how poor financial wellbeing limits socializing. A study conducted by the London newspaper The Economist demonstrated that financial resources make it easier to bond over activities, relax, and maintain friendships (The Economist, 2018). Beyond these effects on socialization, the stigma and feelings of shame associated with poverty also have an adverse effect on mental health and increase feelings of loneliness, as a study published in the Journal of American College Health shows (Xiong & Zhai, 2025).
""",
]

PREVIOUS_RESEARCH_TEXT = """
Of course, some studies rebuke that there is a strong interaction between financial health and loneliness, suggesting correlation rather than causation (Egaña-Marcos et al., 2025). In addition to this, several of the studies that had found a strong cause-and-effect relationship between financial health and loneliness were examining older populations and countries other than the United States, and as our work will focus on college-age students in the US, the findings may not be applicable.
"""

PURPOSE_TEXT = """
The purpose of this study was to better understand and address loneliness among college students by examining how social behaviors, financial health, and biological well-being interact to shape overall connection and isolation. Rather than viewing loneliness as just an emotional state, this study approaches it as a multidimensional issue influenced by how students engage with others through reciprocation, endurance, and proactivity, as well as external stressors like financial strain and effects on physical and mental health. Using a 43-question survey and a mathematical model of group dynamics, we aimed to identify patterns that explain why some students feel more connected while others experience persistent loneliness. By integrating social, financial, and biological dimensions, this research provides a more comprehensive framework for understanding loneliness in college settings and highlights practical ways students and communities can work to reduce isolation and improve overall well-being.
"""

METHODS_TEXT = [
    """
I came up with the idea of sociality while studying the concept of virtue in philosophy. The beginnings of this process involved me testing conceptual explanations of the loneliness epidemic. Initially, the same hypothetical scenario came to mind. After asking passersby and acquaintances alike, it became clear that my initial conceptions of the category were hitting something real rather than something I imagined; however, this needed testing. My hypothetical went something like this: "Imagine you and 99 other people are sitting in a conference hall. You're all on the brink of starvation and need to eat as soon as possible. Luckily, the room you're stuck in is attached to a fully stocked kitchen. What needs to happen for people to be fed?" Sans some overthought responses, the simplest answer was that someone needed to cook the food, and once they started, it just made sense to cook for others.
""",
    """
This was my pre-thesis. Everyone was "hungry," but nobody wanted to do the work of cooking the food. This is itself an issue of virtue that many philosophers might recognize immediately. And after testing it out, it at least seemed to make sense. If merely one or two or a few people were lonely, it could just be chalked up to noise. But if the loneliness epidemic is actually an epidemic, it would follow that everyone being lonely is more a matter of failure to want to do the work of creating and ensuring connection. Could it be that people, for whatever reason, viewed relationships as something to extract from as opposed to something to build with the other person? This was something to be aware of, but a hunch alone is not enough to build any rigorous body of evidence.
""",
    """
This became even more important when viewed through the lens of college students who, for the first time, are free to form or neglect social relationships on their own terms, unimpeded by stricter environments. It stands to reason that one's ability to manage a social life in college alongside other obligations is a skill that pays dividends not just in the social realm but also for health. Using the skills of formal logic, I isolated a few key variables to test distinct traits I initially viewed as central to the idea of an individual who would solve the problem I was noticing.
""",
    """
With these specific metrics in mind, I crafted the initial draft of a questionnaire to assess a person's sociality, so they could be placed in groups that would allow eusocial traits to influence each other positively. The initial goal here is for universities to use this when assigning room recommendations or forming class groups.
""",
]

SOCIALITY_TEXT = {
    "Sociality": """
Sociality is the unified amalgam of three eusocial traits that, when taken together, form a cohesive quality that trends a group's connectivity upward as opposed to downward. The three traits are Reciprocation, Endurance, and Proactivity.
""",
    "Reciprocation": """
Reciprocation is the quality of being open when someone reaches out for connection, regardless of one's preferences, and without reducing the other party to a mere means. Does someone's friend group look like them? Do they think like them? Does this person's friend group follow a particular trend? Do they tend to respond in kind when someone shows interest in connecting with them? These questions can be used to gauge reciprocation.
""",
    "Endurance": """
Endurance is the quality of withstanding being let down by people. That is to say, being stood up, left on read, or generally being excluded for a limited amount of time, and not taking it personally or disconnecting from an attempted connection right away. Those with low endurance have no tolerance for the numerous excuses a potential friend might have for not texting back within a respectable time frame. It is very important to note that endurance is not the same as having no boundaries. Rather, it is having a reasonable boundary.
""",
    "Proactivity": """
Proactivity is similar to extraversion but is not necessarily possessed by solely extraverts. It is the quality of being quick to make an attempt to forge bonds with others. Having high proactivity means someone is relatively quick to reach out and connect, rather than not attempting to make a connection. Someone high in this trait is typically going to be consistent in facilitating opportunities to connect, exchange information, or hang out.
""",
}

FORMULA_TEXT = "dS/dt = S(1-S)[(β₀ + δ₋)σ(S - θ_iso) - δ₋]"

FORMULA_EXPLANATION = [
    "S is the aggregate sociality of a population or group in this case: the mean of individual sociality scores, where each individual's sociality is itself a composite of component capacities: initiation willingness, reciprocation capacity, resilience to rejection, persistence in maintaining connections. S ranges from 0 to 1.",
    "dS/dt is the rate of change in aggregate sociality over time. Positive means the population is becoming more virtuous or self-sustaining growth. Negative means decay toward an isolation equilibrium.",
    "S(1-S) is a boundary constraint. It ensures sociality stays bounded between 0 and 1, and that change slows as you approach either extreme. Populations cannot become infinitely virtuous or infinitely degraded.",
    "σ(S - θ_iso) is a sigmoid function centered on the isolation threshold. When S is below θ_iso, approximately 0.54, this term approaches zero; interactions become unlikely because there are not enough people to reciprocate. When S is above θ_iso, this term approaches one, interactions happen, and sustainable positive dynamics become possible.",
    "β₀ is the benefit rate. When positive interactions occur, sociality increases at this rate. It captures what individuals gain from successful connections.",
    "δ₋ is the damage rate. Failed interactions, rejection, non-reciprocation, and burnout degrade sociality at this rate.",
    "θ_iso, approximately 0.54, is the isolation threshold. Below it, populations collapse into disconnection. Above it, connection networks can form.",
    "θ_growth, approximately 0.51 and derived as θ_iso - τ·ln(β₀/δ₋), is the sociality growth threshold. Below it, even if connections form, sociality still declines on net. Above it, sociality grows, and the population improves itself.",
    "The two thresholds explain why populations can be connected yet still declining, between 0.51 and 0.54, and why crossing 0.51 initiates a self-sustaining positive feedback loop.",
]

WHY_SURVEY_SOLVES_TEXT = """
The survey is meant to solve a practical problem, not just a theoretical one. If loneliness is shaped partly by the distribution of social behaviors inside a group, then institutions should be able to use those patterns when forming roommate matches, class groups, project teams, and other social environments. In that sense, the questionnaire is not just measuring feelings; it is trying to identify group conditions that make belonging more or less likely for students.
"""

SIGNIFICANCE_TEXT = [
    """
The sociality scores are significant because they help explain why some students experience stronger connection while others may be more vulnerable to loneliness. High scores, 55 to 66, represent individuals who actively stabilize and strengthen social networks, helping reduce loneliness not only for themselves but for others around them. Moderate scores, 34 to 54, which were the most common in this study, suggest students who are capable of maintaining connections but may still experience periods of loneliness without the presence of stronger social anchors. Low scores, below 34, indicate a higher risk of isolation, where patterns of interaction may not be sufficient to sustain meaningful relationships. In this dataset, the absence of high-sociality individuals and the clustering of scores in the moderate range indicate a group dynamic where loneliness may persist due to a lack of strong stabilizers. However, the abundance of those in the moderate range suggests that if this dataset were to be depicted it would show a slightly left skewed bell curve. These scores highlight that loneliness is not just an individual issue, but a group-level outcome shaped by the distribution of social behaviors within a community.
""",
    """
Financial health scores were not a statistically significant predictor of sociality scores and explained only 24 percent of their variance in this student sample. Aspects of financial health included in the survey, such as familial support, financial burden, and the impact of finances on socializing, were largely unrelated to the sociality traits measured, like being open to connection, initiating new bonds, and remaining resilient after interpersonal disappointment. Poor financial health therefore appears unlikely to be systematically linked to the interaction patterns captured by the sociality scale. However, because low sociality does not necessarily imply loneliness, it remains possible that financial health could still relate to loneliness through other pathways not captured here. Given that the sociality results point to group-level social behaviors as the main drivers of loneliness, efforts to improve students' financial health alone are unlikely to directly resolve loneliness in this community of college students.
""",
    """
By using sociality as a tool for observing and forming groups, we demonstrate that what we define as sociality need not be random but can be engineered to increase the likelihood of creating a sense of belonging. This is an important result because it shows us that the loneliness epidemic is not simply a matter of ill fortune but of poorly optimized groupings. The philosophical basis of this is that it takes the concept of relationships from resources to be mined to shared spaces that allow for connections and expansion of networks. Sociality allows us to create systems that make up for the individual obstacles that prevent connection and instead focus on the group. In social situations, people do not need to change their behavior at all to facilitate connection. Instead, trait contagion occurs through exposure to highly social people within groups, which can encourage these traits to be adopted more widely.
""",
]

LIMITATIONS_TEXT = """
While this study provides insight into loneliness as a structured and measurable phenomenon, it has several limitations. The model treats social groups as closed systems, meaning it does not fully capture how new relationships or external communities might help reduce loneliness over time. Additionally, the lack of high-sociality individuals in the sample limits our ability to observe how strong social stabilizers might buffer against loneliness in a group setting. Another limitation is that the model does not yet account for social barriers such as homophily, which may reinforce loneliness by restricting people to familiar or similar social circles. Future research should expand on this by incorporating these factors and examining open social systems where connections can grow beyond initial groups. Longitudinal studies would also be valuable in understanding how traits like endurance and proactivity develop over time and whether increasing these traits can actively reduce loneliness. By addressing these limitations, future work can build a more complete understanding of how loneliness forms and how it can be effectively reduced within college environments.
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

DEFAULT_STATS = {
    "sample_size": 30,
    "raw_response_count": 30,
    "mean_score": 44.2,
    "median_score": 45.0,
    "min_score": 29,
    "max_score": 53,
    "mean_normalized_s": 0.670,
    "category_counts": {"High": 0, "Moderate": 27, "Low": 3},
    "group_averages": [
        {
            "Group Assignment": "Group 1",
            "Average Raw Score": "44.0",
            "Average Normalized Sociality": "0.667",
            "Members": "6",
        },
        {
            "Group Assignment": "Group 2",
            "Average Raw Score": "44.0",
            "Average Normalized Sociality": "0.667",
            "Members": "6",
        },
        {
            "Group Assignment": "Group 3",
            "Average Raw Score": "44.3",
            "Average Normalized Sociality": "0.671",
            "Members": "6",
        },
        {
            "Group Assignment": "Group 4",
            "Average Raw Score": "44.5",
            "Average Normalized Sociality": "0.674",
            "Members": "6",
        },
        {
            "Group Assignment": "Group 5",
            "Average Raw Score": "44.2",
            "Average Normalized Sociality": "0.670",
            "Members": "6",
        },
    ],
}


def load_messages():
    if MESSAGE_FILE.exists():
        try:
            with MESSAGE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except Exception:
            return []
    return []


def save_messages(messages):
    with MESSAGE_FILE.open("w", encoding="utf-8") as file:
        json.dump(messages, file, indent=2, ensure_ascii=False)


def load_json_list(path):
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return data
        except Exception:
            return []
    return []


def save_json_list(path, records):
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")


@st.cache_data
def load_materials():
    if not MATERIALS_FILE.exists():
        return {}
    try:
        return json.loads(MATERIALS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def get_doc_paragraphs(materials, filename):
    return materials.get(filename, {}).get("paragraphs", [])


def get_pdf_pages(materials, filename):
    return materials.get(filename, {}).get("pages", [])


def get_sheet_rows(materials, filename, sheet_name=None):
    sheets = materials.get(filename, {}).get("sheets", {})
    if not sheets:
        return []
    if sheet_name and sheet_name in sheets:
        return sheets[sheet_name]
    return sheets[next(iter(sheets))]


def rows_to_records(rows, limit=None):
    if not rows:
        return []
    headers = [str(cell).strip() for cell in rows[0]]
    records = []
    for row in rows[1:]:
        if not any(str(cell).strip() for cell in row):
            continue
        padded = list(row) + [""] * max(0, len(headers) - len(row))
        record = {}
        for index, header in enumerate(headers):
            key = header if header else f"Column {index + 1}"
            record[key] = str(padded[index])
        records.append(record)
        if limit and len(records) >= limit:
            break
    return records


def render_paragraphs(paragraphs):
    for paragraph in paragraphs:
        text = str(paragraph).strip()
        if text:
            st.write(text)


def render_bullets(items):
    for item in items:
        text = str(item).strip()
        if text:
            st.markdown(f"- {text}")


def overlap_count(first_items, second_items):
    return len(set(first_items or []) & set(second_items or []))


def same_person(first_record, second_record):
    first_contact = str(first_record.get("contact", "")).strip().lower()
    second_contact = str(second_record.get("contact", "")).strip().lower()
    if first_contact and second_contact and first_contact == second_contact:
        return True

    first_name = str(first_record.get("name", "")).strip().lower()
    second_name = str(second_record.get("name", "")).strip().lower()
    if first_name == "anonymous" or second_name == "anonymous":
        return False
    return bool(first_name and second_name and first_name == second_name)


def score_connection_match(new_record, candidate):
    score = 0
    if new_record.get("connection_goal") == candidate.get("connection_goal"):
        score += 4
    if new_record.get("connection_style") == candidate.get("connection_style"):
        score += 3
    score += overlap_count(new_record.get("availability"), candidate.get("availability")) * 2
    if new_record.get("connection_goal") == "I feel isolated today":
        score += 1
    return score


def find_best_matches(new_record, records, scoring_function, limit=3):
    scored_matches = []
    for candidate in records:
        if candidate is new_record or same_person(new_record, candidate):
            continue
        score = scoring_function(new_record, candidate)
        if score > 0:
            scored_matches.append((score, candidate))
    scored_matches.sort(key=lambda item: item[0], reverse=True)
    return scored_matches[:limit]


def render_connection_match(match_record, score=None, show_contact=False):
    title = match_record.get("name", "Anonymous")
    st.markdown(f"**{title}**")
    if show_contact and match_record.get("contact"):
        st.write(f"Contact: {match_record.get('contact')}")
    st.write(f"Goal: {match_record.get('connection_goal', '')}")
    st.write(f"Preferred connection: {match_record.get('connection_style', '')}")
    if match_record.get("availability"):
        st.write(f"Availability: {', '.join(match_record.get('availability', []))}")
    if match_record.get("note"):
        st.write(f"Note: {match_record.get('note')}")
    if score is not None:
        st.caption(f"Match strength: {score}")


def extract_survey_question_sections(materials):
    paragraphs = get_doc_paragraphs(
        materials,
        "Sociality Survey Questions and Explanation.docx",
    )
    sections = {"Reciprocation": [], "Endurance": [], "Proactivity": []}
    current = None
    for paragraph in paragraphs:
        text = str(paragraph).strip()
        if text in sections:
            current = text
            continue
        if text == "Scoring and Aggregation":
            current = None
            continue
        if current and text and not text.startswith("Measuring "):
            sections[current].append(text)
    return sections


def compute_sociality_stats(materials):
    balanced_rows = get_sheet_rows(
        materials,
        "Balanced sociality scores.xlsx",
        "Balanced_Sorting_Sheet",
    )
    normalized_rows = get_sheet_rows(
        materials,
        "Normalized sociality scores.xlsx",
        "Normalized_Sociality_Scores",
    )
    response_rows = get_sheet_rows(
        materials,
        "Sociality Survey (Responses).xlsx",
        "Form Responses 1",
    )

    scores = []
    group_members = {}
    for row in balanced_rows[1:]:
        if len(row) < 3:
            continue
        try:
            score = float(row[1])
            group_id = int(float(row[2]))
        except Exception:
            continue
        scores.append(score)
        group_members.setdefault(group_id, []).append(score)

    normalized_values = []
    for record in rows_to_records(normalized_rows):
        try:
            normalized_values.append(float(record.get("Normalized S", "")))
        except Exception:
            continue

    if not scores:
        return DEFAULT_STATS

    category_counts = {"High": 0, "Moderate": 0, "Low": 0}
    for score in scores:
        if score >= 55:
            category_counts["High"] += 1
        elif score >= 34:
            category_counts["Moderate"] += 1
        else:
            category_counts["Low"] += 1

    group_average_records = []
    for group_id, members in sorted(group_members.items()):
        group_average_records.append(
            {
                "Group Assignment": f"Group {group_id}",
                "Average Raw Score": f"{statistics.mean(members):.1f}",
                "Average Normalized Sociality": f"{statistics.mean(members) / 66:.3f}",
                "Members": str(len(members)),
            }
        )

    return {
        "sample_size": len(scores),
        "raw_response_count": max(len(response_rows) - 1, 0),
        "mean_score": round(statistics.mean(scores), 1),
        "median_score": round(statistics.median(scores), 1),
        "min_score": min(scores),
        "max_score": max(scores),
        "mean_normalized_s": round(statistics.mean(normalized_values), 3)
        if normalized_values
        else DEFAULT_STATS["mean_normalized_s"],
        "category_counts": category_counts,
        "group_averages": group_average_records or DEFAULT_STATS["group_averages"],
    }


materials = load_materials()
stats = compute_sociality_stats(materials)
survey_sections = extract_survey_question_sections(materials)

balanced_records = rows_to_records(
    get_sheet_rows(
        materials,
        "Balanced sociality scores.xlsx",
        "Balanced_Sorting_Sheet",
    )
)
normalized_records = rows_to_records(
    get_sheet_rows(
        materials,
        "Normalized sociality scores.xlsx",
        "Normalized_Sociality_Scores",
    )
)
copy_sorting_records = rows_to_records(
    get_sheet_rows(
        materials,
        "Copy of Sociality Sorting Sheet.xlsx",
        "Sheet1",
    )
)
response_preview_records = rows_to_records(
    get_sheet_rows(
        materials,
        "Sociality Survey (Responses).xlsx",
        "Form Responses 1",
    ),
    limit=8,
)
copy_response_preview_records = rows_to_records(
    get_sheet_rows(
        materials,
        "Copy of Sociality Survey (Responses).xlsx",
        "Form Responses 1",
    ),
    limit=8,
)

analysis_pages = get_pdf_pages(materials, "Sociality Survey Results Analysis.pdf")
timeline_notes = get_doc_paragraphs(
    materials,
    "Timeline, goal, and information for HNRS project.docx",
)
brainstorming_notes = get_doc_paragraphs(materials, "hypothesis brainstorming.docx")
virtue_formula_notes = get_doc_paragraphs(materials, "Virtue formula.docx")
survey_explanation = get_doc_paragraphs(
    materials,
    "Sociality Survey Questions and Explanation.docx",
)

scoring_notes = survey_explanation[49:57] if len(survey_explanation) >= 57 else []

result_summary = [
    {"Metric": "Analyzed sample", "Value": str(stats["sample_size"])},
    {"Metric": "Mean sociality score", "Value": str(stats["mean_score"])},
    {"Metric": "Median sociality score", "Value": str(stats["median_score"])},
    {
        "Metric": "Raw score range",
        "Value": f"{stats['min_score']} to {stats['max_score']}",
    },
    {
        "Metric": "High sociality",
        "Value": str(stats["category_counts"]["High"]),
    },
    {
        "Metric": "Moderate sociality",
        "Value": str(stats["category_counts"]["Moderate"]),
    },
    {
        "Metric": "Low sociality",
        "Value": str(stats["category_counts"]["Low"]),
    },
]

st.title(MAIN_TITLE)
st.subheader(SUBTITLE)
st.caption(GROUP_LINE)
st.write(
    "This website collects the group's current literature review materials, survey design, early data analysis, and a place for students to leave a message if they feel isolated or want connection."
)

with st.sidebar:
    st.header("Project Overview")
    st.markdown(
        f"""
**Pages:** 6  
**Survey length:** 43 questions  
**Analyzed sample:** {stats["sample_size"]} students  
**Group assignments:** {len(stats["group_averages"])}
"""
    )
    if materials:
        st.markdown("---")
        st.markdown(f"**Loaded source files:** {len(materials)}")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Landing Page",
        "Literature Review",
        "Methods and Model",
        "Survey and Results",
        "Connection",
        "Leave a Message",
    ]
)

with tab1:
    st.write(TAB_CREDIT)

    metric1, metric2, metric3, metric4 = st.columns(4)
    metric1.metric("Analyzed Sample", stats["sample_size"])
    metric2.metric("Mean Sociality Score", stats["mean_score"])
    metric3.metric("Median Sociality Score", stats["median_score"])
    metric4.metric("Average Normalized Sociality", stats["mean_normalized_s"])

    caption1, caption2, caption3, caption4 = st.columns(4)
    with caption1:
        st.caption("Number of scored participants included in the dataset.")
    with caption2:
        st.caption("The average raw sociality score across participants.")
    with caption3:
        st.caption("The middle score in the distribution, with half above and half below.")
    with caption4:
        st.caption("In the model, S is the group's aggregate sociality value on a 0 to 1 scale.")

    st.header("Abstract")
    st.write(ABSTRACT)

    st.header("Loneliness Epidemic")
    st.write(LANDING_BROAD)

    st.header("Loneliness in College Students")
    st.write(LANDING_COLLEGE)

    st.header("Loneliness at AU")
    st.write(LANDING_AU)

    st.header("Why This Matters")
    st.write(
        "This project treats loneliness as more than an individual feeling. It frames loneliness as a group-level outcome influenced by social behavior, biology, financial pressure, and the broader structure of student life."
    )
    st.write(
        "The practical goal is not only to describe loneliness, but also to create a framework that could help universities make better dorm assignments, class assignments, group project assignments, and other interventions that directly support student belonging."
    )

    if brainstorming_notes:
        st.subheader("Current Hypothesis Direction")
        render_bullets(brainstorming_notes)

with tab2:
    st.write(TAB_CREDIT)

    st.header("Biological Effects of Loneliness on College Students")
    render_paragraphs(BIOLOGY_TEXT)

    st.header("Financial Health and Loneliness")
    render_paragraphs(FINANCIAL_TEXT)

    st.header("Previous Research")
    st.write(PREVIOUS_RESEARCH_TEXT)

    st.header("Purpose of Our Study")
    st.write(PURPOSE_TEXT)

with tab3:
    st.write(TAB_CREDIT)

    st.header("Methods")
    render_paragraphs(METHODS_TEXT)

    st.subheader("What Problem the Survey Is Solving")
    st.write(WHY_SURVEY_SOLVES_TEXT)

    st.header("The Three Sociality Traits")
    st.write(SOCIALITY_TEXT["Sociality"])

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
    st.write(FORMULA_TEXT)
    render_bullets(FORMULA_EXPLANATION)

    if virtue_formula_notes:
        st.subheader("Additional Formula Notes")
        render_paragraphs(virtue_formula_notes)

    st.header("Limitations and Future Research")
    st.write(LIMITATIONS_TEXT)

with tab4:
    st.write(TAB_CREDIT)

    counts = stats["category_counts"]
    stat1, stat2, stat3, stat4 = st.columns(4)
    stat1.metric("Low Sociality", counts["Low"])
    stat2.metric("Moderate Sociality", counts["Moderate"])
    stat3.metric("High Sociality", counts["High"])
    stat4.metric("Group Assignments", len(stats["group_averages"]))

    result_caption1, result_caption2, result_caption3, result_caption4 = st.columns(4)
    with result_caption1:
        st.caption("Scores below 34, indicating higher risk of isolation.")
    with result_caption2:
        st.caption("Scores from 34 to 54, the most common range in this sample.")
    with result_caption3:
        st.caption("Scores from 55 to 66, representing strong social stabilizers.")
    with result_caption4:
        st.caption("Number of balanced groups formed from the scored dataset.")

    st.header("Results Summary")
    st.table(result_summary)

    st.header("Group Assignment Summary")
    st.table(stats["group_averages"])

    if analysis_pages:
        st.subheader("Analysis Notes")
        for page in analysis_pages:
            st.write(page)

    st.header("Survey Design")
    st.write(
        "The survey measures three sociality dimensions and then layers in financial-health questions to test whether social behavior patterns and material conditions relate to loneliness."
    )

    question_tab1, question_tab2, question_tab3 = st.tabs(
        ["Reciprocation", "Endurance", "Proactivity"]
    )
    with question_tab1:
        render_bullets(survey_sections["Reciprocation"] or SURVEY_QUESTIONS["Reciprocation"])
    with question_tab2:
        render_bullets(survey_sections["Endurance"] or SURVEY_QUESTIONS["Endurance"])
    with question_tab3:
        render_bullets(survey_sections["Proactivity"] or SURVEY_QUESTIONS["Proactivity"])

    st.subheader("Additional Financial Health Questions")
    render_bullets(FINANCIAL_QUESTIONS)

    if balanced_records:
        with st.expander("Balanced Sociality Score Sheet"):
            st.dataframe(balanced_records, width="stretch", hide_index=True)

    if normalized_records:
        with st.expander("Normalized Sociality Score Sheet"):
            st.dataframe(normalized_records, width="stretch", hide_index=True)

    if copy_sorting_records:
        with st.expander("Original Sociality Sorting Sheet"):
            st.dataframe(copy_sorting_records, width="stretch", hide_index=True)

    if response_preview_records:
        with st.expander("Anonymized Preview of Survey Response Workbook"):
            st.dataframe(response_preview_records, width="stretch", hide_index=True)

    if copy_response_preview_records:
        with st.expander("Anonymized Preview of Copy Survey Workbook"):
            st.dataframe(copy_response_preview_records, width="stretch", hide_index=True)

    if scoring_notes:
        st.header("Scoring Interpretation")
        render_paragraphs(scoring_notes)

    if timeline_notes:
        with st.expander("Working Notes From Project Timeline"):
            render_paragraphs(timeline_notes)

    st.header("Significance")
    render_paragraphs(SIGNIFICANCE_TEXT)

with tab5:
    st.header("Connection")
    st.write(
        "This tab turns a feeling into a next step. Instead of only leaving a message, a student can ask for connection and the site will look for 1 to 2 compatible requests."
    )

    connection_records = load_json_list(CONNECTION_FILE)

    with st.form("connection_form", clear_on_submit=True):
        name = st.text_input("Your name, username, or nickname", key="connection_name")
        contact = st.text_input(
            "Best way to reach you, optional but helpful",
            key="connection_contact",
        )
        connection_goal = st.selectbox(
            "What do you need right now?",
            [
                "I want to meet someone",
                "I feel isolated today",
                "Looking for study partner",
            ],
            key="connection_goal",
        )
        availability = st.multiselect(
            "When could you connect?",
            [
                "Today",
                "This week",
                "Weekends",
                "Evenings",
                "Between classes",
                "Online",
            ],
            key="connection_availability",
        )
        connection_style = st.selectbox(
            "What kind of first connection would feel easiest?",
            [
                "Text first",
                "Meet for coffee",
                "Study together",
                "Walk and talk",
                "Online chat",
            ],
            key="connection_style",
        )
        note = st.text_area(
            "Short note, optional",
            placeholder="Example: I am new on campus and want someone to get coffee with.",
            key="connection_note",
        )
        connection_submitted = st.form_submit_button("Find a Connection")

        if connection_submitted:
            new_connection = {
                "name": name.strip() if name.strip() else "Anonymous",
                "contact": contact.strip(),
                "connection_goal": connection_goal,
                "availability": availability,
                "connection_style": connection_style,
                "note": note.strip(),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            connection_records.append(new_connection)
            save_json_list(CONNECTION_FILE, connection_records)
            st.success("Your connection request has been saved.")

            matches = find_best_matches(
                new_connection,
                connection_records[:-1],
                score_connection_match,
            )
            if matches:
                st.subheader("Possible Connection Matches")
                for score, match_record in matches:
                    st.markdown("---")
                    render_connection_match(match_record, score, show_contact=True)
            else:
                st.info(
                    "No match yet. Your request is now saved, so the next compatible person can find you."
                )

    st.subheader("Recent Connection Requests")
    if connection_records:
        for request in reversed(connection_records[-6:]):
            st.markdown("---")
            render_connection_match(request, show_contact=False)
    else:
        st.info("No connection requests yet.")

with tab6:
    st.header("Leave a Message")
    st.write("If someone feels isolated, they can leave a short message below.")

    with st.form("message_form", clear_on_submit=True):
        name = st.text_input("Your name or username")
        contact = st.text_input("Your contact (optional)")
        message = st.text_area("Your message")
        submitted = st.form_submit_button("Post Message")

        if submitted:
            if message.strip():
                messages = load_messages()
                messages.append(
                    {
                        "name": name.strip() if name.strip() else "Anonymous",
                        "contact": contact.strip(),
                        "message": message.strip(),
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
                save_messages(messages)
                st.success("Your message has been posted.")
            else:
                st.warning("Please enter a message before posting.")

    st.subheader("Recent Messages")
    messages = load_messages()

    if messages:
        for msg in reversed(messages):
            st.markdown("---")
            st.write(f"**Name:** {msg.get('name', '')}")
            if msg.get("contact", ""):
                st.write(f"**Contact:** {msg.get('contact', '')}")
            st.write(f"**Message:** {msg.get('message', '')}")
            st.write(f"**Time:** {msg.get('time', '')}")
    else:
        st.info("No messages yet.")
