def classify_feedback(text):
    compliments = ["bom", "ótimo", "exelente", "maravilhoso", "amei"]
    complaints = ["ruim", "péssimo", "reclamação", "horrivel", "odiei"]

    text_lower = text.lower()
    if any(word in text_lower for word in compliments):
        return "compliment"
    elif any(word in text_lower for word in complaints):
        return "complaint"
    else:
        return "neutral"