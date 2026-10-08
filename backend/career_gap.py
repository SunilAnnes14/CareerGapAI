from services.job_service import JobService

from skill_detector import (
    detect_skills,
    normalize_student_skills
)

from roadmap_generator import (
    generate_roadmap,
    display_roadmap
)

from skill_dependencies import (
    create_learning_order,
    display_learning_order
)

from market_evidence import (
    build_market_evidence,
    display_market_evidence
)

from priority_engine import (
    build_priority_list,
    display_priority_list
)


# ==========================================
# CAREERGAP AI
# ==========================================

print("\n======================================")
print("          CAREERGAP AI")
print("======================================")


# ==========================================
# 1. GET STUDENT INFORMATION
# ==========================================

target_role = input(
    "\nEnter your target job role: "
)

location = input(
    "Enter your preferred location: "
)

student_input = input(
    "Enter your skills separated by commas: "
)


# ==========================================
# 2. NORMALIZE STUDENT SKILLS
# ==========================================

student_skills = normalize_student_skills(
    student_input
)


# ==========================================
# 3. DISPLAY STUDENT PROFILE
# ==========================================

print("\n======================================")
print("          STUDENT PROFILE")
print("======================================")

print(
    "Target Role :",
    target_role
)

print(
    "Location    :",
    location
)

print("\nYour Skills:")


if len(student_skills) == 0:

    print("No valid skills entered.")

else:

    for skill in student_skills:

        print("✓", skill)


# ==========================================
# 4. SEARCH JOB MARKET
# ==========================================

print("\n======================================")
print("          JOB MARKET SEARCH")
print("======================================")

print("\nSearching current job listings...")


job_service = JobService()


jobs = job_service.search_jobs(
    target_role,
    location
)


print(
    "\nJobs found:",
    len(jobs)
)


# ==========================================
# 5. CHECK IF JOBS WERE FOUND
# ==========================================

if len(jobs) == 0:

    print("\nNo jobs were found.")

    print(
        "Try another job role or location."
    )

    exit()


# ==========================================
# 6. ANALYZE JOB DESCRIPTIONS
# ==========================================

print(
    "\nAnalyzing job descriptions..."
)


skill_counts = {}


for job in jobs:

    description = job.get(
        "description",
        ""
    )


    detected_skills = detect_skills(
        description
    )


    for skill in detected_skills:

        if skill not in skill_counts:

            skill_counts[skill] = 0


        skill_counts[skill] += 1


# ==========================================
# 7. CALCULATE INDUSTRY SKILL DEMAND
# ==========================================

industry_skills = {}

total_jobs = len(jobs)


for skill, count in skill_counts.items():

    demand = (
        count / total_jobs
    ) * 100


    industry_skills[skill] = round(
        demand
    )


# ==========================================
# 8. DISPLAY INDUSTRY SKILL DEMAND
# ==========================================

print("\n======================================")
print("       INDUSTRY SKILL DEMAND")
print("======================================")


sorted_industry_skills = sorted(
    industry_skills.items(),
    key=lambda x: x[1],
    reverse=True
)


for skill, demand in sorted_industry_skills:

    print(
        f"{skill:<20}{demand}%"
    )


# ==========================================
# 9. FIND MATCHING SKILLS
# ==========================================

matching_skills = []


for skill in student_skills:

    if skill in industry_skills:

        matching_skills.append(
            skill
        )


# ==========================================
# 10. FIND SKILL GAPS
# ==========================================

missing_skills = []


for skill, demand in industry_skills.items():

    if skill not in student_skills:

        missing_skills.append({

            "skill": skill,

            "demand": demand

        })


# Sort missing skills
# from highest demand to lowest demand

missing_skills.sort(
    key=lambda x: x["demand"],
    reverse=True
)


# ==========================================
# 11. DISPLAY MATCHING SKILLS
# ==========================================

print("\n======================================")
print("          YOUR MATCHING SKILLS")
print("======================================")


if len(matching_skills) == 0:

    print(
        "No matching skills found."
    )

else:

    for skill in matching_skills:

        demand = industry_skills[
            skill
        ]


        print(
            f"✓ {skill:<20}"
            f"{demand}% industry demand"
        )


# ==========================================
# 12. DISPLAY SKILL GAP
# ==========================================

print("\n======================================")
print("             YOUR SKILL GAP")
print("======================================")


if len(missing_skills) == 0:

    print(
        "🎉 No major skill gaps found!"
    )

else:

    for item in missing_skills:

        print(
            f"❌ {item['skill']:<20}"
            f"{item['demand']}% industry demand"
        )


# ==========================================
# 13. TOP SKILLS TO LEARN
# ==========================================

print("\n======================================")
print("        TOP SKILLS TO LEARN")
print("======================================")


if len(missing_skills) == 0:

    print(
        "You already have the detected skills."
    )

else:

    top_skills = missing_skills[:5]


    for index, item in enumerate(
        top_skills,
        start=1
    ):

        print(
            f"{index}. "
            f"{item['skill']} "
            f"→ {item['demand']}% demand"
        )


# ==========================================
# 14. CALCULATE MARKET ALIGNMENT
# ==========================================

if len(industry_skills) > 0:

    matched_demand = 0

    total_demand = 0


    for skill, demand in industry_skills.items():

        total_demand += demand


        if skill in student_skills:

            matched_demand += demand


    market_alignment = (
        matched_demand /
        total_demand
    ) * 100

else:

    market_alignment = 0


# ==========================================
# 15. DISPLAY MARKET ALIGNMENT
# ==========================================

print("\n======================================")
print("       MARKET ALIGNMENT")
print("======================================")


print(
    f"{market_alignment:.1f}%"
)


print(
    "\nThis score represents how much of "
    "the observed skill demand you currently "
    "cover among the skills detected in "
    "the analyzed job listings."
)


# ==========================================
# 16. GENERATE LEARNING ROADMAP
# ==========================================

roadmap = generate_roadmap(
    missing_skills
)


display_roadmap(
    roadmap,
    max_skills=5
)
# ==========================================
# GENERATE LEARNING ORDER
# ==========================================

learning_order = create_learning_order(
    missing_skills,
    student_skills
)


display_learning_order(
    learning_order,
    max_skills=8
)
# ==========================================
# MARKET EVIDENCE
# ==========================================

market_evidence = build_market_evidence(
    industry_skills,
    skill_counts,
    total_jobs,
    student_skills
)


display_market_evidence(
    market_evidence,
    max_skills=10
)
# ==========================================
# INTELLIGENT SKILL PRIORITY
# ==========================================

from skill_dependencies import SKILL_DEPENDENCIES


priority_list = build_priority_list(
    industry_skills,
    student_skills,
    SKILL_DEPENDENCIES
)


display_priority_list(
    priority_list,
    max_skills=10
)


# ==========================================
# 17. CAREERGAP SUMMARY
# ==========================================

print("\n======================================")
print("          CAREERGAP SUMMARY")
print("======================================")


print(
    "\nTarget Role :",
    target_role
)

print(
    "Location    :",
    location
)

print(
    "Jobs Analyzed:",
    total_jobs
)

print(
    "Skills You Have:",
    len(student_skills)
)

print(
    "Skills Detected:",
    len(industry_skills)
)

print(
    "Skill Gaps:",
    len(missing_skills)
)

print(
    f"Market Alignment: "
    f"{market_alignment:.1f}%"
)


# ==========================================
# 18. ANALYSIS COMPLETE
# ==========================================

print("\n======================================")
print("        ANALYSIS COMPLETE")
print("======================================")