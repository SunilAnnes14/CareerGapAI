# ---------------------------------------------
# CAREERGAP AI - STUDENT SKILL GAP ANALYZER
# ---------------------------------------------

# Skills currently possessed by the student
student_skills = [
    "python",
    "sql",
    "machine learning",
    "pandas",
    "numpy"
]


# Skills required by the industry
# These will eventually come from our SerpApi analysis

industry_skills = {
    "python": 90,
    "sql": 80,
    "machine learning": 75,
    "pandas": 65,
    "numpy": 60,
    "aws": 55,
    "docker": 45,
    "pytorch": 40,
    "kubernetes": 30,
    "llm": 35
}


# ---------------------------------------------
# Find missing skills
# ---------------------------------------------

missing_skills = []

for skill, demand in industry_skills.items():

    if skill not in student_skills:

        missing_skills.append({
            "skill": skill,
            "demand": demand
        })


# ---------------------------------------------
# Sort missing skills by industry demand
# ---------------------------------------------

missing_skills.sort(
    key=lambda x: x["demand"],
    reverse=True
)


# ---------------------------------------------
# Display CareerGap Report
# ---------------------------------------------

print("\n====================================")
print("        CAREERGAP AI")
print("====================================")

print("\nYOUR SKILLS")
print("------------------------------------")

for skill in student_skills:
    print("✓", skill)


print("\nSKILLS YOU SHOULD LEARN")
print("------------------------------------")

for item in missing_skills:

    print(
        "❌",
        item["skill"],
        "→",
        item["demand"],
        "% industry demand"
    )