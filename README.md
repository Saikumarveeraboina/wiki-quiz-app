🧠 Wiki Quiz Generator
A full-stack web application that generates quiz questions automatically from a given Wikipedia article URL using an LLM.
The application allows users to generate quizzes, view answers interactively, and see previously generated quizzes.

📌 Project Objective
To build a system that:
Accepts a Wikipedia article URL
Extracts content from the article
Uses a Large Language Model (LLM) to generate quiz questions
Stores generated quizzes in a database
Displays quizzes in a user-friendly frontend

🛠️ Tech Stack
Backend
Python
FastAPI
PostgreSQL
psycopg2
BeautifulSoup (for scraping)
Groq LLM
Uvicorn

Frontend
React (Vite)
JavaScript
CSS
Fetch API

Deployment
Backend: Render
Frontend: Vercel

⚙️ Backend Setup (Local)
1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Environment Variables (.env)
DB_HOST=localhost
DB_NAME=wiki_quiz_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
GROQ_API_KEY=your_groq_api_key

4️⃣ Run Backend
uvicorn app.main:app --reload


Backend will run at:
http://127.0.0.1:8000

🌐 API Endpoints
Method	Endpoint	Description
GET	/	Health check
POST	/generate-quiz	Generate quiz from Wikipedia URL
GET	/past-quizzes	Fetch stored quizzes
🎨 Frontend Setup (Local)
1️⃣ Install Dependencies
npm install

2️⃣ Environment Variable (.env)
VITE_API_BASE=http://127.0.0.1:8000

3️⃣ Run Frontend
npm run dev


Frontend will run at:
http://localhost:5173

🖥️ Application Features
Generate quiz from any Wikipedia article
Display multiple-choice questions (A, B, C, D)

Show/Hide answers on button click
View difficulty level for each question
View previously generated quizzes
Clean and simple UI

☁️ Deployment Details
Backend (Render)
Web Service using FastAPI
PostgreSQL database created on Render
Environment variables added in Render dashboard

Start command:
uvicorn app.main:app --host 0.0.0.0 --port 10000

Frontend (Vercel)
Framework: Vite + React

Environment variable added:
VITE_API_BASE=https://<render-backend-url>

🚀 Live URLs
Backend: https://wiki-quiz-app-cw3q.onrender.com
Frontend: https://wiki-quiz-apps.vercel.app

✅ Assignment Notes
Focused on functionality rather than over-engineering
Clean code structure
Beginner-friendly implementation
Meets all problem statement requirements
