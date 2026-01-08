CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS quizzes (
    id SERIAL PRIMARY KEY,
    url TEXT UNIQUE,
    title TEXT,
    summary TEXT,
    quiz JSONB,
    related_topics JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
