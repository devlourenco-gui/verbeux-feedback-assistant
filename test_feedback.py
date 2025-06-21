import requests

BASE_URL = "http://localhost:5000"

def send_feedback(message):
    response = requests.post(
        f"{BASE_URL}/feedback",
        json={"message":message}

    )
    print(f"Enviado: {message} => Categoria: {response.json().get('category')}")

def get_feedbacks(category=None):
    params = {"category": category} if category else {}
    response = requests.get(f"{BASE_URL}/feedbacks", params=params)
    feedbacks = response.json()
    print(f"\nFeedbacks{' da categoria ' + category if category else ''}")
    for f in feedbacks:
        print(f" [{f['category']}] {f['message']}")

if __name__ == "__main__":
    send_feedback("Eu odiei")
    send_feedback("Foi um maravilhoso")
    send_feedback("Não sei o que dizer")

    get_feedbacks()
