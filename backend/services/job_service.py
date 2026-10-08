import os
import serpapi
from dotenv import load_dotenv


load_dotenv()


class JobService:

    def __init__(self):

        api_key = os.getenv("SERPAPI_KEY")

        self.client = serpapi.Client(
            api_key=api_key
        )


    def search_jobs(
        self,
        role,
        location,
        max_jobs=30
    ):

        all_jobs = []

        next_page_token = None


        while len(all_jobs) < max_jobs:

            # ------------------------------
            # First page
            # ------------------------------

            search_params = {
                "engine": "google_jobs",
                "q": role,
                "location": location
            }


            # ------------------------------
            # Next pages
            # ------------------------------

            if next_page_token:

                search_params[
                    "next_page_token"
                ] = next_page_token


            # ------------------------------
            # Search SerpApi
            # ------------------------------

            results = self.client.search(
                search_params
            )


            # ------------------------------
            # Get jobs
            # ------------------------------

            jobs = results.get(
                "jobs_results",
                []
            )


            # Stop if no jobs returned

            if not jobs:

                break


            # ------------------------------
            # Add jobs
            # ------------------------------

            all_jobs.extend(jobs)


            # ------------------------------
            # Get next page token
            # ------------------------------

            pagination = results.get(
                "serpapi_pagination",
                {}
            )


            next_page_token = pagination.get(
                "next_page_token"
            )


            # ------------------------------
            # No more pages
            # ------------------------------

            if not next_page_token:

                break


        # ----------------------------------
        # Limit result to requested amount
        # ----------------------------------

        return all_jobs[:max_jobs]