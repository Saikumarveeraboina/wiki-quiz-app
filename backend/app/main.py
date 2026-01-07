from fastapi import FastAPI
from pydantic import BaseModel

from app.scraper import scrape_wikipedia
from app.llm import generate_quiz_with_llm

app = FastAPI(title="Wiki Quiz Generator API")


class WikiRequest(BaseModel):
    url: str


@app.get("/")
def root():
    return {"message": "Wiki Quiz Generator Backend Running"}


@app.post("/generate-quiz")
def generate_quiz_from_wiki(data: WikiRequest):
    article_data = scrape_wikipedia(data.url)

    llm_result = generate_quiz_with_llm(article_data["content"])

    return {
        "url": data.url,
        "title": article_data["title"],
        "summary": article_data["summary"],
        "quiz": llm_result["quiz"],
        "related_topics": llm_result["related_topics"]
    }
