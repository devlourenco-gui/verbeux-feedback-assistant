Feedback Assistant – Verbeux API Integration

✅ Visão Geral

Este projeto é um assistente de feedback de clientes desenvolvido em **Python com Flask**.  
Ele permite **coletar**, **classificar** e **armazenar** feedbacks de forma simples, além de disponibilizar uma **interface web** para visualização e análise.

---

🚀 Funcionalidades

- Envio de feedbacks (Elogio, Reclamação ou Neutro)  
- Classificação automática de mensagens por palavras-chave  
- Armazenamento dos feedbacks em SQLite  
- Exibição de todos os feedbacks via API (JSON)  
- Visualização dos feedbacks via página HTML + JavaScript  
- Filtros por categoria (Compliment / Complaint / Neutral)  
- Contadores de feedbacks por categoria (Analytics)  
- Configuração de CORS para integração com frontend  

---

📂 Estrutura do Projeto
```
backend/
├── static/
│   ├── css/
│   │   └── style.css          # Frontend styles
│   └── js/
│       └── script.js          # Frontend JavaScript (if needed)
├── templates/
│   └── index.html             # HTML template for feedback listing
├── classifier.py              # Feedback classification logic
├── database.py                # SQLAlchemy models and database setup
├── main.py                    # FastAPI app and routes
├── proxy.py                   # Proxy router for Verbeux FeedAI API
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)

```
.
├── backend/
│   ├── main.py              # API Flask com os endpoints
│   ├── classifier.py        # Lógica de classificação de feedbacks
│   ├── database.py          # Banco de dados SQLite e funções de acesso
│   └── feedback.db          # Banco de dados local (ignorado no Git)
├── frontend_files/          # Arquivos estáticos (CSS e JS)
│   ├── style.css
│   └── script.js
├── html_views/              # Template HTML (interface web)
│   └── index.html
├── tests/                   # Scripts de testes manuais
│   ├── test_feedback.py     # Teste de envio e listagem de feedbacks
│   └── test_request.py      # Teste de envio POST
├── requirements.txt         # Dependências Python
└── .gitignore               # Arquivos ignorados pelo Git

---

⚙️ Como Executar Localmente

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
2. Rodar o Backend (API Flask)
bash
Copiar
Editar
python main.py
O servidor Flask iniciará em:
http://localhost:5000

3. Acessar o Frontend
Abra o navegador e vá para:
http://localhost:5000/

A página web permitirá enviar feedbacks e visualizar os resultados.

🧑‍💻 Endpoints Disponíveis

Endpoint	Método	Função
/	GET	Exibe a página HTML
/feedback	POST	Envia um novo feedback
/feedbacks	GET	Lista todos os feedbacks
/feedbacks?category=compliment	GET	Filtra feedbacks por categoria

🧪 Testes Manuais

Execute os scripts de teste manualmente:

bash
Copiar
Editar
python test_feedback.py
python test_request.py
Eles enviam feedbacks de exemplo e listam as respostas da API.

🔑 Observações Importantes

✅ O projeto usa SQLite para simplificar o armazenamento local.
✅ A classificação é feita com base em palavras-chave simples.
✅ O frontend HTML e os arquivos estáticos são servidos diretamente via Flask.

✅ Conclusão:

✅ Conclusão:

Esta solução atende aos principais requisitos do desafio técnico da Verbeux, incluindo a criação de uma API funcional, um sistema de classificação automática de feedbacks, armazenamento em banco de dados e uma interface web simples para interação e análise.

A integração direta com a plataforma Verbeux (FeedAI / Generative API) ainda não foi implementada, mas o projeto foi desenvolvido de forma modular, facilitando a inclusão dessa funcionalidade futuramente.

O código foi escrito pensando em clareza, simplicidade e fácil manutenção, cumprindo o objetivo de criar um assistente de feedback funcional.
