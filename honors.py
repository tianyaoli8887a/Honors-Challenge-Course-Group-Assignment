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
MATCH_FILE = BASE_DIR / "anonymous_matches.json"

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
