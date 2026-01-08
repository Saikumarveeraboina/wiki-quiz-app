import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()


def extract_json(text: str):
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found in LLM response")
    return json.loads(match.group())


def generate_quiz_with_llm(text: str):
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant"

    )

    prompt = f"""
Generate exactly 5 multiple-choice questions from the following Wikipedia content.

Rules:
- Use ONLY the given content
- 4 options per question
- Include correct answer
- Include difficulty (easy, medium, hard)
- Include short explanation
- Return ONLY JSON (no text, no markdown)

JSON format:
{{
  "quiz": [
    {{
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "...",
      "difficulty": "easy|medium|hard",
      "explanation": "..."
    }}
  ],
  "related_topics": ["Topic1", "Topic2"]
}}

Content:
{text}
"""

    response = llm.invoke([HumanMessage(content=prompt)])


    return extract_json(response.content)
