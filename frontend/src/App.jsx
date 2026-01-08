import { useState } from "react";
import { generateQuiz, getPastQuizzes } from "./services/api";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [pastQuizzes, setPastQuizzes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);


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
      <h1 className="app-title">Wiki Quiz Generator</h1>
      <div className="card">
        <h2 className="heading">Generate Quiz</h2>
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
        <div>
          <h2 className="heading2">{quiz.title}</h2>
          <p>{quiz.summary}</p>

          {quiz.quiz.map((q) => (
            <div className="question-card" key={q.question}>
              <p className="para"><strong>{q.question}</strong></p>

              <div className="options">
                {q.options.map((opt, i) => (
                  <div key={i} className="option">
                    <strong>{String.fromCharCode(65 + i)}.</strong> {opt}
                  </div>
                ))}
              </div>

              <button className="btn" onClick={() => setShowAnswer(!showAnswer)}>
                {showAnswer ? "Hide Answer" : "Show Answer"}
              </button>

              {showAnswer && (
                <p className="para2">Answer: {q.answer}</p>
              )}

              <p className="para3"><b>Difficulty:</b> {q.difficulty}</p>
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
