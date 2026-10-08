import os
import serpapi
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

client = serpapi.Client(api_key=api_key)

results = client.search({
    "engine": "google_jobs",
    "q": "machine learning engineer",
    "location": "India"
})

jobs = results.get("jobs_results", [])

print("Number of jobs found:", len(jobs))

for job in jobs:
    print("--------------------------------")
    print("Job:", job.get("title"))
    print("Company:", job.get("company_name"))
    print("Location:", job.get("location"))