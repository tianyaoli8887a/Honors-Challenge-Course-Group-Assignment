import json
import statistics
from datetime import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Loneliness Project", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
MESSAGE_FILE = BASE_DIR / "messages.json"
MATERIALS_FILE = BASE_DIR / "hnrs_materials_extracted.json"
HPA_IMAGE = BASE_DIR / "assets" / "image1.png"


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
    first_sheet = next(iter(sheets))
    return sheets[first_sheet]


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
            record[key] = padded[index]
        records.append(record)
        if limit and len(records) >= limit:
            break
    return records


def render_paragraphs(paragraphs):
    for paragraph in paragraphs:
        if paragraph.strip():
            st.write(paragraph.strip())


def render_bullets(items):
    for item in items:
        st.markdown(f"- {item}")


def safe_get(items, index, default=""):
    if 0 <= index < len(items):
        return items[index]
    return default


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

    normalized_records = rows_to_records(normalized_rows)
    normalized_values = []
    for record in normalized_records:
        try:
            normalized_values.append(float(record.get("Normalized S", "")))
        except Exception:
            continue

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
                "Group": group_id,
                "Average Raw Score": round(statistics.mean(members), 1),
                "Average Normalized S": round(statistics.mean(members) / 66, 3),
                "Members": len(members),
            }
        )

    return {
        "sample_size": len(scores),
        "raw_response_count": max(len(response_rows) - 1, 0),
        "mean_score": round(statistics.mean(scores), 1) if scores else None,
        "median_score": round(statistics.median(scores), 1) if scores else None,
        "min_score": min(scores) if scores else None,
        "max_score": max(scores) if scores else None,
        "mean_normalized_s": round(statistics.mean(normalized_values), 3)
        if normalized_values
        else None,
        "category_counts": category_counts,
        "group_averages": group_average_records,
    }


def extract_survey_question_sections(materials):
    paragraphs = get_doc_paragraphs(
        materials,
        "Sociality Survey Questions and Explanation.docx",
    )
    sections = {"Reciprocation": [], "Endurance": [], "Proactivity": []}
    current = None
    for paragraph in paragraphs:
        if paragraph in sections:
            current = paragraph
            continue
        if paragraph == "Scoring and Aggregation":
            current = None
            continue
        if current and paragraph and not paragraph.startswith("Measuring "):
            sections[current].append(paragraph)
    return sections


materials = load_materials()
stats = compute_sociality_stats(materials)
survey_sections = extract_survey_question_sections(materials)
link_doc = get_doc_paragraphs(materials, "Link between fin + LN for website.docx")
abstract_paragraphs = get_doc_paragraphs(materials, "Abstract.docx")
research_notes = get_doc_paragraphs(materials, "HNRS research_.docx")
modeling_notes = get_doc_paragraphs(
    materials,
    "Copy of Modeling Sociality and Group Dynamics.docx",
)
timeline_notes = get_doc_paragraphs(
    materials,
    "Timeline, goal, and information for HNRS project.docx",
)
brainstorming_notes = get_doc_paragraphs(materials, "hypothesis brainstorming.docx")
financial_questions = get_doc_paragraphs(
    materials,
    "Additional financial health questions.docx",
)
neurobio_notes = get_doc_paragraphs(
    materials,
    "Literature review - Neurobiology part.docx",
)
virtue_formula_notes = get_doc_paragraphs(materials, "Virtue formula.docx")
analysis_pages = get_pdf_pages(materials, "Sociality Survey Results Analysis.pdf")
survey_explanation = get_doc_paragraphs(
    materials,
    "Sociality Survey Questions and Explanation.docx",
)

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
response_preview_records = []
for record in rows_to_records(
    get_sheet_rows(
        materials,
        "Sociality Survey (Responses).xlsx",
        "Form Responses 1",
    ),
    limit=8,
):
    response_preview_records.append(
        {
            "Major/Minor": record.get("Major/Minor", ""),
            "Financial Situation": record.get(
                "How would you describe your current financial situation?",
                "",
            ),
            "Expense Worry": record.get(
                "How often do you worry about having enough money to pay for your basic monthly expenses (rent, food, bills)?",
                "",
            ),
            "Next Semester Confidence": record.get(
                "How confident are you that you can pay for next semester’s educational expenses (tuition, fees, books)?",
                "",
            ),
            "Finances Affect Daily Wellbeing": record.get(
                "Because of my money situation, I feel stress that affects my daily life and well being.",
                "",
            ),
            "Finances Affect Connection": record.get(
                "My finances prevent me from maintaining connections to friends and potential friends.",
                "",
            ),
        }
    )

