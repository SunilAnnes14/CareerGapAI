from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.job_service import JobService

from skill_detector import (
    detect_skills,
    normalize_student_skills
)

from skill_dependencies import (
    SKILL_DEPENDENCIES,
    create_learning_order
)

from priority_engine import (
    build_priority_list
)

from roadmap_generator import (
    generate_roadmap
)

from market_evidence import (
    build_market_evidence
)


# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="CareerGap AI API",
    description="AI-powered career skill gap analysis using live job market data",
    version="1.0.0"
)


# ==========================================
# CORS CONFIGURATION
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ==========================================
# REQUEST MODEL
# ==========================================

class CareerRequest(BaseModel):

    target_role: str

    location: str

    skills: str


# ==========================================
# HOME ENDPOINT
# ==========================================

@app.get("/")
def home():

    return {
        "message": "CareerGap AI API is running",
        "status": "success"
    }


# ==========================================
# CAREER ANALYSIS ENDPOINT
# ==========================================

@app.post("/analyze")
def analyze_career(request: CareerRequest):

    # ======================================
    # 1. NORMALIZE STUDENT SKILLS
    # ======================================

    student_skills = normalize_student_skills(
        request.skills
    )


    # ======================================
    # 2. SEARCH LIVE JOBS
    # ======================================

    job_service = JobService()

    jobs = job_service.search_jobs(
        request.target_role,
        request.location
    )


    # ======================================
    # 3. HANDLE NO JOBS
    # ======================================

    if len(jobs) == 0:

        return {
            "success": False,
            "message": (
                "No jobs found for this role "
                "and location."
            )
        }


    # ======================================
    # 4. DETECT SKILLS
    #    FROM JOB DESCRIPTIONS
    # ======================================

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


    # ======================================
    # 5. CALCULATE INDUSTRY SKILL DEMAND
    # ======================================

    industry_skills = {}

    total_jobs = len(jobs)


    for skill, count in skill_counts.items():

        demand = (
            count / total_jobs
        ) * 100


        industry_skills[skill] = round(
            demand
        )


    # ======================================
    # 6. FIND MATCHING SKILLS
    # ======================================

    matching_skills = []


    for skill in student_skills:

        if skill in industry_skills:

            matching_skills.append(
                skill
            )


    # ======================================
    # 7. FIND SKILL GAPS
    # ======================================

    missing_skills = []


    for skill, demand in industry_skills.items():

        if skill not in student_skills:

            missing_skills.append({

                "skill": skill,

                "demand": demand

            })


    missing_skills.sort(

        key=lambda x: x["demand"],

        reverse=True

    )


    # ======================================
    # 8. CALCULATE MARKET ALIGNMENT
    # ======================================

    matched_demand = 0

    total_demand = 0


    for skill, demand in industry_skills.items():

        total_demand += demand


        if skill in student_skills:

            matched_demand += demand


    if total_demand > 0:

        market_alignment = (

            matched_demand

            /

            total_demand

        ) * 100

    else:

        market_alignment = 0


    # ======================================
    # 9. INTELLIGENT PRIORITY
    # ======================================

    priority_list = build_priority_list(

        industry_skills,

        student_skills,

        SKILL_DEPENDENCIES

    )


    # ======================================
    # 10. PERSONALIZED ROADMAP
    # ======================================

    roadmap = generate_roadmap(

        missing_skills

    )


    # ======================================
    # 11. LEARNING ORDER
    # ======================================

    learning_order = create_learning_order(

        missing_skills,

        student_skills

    )


    # ======================================
    # 12. MARKET EVIDENCE
    # ======================================

    market_evidence = build_market_evidence(

        industry_skills,

        skill_counts,

        total_jobs,

        student_skills

    )


    # ======================================
    # 13. PREPARE LIVE JOB EVIDENCE
    # ======================================

    job_evidence = []


    for job in jobs:

        job_evidence.append({

            "title": job.get(
                "title",
                "Unknown Job"
            ),

            "company": job.get(
                "company_name",
                "Unknown Company"
            ),

            "location": job.get(
                "location",
                "Unknown Location"
            ),

            "via": job.get(
                "via",
                ""
            ),

            "description": job.get(
                "description",
                ""
            ),

            "link": job.get(
                "share_link",
                ""
            )

        })


    # ======================================
    # 14. RETURN COMPLETE RESULT
    # ======================================

    return {

        "success": True,


        # ==================================
        # STUDENT PROFILE
        # ==================================

        "profile": {

            "target_role":
                request.target_role,

            "location":
                request.location,

            "student_skills":
                student_skills

        },


        # ==================================
        # MARKET INFORMATION
        # ==================================

        "market": {

            "jobs_analyzed":
                total_jobs,

            "industry_skills":
                industry_skills,

            "market_alignment":
                round(
                    market_alignment,
                    1
                )

        },


        # ==================================
        # SKILL ANALYSIS
        # ==================================

        "skill_analysis": {

            "matching_skills":
                matching_skills,

            "missing_skills":
                missing_skills

        },


        # ==================================
        # PRIORITY
        # ==================================

        "priority":
            priority_list,


        # ==================================
        # ROADMAP
        # ==================================

        "roadmap":
            roadmap,


        # ==================================
        # LEARNING ORDER
        # ==================================

        "learning_order":
            learning_order,


        # ==================================
        # MARKET EVIDENCE
        # ==================================

        "market_evidence":
            market_evidence,


        # ==================================
        # LIVE JOB EVIDENCE
        # ==================================

        "jobs":
            job_evidence

    }