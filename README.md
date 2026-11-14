# CareerGapAI

**Find out exactly which skills stand between you and the job you want, using live job postings.**

CareerGapAI takes a target role, a location and your current skills. It pulls up to 30 live job listings from Google Jobs, works out which skills employers are actually asking for, and compares them with yours. It then tells you what you're missing, what to learn first, and in what order.

## What you get back

- **Market alignment score:** how much of the in-demand skill set you already cover, weighted by demand.
- **Skill demand:** the percentage of analyzed postings that mention each skill.
- **Skill gaps:** missing skills, sorted by how often employers ask for them.
- **Priority list:** each missing skill gets a score from market demand, plus a bonus for skills that unlock many others. Scores map to CRITICAL / VERY HIGH / HIGH / MEDIUM / LOW.
- **Learning order:** prerequisites come first. For example, Python is scheduled before machine learning, and machine learning before deep learning and PyTorch.
- **Roadmap:** learning topics for each missing skill.
- **Market evidence:** the job postings behind the analysis (title, company, location, link), so every recommendation can be traced to real listings.

## How it works

```
target role + location ──► SerpAPI (Google Jobs) ──► up to 30 postings
                                                          │
your skills ──► normalize aliases                         ▼
  ("sklearn" → scikit-learn,           detect skills in each description
   "k8s" → kubernetes, …)              (skill dictionary + word-boundary regex)
        │                                                 │
        └──────────────► compare ◄────── demand % per skill
                            │
     gaps ─► priority engine (demand + dependency bonus)
          ─► learning order (prerequisite graph)
          ─► roadmap + market evidence
```

| Module | Role |
|---|---|
| `backend/main.py` | FastAPI app with the `POST /analyze` endpoint |
| `backend/services/job_service.py` | Fetches and paginates Google Jobs results through SerpAPI |
| `backend/skill_dictionary.py` | Canonical skills and their aliases |
| `backend/skill_detector.py` | Detects skills in job text and normalizes user input |
| `backend/skill_dependencies.py` | Prerequisite graph and learning-order builder |
| `backend/priority_engine.py` | Priority scoring and labels |
| `backend/roadmap_generator.py` | Learning paths for each skill |
| `backend/market_evidence.py` | Builds the evidence summary from the analyzed jobs |

## Tech stack

Python · FastAPI · Pydantic · SerpAPI (Google Jobs engine) · python-dotenv · Uvicorn

## Run it locally

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env         # macOS/Linux: cp .env.example .env
# put your SerpAPI key in .env
uvicorn main:app --reload
```

The API runs at http://127.0.0.1:8000, with interactive docs at http://127.0.0.1:8000/docs. CORS is set up for an Angular frontend on `localhost:4200`.

### Example request

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"target_role": "Machine Learning Engineer", "location": "India", "skills": "python, sql, pandas"}'
```

The response contains `profile`, `market` (jobs analyzed, skill demand, alignment), the skill analysis, priority list, learning order, roadmap and job evidence.

## Status

In active development. Next: the frontend dashboard and broader skill coverage.

## Author

**Sunil Annes S K**, B.Tech Artificial Intelligence and Data Science, LICET, Chennai · [GitHub](https://github.com/SunilAnnes14) · [Kaggle](https://www.kaggle.com/sunilannessk)
