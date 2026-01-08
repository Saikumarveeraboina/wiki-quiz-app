import { useState } from "react";
import { generateQuiz, getPastQuizzes } from "./services/api";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [pastQuizzes, setPastQuizzes] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    try {
      setLoading(true);
      const data = await generateQuiz(url);
      setQuiz(data);
    } catch {
      alert("Failed to generate quiz");
    } finally {
      setLoading(false);
    }
  };

  const handlePastQuizzes = async () => {
    const data = await getPastQuizzes();
    setPastQuizzes(data);
  };

  return (
    <div className="app">
      <h1>Wiki Quiz Generator</h1>

      {/* Generate Section */}
      <div className="card">
        <h2>Generate Quiz</h2>
        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Paste Wikipedia URL"
        />
        <button onClick={handleGenerate}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>
      </div>

      {/* Generated Quiz */}
      {quiz && (
        <div className="quiz-section">
          <h2>{quiz.title}</h2>
          <p className="summary">{quiz.summary}</p>

          {quiz.quiz.map((q) => (
            <div className="question-card" key={q.question}>
              <h3>{q.question}</h3>

              <ul>
                {q.options.map((opt) => (
                  <li key={opt}>{opt}</li>
                ))}
              </ul>

              <p className="answer">
                <strong>Answer:</strong> {q.answer}
              </p>

              <p className="difficulty">
                Difficulty: {q.difficulty}
              </p>
            </div>
          ))}
        </div>
      )}

      {/* Past Quizzes */}
      <button className="past-btn" onClick={handlePastQuizzes}>
        View Past Quizzes
      </button>

      {pastQuizzes.length > 0 && (
        <div className="card">
          <h2>Past Quizzes</h2>
          {pastQuizzes.map((q) => (
            <div key={q.id} className="past-item">
              <strong>{q.title}</strong>
              <p>{q.url}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
