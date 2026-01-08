cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO quizzes (wiki_url, title, summary, quiz, related_topics)
    VALUES (%s, %s, %s, %s, %s)
    """,
    (
        url,
        title,
        summary,
        json.dumps(quiz),
        json.dumps(related_topics)
    )
)

conn.commit()
cursor.close()
