from flask import Blueprint, request, jsonify
from db.crud import Database

bp = Blueprint("reviews", __name__)
db = Database()

POSITIVE_KEYWORDS = {"хорош", "люблю", "отлично", "нравит", "круто", "супер"}
NEGATIVE_KEYWORDS = {"плохо", "ненавиж", "ужас", "отстой", "не работает", "проблема"}


def detect_sentiment(text: str) -> str:
    lower_text = text.lower()
    if any(word in lower_text for word in POSITIVE_KEYWORDS):
        return "positive"
    elif any(word in lower_text for word in NEGATIVE_KEYWORDS):
        return "negative"
    return "neutral"


@bp.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    sentiment = detect_sentiment(text)
    review = db.add_review(text, sentiment)

    return jsonify(review.model_dump())


@bp.route("/reviews", methods=["GET"])
def get_reviews():
    sentiment = request.args.get("sentiment")
    reviews = db.get_reviews(sentiment)

    return jsonify([
        r.model_dump()
        for r in reviews
    ])
