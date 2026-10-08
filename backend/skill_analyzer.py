import os
import serpapi
from dotenv import load_dotenv

load_dotenv()

# Get API key
api_key = os.getenv("SERPAPI_KEY")

# Create SerpApi client
client = serpapi.Client(api_key=api_key)


# ------------------------------------------------
# STEP 1: Search for jobs
# ------------------------------------------------

results = client.search({
    "engine": "google_jobs",
    "q": "machine learning engineer",
    "location": "India"
})


# Get job results
jobs = results.get("jobs_results", [])

print("====================================")
print("        CAREERGAP AI")
print("====================================")

print("Jobs found:", len(jobs))


# ------------------------------------------------
# STEP 2: Skills we want to search for
# ------------------------------------------------

skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "git",
    "mongodb",
    "postgresql",
    "spark",
    "power bi",
    "tableau",
    "llm",
    "rag",
    "fastapi"
]


# ------------------------------------------------
# STEP 3: Count skill occurrences
# ------------------------------------------------

skill_counts = {}

for skill in skills:
    skill_counts[skill] = 0


for job in jobs:

    # Get job description
    description = job.get("description", "")

    # Convert description to lowercase
    description = description.lower()

    # Check every skill
    for skill in skills:

        if skill in description:
            skill_counts[skill] += 1


# ------------------------------------------------
# STEP 4: Display skill demand
# ------------------------------------------------

print("\n====================================")
print("       INDUSTRY SKILL DEMAND")
print("====================================")

total_jobs = len(jobs)

for skill, count in skill_counts.items():

    if count > 0:

        percentage = (count / total_jobs) * 100

        print(
            f"{skill:<20} "
            f"{count}/{total_jobs} jobs "
            f"({percentage:.0f}%)"
        )