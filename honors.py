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
