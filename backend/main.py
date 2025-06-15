from flask import Flask, request, jsonify
from classifier import classify_feedback
from database import save_feedback, get_all_feedbacks, init_db

init_db()

app = Flask(__name__)

@app.route("/feedback", methods=["POST"])
def receive_feedback():
    data = request.get_json()
    message = data.get("message", "")
    category = classify_feedback(message)
    save_feedback(message, category)
    return jsonify({"category": category}), 200

@app.route("/feedbacks", methods=["GET"])
def list_feedbacs():
    feedbacks = get_all_feedbacks()
    return jsonify(feedbacks), 200

if __name__ == "__main__":
    app.run(debug=True)

