# ==========================================
# CAREERGAP AI
# INTELLIGENT PRIORITY ENGINE
# ==========================================


# ==========================================
# CALCULATE PRIORITY SCORE
# ==========================================

def calculate_priority_score(
    skill,
    demand,
    student_skills,
    skill_dependencies
):

    # --------------------------------------
    # Student already has this skill
    # --------------------------------------

    if skill in student_skills:

        return 0


    # --------------------------------------
    # Base score from market demand
    # --------------------------------------

    score = demand


    # --------------------------------------
    # Missing skill bonus
    # --------------------------------------

    # The student does not have the skill,
    # so it is an actual learning gap.

    score += 20


    # --------------------------------------
    # Dependency bonus
    # --------------------------------------

    # Count how many other skills depend
    # on this skill.

    dependent_count = 0


    for other_skill, dependencies in (
        skill_dependencies.items()
    ):

        if skill in dependencies:

            dependent_count += 1


    # Give additional priority to skills
    # that unlock many other skills.

    dependency_bonus = (
        dependent_count * 5
    )


    # Limit dependency bonus

    if dependency_bonus > 20:

        dependency_bonus = 20


    score += dependency_bonus


    return score


# ==========================================
# PRIORITY LABEL
# ==========================================

def get_priority_label(score):

    if score >= 100:

        return "CRITICAL"

    elif score >= 70:

        return "VERY HIGH"

    elif score >= 50:

        return "HIGH"

    elif score >= 30:

        return "MEDIUM"

    else:

        return "LOW"


# ==========================================
# BUILD PRIORITY LIST
# ==========================================

def build_priority_list(
    industry_skills,
    student_skills,
    skill_dependencies
):

    priority_list = []


    for skill, demand in industry_skills.items():

        score = calculate_priority_score(
            skill,
            demand,
            student_skills,
            skill_dependencies
        )


        # ----------------------------------
        # Ignore skills student already has
        # ----------------------------------

        if score == 0:

            continue


        priority = get_priority_label(
            score
        )


        priority_list.append({

            "skill": skill,

            "demand": demand,

            "score": round(score, 1),

            "priority": priority
        })


    # --------------------------------------
    # Sort highest priority first
    # --------------------------------------

    priority_list.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return priority_list


# ==========================================
# DISPLAY PRIORITY LIST
# ==========================================

def display_priority_list(
    priority_list,
    max_skills=10
):

    print("\n======================================")

    print(
        "       INTELLIGENT SKILL PRIORITY"
    )

    print("======================================")


    if len(priority_list) == 0:

        print(
            "\nNo skill gaps detected."
        )

        return


    priority_list = priority_list[
        :max_skills
    ]


    for index, item in enumerate(
        priority_list,
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
            f"   Priority Score: "
            f"{item['score']}"
        )


        print(
            f"   Priority: "
            f"{item['priority']}"
        )


        print(
            "\n--------------------------------------"
        )