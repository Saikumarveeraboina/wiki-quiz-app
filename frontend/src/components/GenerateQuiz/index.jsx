import { useState } from "react";
import "./index.css";
import { generateQuiz } from "../../services/api";

const GenerateQuiz = ({ setQuizData }) => {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!url) return alert("Enter Wikipedia URL");

    setLoading(true);
    try {
      const data = await generateQuiz(url);
      setQuizData(data);
    } catch (err) {
      alert("Failed to generate quiz");
    }
    setLoading(false);
  };

  return (
    <div className="generate-container">
      <h2>Generate Quiz</h2>

      <input
        type="text"
        placeholder="Paste Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button onClick={handleGenerate}>
        {loading ? "Generating..." : "Generate Quiz"}
      </button>
    </div>
  );
};

export default GenerateQuiz;
