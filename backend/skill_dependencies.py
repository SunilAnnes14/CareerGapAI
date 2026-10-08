# ==========================================
# CAREERGAP AI
# INTELLIGENT SKILL DEPENDENCY ENGINE
# ==========================================


# ==========================================
# SKILL DEPENDENCIES
# ==========================================

SKILL_DEPENDENCIES = {

    "machine learning": [
        "python"
    ],

    "deep learning": [
        "python",
        "machine learning"
    ],

    "pytorch": [
        "python",
        "deep learning"
    ],

    "tensorflow": [
        "python",
        "deep learning"
    ],

    "llm": [
        "python",
        "deep learning"
    ],

    "rag": [
        "python",
        "llm"
    ],

    "sql": [],

    "pandas": [
        "python"
    ],

    "numpy": [
        "python"
    ],

    "fastapi": [
        "python"
    ],

    "mongodb": [],

    "postgresql": [
        "sql"
    ],

    "spark": [
        "python",
        "sql"
    ],

    "docker": [
        "git"
    ],

    "kubernetes": [
        "docker"
    ],

    "aws": [
        "docker"
    ],

    "azure": [
        "docker"
    ],

    "git": []
}


# ==========================================
# GET DIRECT DEPENDENCIES
# ==========================================

def get_dependencies(skill):

    return SKILL_DEPENDENCIES.get(
        skill,
        []
    )


# ==========================================
# FIND ALL MISSING PREREQUISITES
# ==========================================

def find_all_prerequisites(
    skill,
    student_skills
):

    prerequisites = []

    visited = set()


    def explore(current_skill):

        if current_skill in visited:

            return

        visited.add(
            current_skill
        )


        dependencies = get_dependencies(
            current_skill
        )


        for dependency in dependencies:

            # Student already knows this skill

            if dependency in student_skills:

                continue


            # Add missing prerequisite

            if dependency not in prerequisites:

                prerequisites.append(
                    dependency
                )


            # Recursively find prerequisites

            explore(
                dependency
            )


    explore(skill)

    return prerequisites


# ==========================================
# BUILD LEARNING ORDER
# ==========================================

def create_learning_order(
    missing_skills,
    student_skills
):

    # --------------------------------------
    # Store market demand
    # --------------------------------------

    demand_map = {}


    for item in missing_skills:

        demand_map[
            item["skill"]
        ] = item["demand"]


    # --------------------------------------
    # Collect all required skills
    # --------------------------------------

    all_required_skills = []


    for item in missing_skills:

        skill = item["skill"]


        # Find all prerequisites

        prerequisites = find_all_prerequisites(
            skill,
            student_skills
        )


        # Add prerequisites

        for prerequisite in prerequisites:

            if prerequisite not in all_required_skills:

                all_required_skills.append(
                    prerequisite
                )


        # Add target skill

        if skill not in all_required_skills:

            all_required_skills.append(
                skill
            )


    # --------------------------------------
    # Create learning order
    # --------------------------------------

    learning_order = []


    # Skills the student already knows

    completed = set(
        student_skills
    )


    # --------------------------------------
    # Repeatedly find skills whose
    # prerequisites are completed
    # --------------------------------------

    while len(all_required_skills) > 0:

        progress = False


        for skill in all_required_skills:

            # Skip skills already completed

            if skill in completed:

                continue


            dependencies = get_dependencies(
                skill
            )


            # ----------------------------------
            # Check whether all prerequisites
            # are already completed
            # ----------------------------------

            ready = True


            for dependency in dependencies:

                if dependency not in completed:

                    ready = False

                    break


            if ready:

                # ==================================
                # ONLY SHOW PREREQUISITES THAT THE
                # STUDENT DOES NOT ALREADY HAVE
                # ==================================

                missing_dependencies = []


                for dependency in dependencies:

                    if dependency not in student_skills:

                        missing_dependencies.append(
                            dependency
                        )


                # ==================================
                # ADD SKILL TO LEARNING ORDER
                # ==================================

                learning_order.append({

                    "skill": skill,

                    "demand":
                        demand_map.get(
                            skill,
                            0
                        ),

                    "dependencies":
                        missing_dependencies

                })


                # Mark skill as completed

                completed.add(
                    skill
                )


                progress = True


        # ----------------------------------
        # Safety check
        # ----------------------------------

        # Prevent infinite loop if there is
        # a circular dependency.

        if not progress:

            break


    return learning_order


# ==========================================
# DISPLAY LEARNING ORDER
# ==========================================

def display_learning_order(
    learning_order,
    max_skills=10
):

    print("\n======================================")

    print(
        "       RECOMMENDED LEARNING ORDER"
    )

    print("======================================")


    # --------------------------------------
    # Check if roadmap exists
    # --------------------------------------

    if len(learning_order) == 0:

        print(
            "\nNo learning order available."
        )

        return


    # --------------------------------------
    # Limit number of displayed skills
    # --------------------------------------

    learning_order = learning_order[
        :max_skills
    ]


    # --------------------------------------
    # Display every step
    # --------------------------------------

    for index, item in enumerate(
        learning_order,
        start=1
    ):

        print(
            f"\nSTEP {index}"
        )


        print(
            item["skill"].upper()
        )


        print(
            f"Market Demand: "
            f"{item['demand']}%"
        )


        dependencies = item[
            "dependencies"
        ]


        # ----------------------------------
        # Display prerequisites
        # ----------------------------------

        if len(dependencies) == 0:

            print(
                "Prerequisites: "
                "Ready to learn"
            )

        else:

            print(
                "Learn after: "
                + ", ".join(
                    dependencies
                )
            )


        print(
            "\n--------------------------------------"
        )