# ==========================================
# CAREERGAP AI
# PERSONALIZED LEARNING ROADMAP
# ==========================================


# ==========================================
# LEARNING CONTENT
# ==========================================

LEARNING_PATHS = {

    "machine learning": {

        "priority": "VERY HIGH",

        "topics": [
            "Supervised learning",
            "Unsupervised learning",
            "Regression",
            "Classification",
            "Decision Trees",
            "Random Forest",
            "Model evaluation",
            "Cross validation"
        ]
    },


    "deep learning": {

        "priority": "HIGH",

        "topics": [
            "Neural networks",
            "Activation functions",
            "Backpropagation",
            "Gradient descent",
            "CNN",
            "RNN",
            "Model training",
            "Regularization"
        ]
    },


    "llm": {

        "priority": "HIGH",

        "topics": [
            "Transformer architecture",
            "Large Language Models",
            "Prompt engineering",
            "Embeddings",
            "LLM APIs",
            "Fine tuning basics",
            "RAG"
        ]
    },


    "sql": {

        "priority": "HIGH",

        "topics": [
            "SELECT queries",
            "WHERE conditions",
            "GROUP BY",
            "ORDER BY",
            "JOIN",
            "Subqueries",
            "Aggregate functions",
            "Database design"
        ]
    },


    "aws": {

        "priority": "MEDIUM",

        "topics": [
            "AWS fundamentals",
            "EC2",
            "S3",
            "IAM",
            "Lambda",
            "Cloud deployment",
            "AWS networking basics"
        ]
    },


    "azure": {

        "priority": "MEDIUM",

        "topics": [
            "Azure fundamentals",
            "Azure Virtual Machines",
            "Azure Storage",
            "Azure Functions",
            "Azure AI services",
            "Cloud deployment"
        ]
    },


    "tensorflow": {

        "priority": "MEDIUM",

        "topics": [
            "TensorFlow basics",
            "Keras",
            "Neural networks",
            "Model creation",
            "Model training",
            "Model evaluation",
            "Model deployment"
        ]
    },


    "pytorch": {

        "priority": "MEDIUM",

        "topics": [
            "PyTorch tensors",
            "Datasets",
            "DataLoaders",
            "Neural networks",
            "Training loops",
            "Loss functions",
            "Optimizers",
            "Model evaluation"
        ]
    },


    "kubernetes": {

        "priority": "MEDIUM",

        "topics": [
            "Containers",
            "Pods",
            "Deployments",
            "Services",
            "ConfigMaps",
            "Secrets",
            "Scaling",
            "Kubernetes networking"
        ]
    },


    "rag": {

        "priority": "MEDIUM",

        "topics": [
            "RAG architecture",
            "Document processing",
            "Chunking",
            "Embeddings",
            "Vector databases",
            "Retrieval",
            "Prompt construction",
            "RAG evaluation"
        ]
    },


    "docker": {

        "priority": "MEDIUM",

        "topics": [
            "Docker basics",
            "Images",
            "Containers",
            "Dockerfile",
            "Docker Compose",
            "Volumes",
            "Networking",
            "Container deployment"
        ]
    },


    "git": {

        "priority": "LOW",

        "topics": [
            "Git basics",
            "Repositories",
            "Commit",
            "Branching",
            "Merging",
            "Pull requests",
            "GitHub workflows"
        ]
    },


    "spark": {

        "priority": "MEDIUM",

        "topics": [
            "Apache Spark basics",
            "RDD",
            "DataFrames",
            "Spark SQL",
            "Transformations",
            "Actions",
            "PySpark"
        ]
    },


    "pandas": {

        "priority": "LOW",

        "topics": [
            "Series",
            "DataFrames",
            "Data cleaning",
            "Filtering",
            "Grouping",
            "Merging",
            "Data analysis"
        ]
    },


    "numpy": {

        "priority": "LOW",

        "topics": [
            "Arrays",
            "Indexing",
            "Slicing",
            "Vectorization",
            "Mathematical operations",
            "Linear algebra"
        ]
    },


    "mongodb": {

        "priority": "LOW",

        "topics": [
            "MongoDB basics",
            "Collections",
            "Documents",
            "CRUD operations",
            "Queries",
            "Indexes",
            "Aggregation"
        ]
    },


    "fastapi": {

        "priority": "MEDIUM",

        "topics": [
            "FastAPI basics",
            "API routes",
            "GET and POST",
            "Request validation",
            "Pydantic",
            "REST APIs",
            "API deployment"
        ]
    },


    "postgresql": {

        "priority": "LOW",

        "topics": [
            "PostgreSQL basics",
            "Tables",
            "SQL queries",
            "Relationships",
            "Indexes",
            "Transactions"
        ]
    }
}


# ==========================================
# GENERATE ROADMAP
# ==========================================

def generate_roadmap(missing_skills):

    roadmap = []


    for item in missing_skills:

        skill = item["skill"]

        demand = item["demand"]


        # Check whether we have
        # learning content for this skill

        if skill in LEARNING_PATHS:

            learning_path = LEARNING_PATHS[
                skill
            ]


            roadmap_item = {

                "skill": skill,

                "demand": demand,

                "priority": learning_path[
                    "priority"
                ],

                "topics": learning_path[
                    "topics"
                ]
            }


            roadmap.append(
                roadmap_item
            )


    return roadmap


# ==========================================
# DISPLAY ROADMAP
# ==========================================

def display_roadmap(
    roadmap,
    max_skills=5
):

    print("\n======================================")

    print(
        "     PERSONALIZED LEARNING ROADMAP"
    )

    print("======================================")


    if len(roadmap) == 0:

        print(
            "\nNo learning roadmap available."
        )

        return


    roadmap = roadmap[:max_skills]


    for index, item in enumerate(
        roadmap,
        start=1
    ):

        print(
            f"\n{index}. "
            f"{item['skill'].upper()}"
        )

        print(
            f"   Priority: "
            f"{item['priority']}"
        )

        print(
            f"   Market Demand: "
            f"{item['demand']}%"
        )


        print(
            "\n   Learn:"
        )


        for topic in item["topics"]:

            print(
                f"   • {topic}"
            )


        print(
            "\n--------------------------------------"
        )