st.title("Loneliness Project")
st.caption("Group: Carina, Alexis, RJ, Tian")
st.write(
    "This website collects the group's current literature review materials, survey design, early data analysis, and a place for students to leave a message if they feel isolated or want connection."
)

if not materials:
    st.warning(
        "The extracted project materials file could not be loaded. The app will still run, but the attachment-based sections may appear empty."
    )

with st.sidebar:
    st.header("Project Snapshot")
    st.markdown(
        f"""
**Processed files:** {len(materials)}  
**Analyzed sample:** {stats["sample_size"]} students  
**Raw response workbook:** {stats["raw_response_count"]} submissions  
**Engineered groups:** {len(stats["group_averages"])}
"""
    )
    st.markdown("---")
    st.markdown("**Included source files**")
    for filename in sorted(materials):
        st.write(f"- {filename}")

tab1, tab2, tab3, tab4, tab5= st.tabs(
    [
        "Landing Page",
        "Literature Review",
        "Methods and Model",
        "Survey and Results",
        "Leave a Message",
    ]
)

with tab1:
    st.write("Credit: Carina, Alexis, RJ")

    metric1, metric2, metric3, metric4 = st.columns(4)
    metric1.metric("Analyzed Sample", stats["sample_size"])
    metric2.metric("Mean Sociality Score", stats["mean_score"])
    metric3.metric("Median Score", stats["median_score"])
    metric4.metric("Average Normalized S", stats["mean_normalized_s"])

    st.header("Abstract")
    render_paragraphs(abstract_paragraphs)

    st.header("Loneliness Epidemic (Broad)")
    st.write(safe_get(link_doc, 3))

    st.header("Loneliness in College Students (Broad)")
    st.write(safe_get(link_doc, 5))

    st.header("Loneliness at AU")
    st.write(safe_get(link_doc, 7))

    st.header("Why This Matters")
    st.write(
        "This project argues that loneliness is not just an individual emotion. It is a group-level outcome shaped by how students connect, how resilient they are after difficult interactions, and how environmental pressures such as financial strain affect daily life."
    )
    st.write(
        "Rather than only describing the problem, the project also proposes a practical use case: using sociality-informed grouping to improve dorm assignments, class groups, and student support systems."
    )

    st.subheader("Current Hypothesis Direction")
    render_bullets(brainstorming_notes)

with tab2:
    st.write("Credit: Carina, Alexis, RJ")

    st.header("Biological Effects of Loneliness on College Students")
    for index in range(9, 14):
        if index < len(link_doc):
            st.write(link_doc[index])

    if HPA_IMAGE.exists():
        st.image(
            str(HPA_IMAGE),
            caption="HPA axis diagram extracted from the project photo materials.",
            use_container_width=True,
        )
        st.caption(
            "The image is placed here because it directly supports the neurobiology section and does not need to function as a text background."
        )

    st.header("Financial Health and Loneliness")
    for index in range(15, 17):
        if index < len(link_doc):
            st.write(link_doc[index])

    st.header("What Previous Research Shows")
    st.write(safe_get(link_doc, 18))

    st.header("Purpose of Our Study")
    st.write(safe_get(link_doc, 20))

    with st.expander("Detailed Neurobiology Literature Notes"):
        render_paragraphs(neurobio_notes)

    with st.expander("Annotated Bibliography and Financial-Loneliness Source Notes"):
        render_paragraphs(research_notes)

