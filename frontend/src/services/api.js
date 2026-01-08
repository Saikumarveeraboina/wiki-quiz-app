const API_BASE = import.meta.env.VITE_API_BASE;


export const generateQuiz = async (url) => {
  const res = await fetch(`${API_BASE}/generate-quiz`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });

  return res.json();
};

export const getPastQuizzes = async () => {
  const res = await fetch(`${API_BASE}/past-quizzes`);
  return res.json();
};
