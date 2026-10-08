from skill_detector import (
    detect_skills,
    normalize_student_skills
)


# ==========================================
# TEST JOB DESCRIPTION
# ==========================================

text = """
We are looking for a Machine Learning Engineer
with experience in Python, PyTorch, Amazon Web Services,
Large Language Models and Retrieval-Augmented Generation.
Knowledge of Kubernetes is preferred.
"""


print("\n======================================")
print("       JOB SKILL DETECTION")
print("======================================")


skills = detect_skills(text)


for skill in skills:

    print("✓", skill)


# ==========================================
# TEST STUDENT SKILLS
# ==========================================

student_input = """
Python, sklearn, AWS Cloud, Py Torch, Mongo DB
"""


print("\n======================================")
print("       STUDENT SKILL NORMALIZATION")
print("======================================")


student_skills = normalize_student_skills(
    student_input
)


for skill in student_skills:

    print("✓", skill)