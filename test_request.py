import requests

url = "http://localhost:5000/feedback"
data = {
    "message": "O atendimento foi ótimo e a equipe é excelente!"
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Resposta:", response.json())
