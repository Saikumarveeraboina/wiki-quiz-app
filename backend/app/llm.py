import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz_with_llm(text: str):
    """
    Generate quiz using Gemini LLM
    """

    # ✅ UPDATED MODEL NAME
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are given Wikipedia article content.

Generate exactly 5 multiple-choice questions strictly based on the content.

Each question must include:
- question
- 4 options
- correct answer
- difficulty (easy, medium, hard)
- short explanation

Return ONLY valid JSON in the following format:

{{
  "quiz": [
    {{
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "...",
      "difficulty": "easy",
      "explanation": "..."
    }}
  ],
  "related_topics": ["Topic1", "Topic2"]
}}

Article Content:
{text}
"""

    response = model.generate_content(prompt)

    # Convert response text to JSON
    return json.loads(response.text)
