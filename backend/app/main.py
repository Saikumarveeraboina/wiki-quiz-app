from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import WikiRequest
from fastapi import HTTPException
import traceback

from app.scraper import scrape_wikipedia
from app.llm import generate_quiz_with_llm
from app.db import init_db
from app.crud import save_quiz, get_all_quizzes

app = FastAPI(title="Wiki Quiz Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://wiki-quiz-apps.vercel.app",
        "https://wiki-quiz-app.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "Wiki Quiz Generator Backend Running"}



@app.post("/generate-quiz")
def generate_quiz_from_wiki(data: WikiRequest):
    try:
        print("URL received:", data.url)

        article_data = scrape_wikipedia(data.url)
        print("Scraping done")

        llm_result = generate_quiz_with_llm(article_data["content"])
        print("LLM response received")

        response = {
            "url": data.url,
            "title": article_data["title"],
            "summary": article_data["summary"],
            "quiz": llm_result["quiz"],
            "related_topics": llm_result["related_topics"]
        }

        save_quiz(response)
        print("Saved to DB")

        return response

    except Exception as e:
        print("🔥 ERROR OCCURRED 🔥")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/past-quizzes")
def past_quizzes():
    return get_all_quizzes()
