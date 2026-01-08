import { useEffect, useState } from "react";
import "./index.css";
import { getPastQuizzes } from "../../services/api";

const History = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    getPastQuizzes().then(setHistory);
  }, []);

  return (
    <div className="history-container">
      <h2>Past Quizzes</h2>

      {history.map((item) => (
        <div className="history-item" key={item.id}>
          <h4>{item.title}</h4>
          <small>{item.url}</small>
        </div>
      ))}
    </div>
  );
};

export default History;
