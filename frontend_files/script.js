const API_URL = "http://localhost:5000";

function sendFeedback() {
  const message = document.getElementById("feedbackInput").value.trim();
  if (!message) return alert("Digite um feedback!");

  fetch(`${API_URL}/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert(`Feedback classificado como: ${data.category}`);
      document.getElementById("feedbackInput").value = "";
      loadFeedbacks();
    })
    .catch((err) => console.error(err));
}

function loadFeedbacks() {
  const category = document.getElementById("categoryFilter").value;
  const url = category
    ? `${API_URL}/feedbacks?category=${category}`
    : `${API_URL}/feedbacks`;

  fetch(url)
    .then((res) => res.json())
    .then((feedbacks) => {
      const list = document.getElementById("feedbackList");
      list.innerHTML = "";
      feedbacks.forEach((f) => {
        const li = document.createElement("li");
        li.textContent = `[${f.category}] ${f.message}`;
        list.appendChild(li);
      });
    });
}



function updateAnalytics() {
  const categories = ["compliment", "complaint", "neutral"];
  let total = 0;

  categories.forEach((cat) => {
    fetch(`${API_URL}/feedbacks?category=${cat}`)
      .then((res) => res.json())
      .then((data) => {
        document.getElementById(`count-${cat}`).textContent = data.length;
        total += data.length;
        document.getElementById("count-total").textContent = total;
      })
      .catch((err) => console.error(`Erro ao buscar ${cat}:`, err));
  });
}

window.onload = () => {
  loadFeedbacks();
  updateAnalytics();
};
