# ==========================================
# CAREERGAP AI
# MARKET EVIDENCE ENGINE
# ==========================================


# ==========================================
# BUILD MARKET EVIDENCE
# ==========================================

def build_market_evidence(
    industry_skills,
    skill_counts,
    total_jobs,
    student_skills
):

    evidence = []


    # ======================================
    # PROCESS EVERY DETECTED SKILL
    # ======================================

    for skill, demand in industry_skills.items():

        jobs_with_skill = skill_counts.get(
            skill,
            0
        )


        # ==================================
        # CHECK STUDENT SKILL
        # ==================================

        if skill in student_skills:

            status = "✓ You have this skill"

        else:

            status = "❌ Skill gap"


        # ==================================
        # DETERMINE PRIORITY
        # ==================================

        if demand >= 70:

            priority = "VERY HIGH"

        elif demand >= 40:

            priority = "HIGH"

        elif demand >= 20:

            priority = "MEDIUM"

        else:

            priority = "LOW"


        # ==================================
        # BUILD EVIDENCE OBJECT
        # ==================================

        evidence_item = {

            "skill": skill,

            "demand": demand,

            "jobs_with_skill":
                jobs_with_skill,

            "total_jobs":
                total_jobs,

            "status":
                status,

            "priority":
                priority
        }


        evidence.append(
            evidence_item
        )


    # ======================================
    # SORT BY MARKET DEMAND
    # ======================================

    evidence.sort(
        key=lambda x: x["demand"],
        reverse=True
    )


    return evidence


# ==========================================
# DISPLAY MARKET EVIDENCE
# ==========================================

def display_market_evidence(
    evidence,
    max_skills=10
):

    print("\n======================================")

    print(
        "          MARKET EVIDENCE"
    )

    print("======================================")


    if len(evidence) == 0:

        print(
            "\nNo market evidence available."
        )

        return


    # ======================================
    # LIMIT DISPLAY
    # ======================================

    evidence = evidence[
        :max_skills
    ]


    # ======================================
    # DISPLAY EACH SKILL
    # ======================================

    for index, item in enumerate(
        evidence,
        start=1
    ):

        print(
            f"\n{index}. "
            f"{item['skill'].upper()}"
        )


        print(
            f"   Market Demand: "
            f"{item['demand']}%"
        )


        print(
            f"   Found in: "
            f"{item['jobs_with_skill']} / "
            f"{item['total_jobs']} jobs"
        )


        print(
            f"   Status: "
            f"{item['status']}"
        )


        print(
            f"   Priority: "
            f"{item['priority']}"
        )


        print(
            "\n--------------------------------------"
        )