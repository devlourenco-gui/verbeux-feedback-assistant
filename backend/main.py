from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from classifier import classify_feedback
from database import save_feedback, get_all_feedbacks


app = Flask(__name__, static_folder="frontend_files", template_folder="html_views")
CORS(app)

@app.route("/")
def home():
    return render_template("inder.html")

@app.route("/feedback", methods=["POST"])
def receive_feedback():
    data = request.get_json()
    message = data.get("message", "")
    category = classify_feedback(message)
    save_feedback(message, category)
    return jsonify({"category": category}), 200

@app.route("/feedbacks", methods=["GET"])
def list_feedbacks():
    category = request.args.get("category")
    feedbacks = get_all_feedbacks(category)
    return jsonify(feedbacks), 200

if __name__ == "__main__":
    from database import init_db
    init_db()
    app.run(debug=True)


"""
caso precise apagar os feedbacks

if __name__ == "__main__":
    from database import init_db, delete_all_feedbacks
    init_db()
    delete_all_feedbacks
    app.run(debug=True)
"""
