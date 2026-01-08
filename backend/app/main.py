from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import WikiRequest

from app.scraper import scrape_wikipedia
from app.llm import generate_quiz_with_llm
from app.db import init_db
from app.crud import save_quiz, get_all_quizzes

app = FastAPI(title="Wiki Quiz Generator API")

# ✅ CORS (MANDATORY for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Run DB setup when server starts
@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "Wiki Quiz Generator Backend Running"}

@app.post("/generate-quiz")
def generate_quiz_from_wiki(data: WikiRequest):
    article_data = scrape_wikipedia(data.url)
    llm_result = generate_quiz_with_llm(article_data["content"])

    response = {
        "url": data.url,
        "title": article_data["title"],
        "summary": article_data["summary"],
        "quiz": llm_result["quiz"],
        "related_topics": llm_result["related_topics"]
    }

    save_quiz(response)
    return response

@app.get("/past-quizzes")
def past_quizzes():
    return get_all_quizzes()
