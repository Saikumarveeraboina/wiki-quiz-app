import "./index.css";

const QuizModal = ({ quizData, onClose }) => {
  return (
    <div className="modal-overlay">
      <div className="modal">
        <h3>{quizData.title}</h3>
        <p>{quizData.summary}</p>

        <hr />

        {quizData.quiz.map((q, i) => (
          <div key={i}>
            <h4>{q.question}</h4>

            {q.options.map((opt, idx) => (
              <div className="option" key={idx}>
                {opt}
              </div>
            ))}

            <p className="answer">
              Correct Answer: {q.answer}
            </p>

            <p>
              <small>{q.explanation}</small>
            </p>

            <hr />
          </div>
        ))}

        <button className="close-btn" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};

export default QuizModal;
