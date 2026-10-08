import re

from skill_dictionary import SKILL_ALIASES


# ==========================================
# DETECT SKILLS FROM JOB DESCRIPTION
# ==========================================

def detect_skills(text):

    text = text.lower()

    detected_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            pattern = (
                r"\b"
                + re.escape(alias.lower())
                + r"\b"
            )

            if re.search(pattern, text):

                detected_skills.append(skill)

                break

    return detected_skills


# ==========================================
# NORMALIZE ONE STUDENT SKILL
# ==========================================

def normalize_one_skill(skill):

    skill = skill.strip().lower()

    if not skill:

        return None


    # Check every known skill

    for standard_skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            alias = alias.lower().strip()


            # Exact match

            if skill == alias:

                return standard_skill


    # --------------------------------------
    # Additional common variations
    # --------------------------------------

    manual_aliases = {

        "sklearn": "scikit-learn",

        "scikit learn": "scikit-learn",

        "scikit_learning": "scikit-learn",

        "aws cloud": "aws",

        "amazon web services": "aws",

        "py torch": "pytorch",

        "py-torch": "pytorch",

        "mongo db": "mongodb",

        "mongo": "mongodb",

        "k8s": "kubernetes",

        "powerbi": "power bi",

        "fast api": "fastapi",

        "large language model": "llm",

        "large language models": "llm",

        "retrieval augmented generation": "rag",

        "retrieval-augmented generation": "rag"
    }


    if skill in manual_aliases:

        return manual_aliases[skill]


    # --------------------------------------
    # Unknown skill
    # --------------------------------------

    return skill


# ==========================================
# NORMALIZE STUDENT SKILLS
# ==========================================

def normalize_student_skills(student_input):

    student_skills = []

    entered_skills = student_input.split(",")


    for entered_skill in entered_skills:

        normalized_skill = normalize_one_skill(
            entered_skill
        )


        if normalized_skill:

            if normalized_skill not in student_skills:

                student_skills.append(
                    normalized_skill
                )


    return student_skills