import json
from app.db import get_db_connection


def save_quiz(data):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO quizzes (url, title, summary, quiz, related_topics)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT ON CONSTRAINT quizzes_url_unique
        DO NOTHING;
        """,
        (
            data["url"],
            data["title"],
            data["summary"],
            json.dumps(data["quiz"]),
            json.dumps(data["related_topics"]),
        )
    )

    conn.commit()
    cur.close()
    conn.close()


def get_all_quizzes():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, url, title, summary, quiz, related_topics, created_at
        FROM quizzes
        ORDER BY created_at DESC
        """
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    quizzes = []
    for row in rows:
        quizzes.append({
            "id": row[0],
            "url": row[1],
            "title": row[2],
            "summary": row[3],
            "quiz": row[4],
            "related_topics": row[5],
            "created_at": row[6],
        })

    return quizzes