with tab3:
    st.write("Credit: Carina, Alexis, RJ")

    st.header("Methods")
    st.write(
        "The study combines a 43-question survey, score normalization, and a group-dynamics model to understand how connection patterns may help explain loneliness among college students."
    )
    render_paragraphs(modeling_notes[:5])

    st.header("The Three Sociality Traits")
    trait_cols = st.columns(3)
    with trait_cols[0]:
        st.subheader("Reciprocation")
        st.write(safe_get(survey_explanation, 1))
    with trait_cols[1]:
        st.subheader("Endurance")
        st.write(safe_get(survey_explanation, 2))
    with trait_cols[2]:
        st.subheader("Proactivity")
        st.write(safe_get(survey_explanation, 3))

    st.header("Mathematical Model")
    st.latex(r"\frac{dS}{dt} = S(1-S)\left[(\beta_0 + \delta_-) \sigma(S - \theta_{iso}) - \delta_-\right]")
    st.write(
        "The website materials explain the model as a way to estimate whether a group's aggregate sociality trends upward toward stronger connection or downward toward isolation."
    )
    render_paragraphs(link_doc[29:38])

    st.subheader("Virtue / Sociality Formula Notes")
    render_paragraphs(virtue_formula_notes)

    st.header("Scoring Interpretation")
    scoring_points = survey_explanation[49:57]
    render_paragraphs(scoring_points)

    st.header("Significance")
    render_paragraphs(link_doc[40:43])

    st.header("Limitations and Future Research")
    render_paragraphs(link_doc[44:45])
    render_paragraphs(modeling_notes[11:])

with tab4:
    st.write("Credit: Carina, Alexis, RJ")

    counts = stats["category_counts"]
    stat1, stat2, stat3, stat4 = st.columns(4)
    stat1.metric("Low Sociality", counts["Low"])
    stat2.metric("Moderate Sociality", counts["Moderate"])
    stat3.metric("High Sociality", counts["High"])
    stat4.metric("Raw Workbook Entries", stats["raw_response_count"])

    st.header("Results Summary")
    for page in analysis_pages:
        st.write(page)

    st.info(
        "The current PDF analysis appears to summarize a cleaned sample of 30 students, while the raw response workbook contains additional submissions. Both are shown here so the website reflects the current project state honestly."
    )

    st.header("Engineered Group Stability")
    st.dataframe(stats["group_averages"], use_container_width=True, hide_index=True)

    st.subheader("Balanced Sociality Group Assignments")
    st.dataframe(balanced_records, use_container_width=True, height=500)

    st.subheader("Normalized Sociality Scores")
    st.dataframe(normalized_records, use_container_width=True, height=500)

    st.header("Survey Design")
    st.write(
        "The survey measures three sociality dimensions and then layers in financial-health questions to test whether social behavior patterns and material conditions relate to loneliness."
    )

    question_tab1, question_tab2, question_tab3 = st.tabs(
        ["Reciprocation", "Endurance", "Proactivity"]
    )
    with question_tab1:
        render_bullets(survey_sections["Reciprocation"])
    with question_tab2:
        render_bullets(survey_sections["Endurance"])
    with question_tab3:
        render_bullets(survey_sections["Proactivity"])

    st.subheader("Additional Financial Health Questions")
    render_bullets(financial_questions)

    with st.expander("Anonymized Preview of Raw Survey Responses"):
        st.write(
            "Direct identifiers such as names and email addresses are intentionally excluded here. The preview keeps the substantive response patterns while avoiding unnecessary exposure of private information."
        )
        st.dataframe(response_preview_records, use_container_width=True)


with tab5:
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
