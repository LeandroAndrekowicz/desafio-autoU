# 📧 Classificador de Emails (FastAPI + OpenAI + Gemini)

Este projeto é uma aplicação web simples que classifica emails usando **FastAPI** no backend e os modelos da **OpenAI/Gemini** como IA.  
Ele também serve um frontend básico (HTML/CSS/JS) para testar a API.

---

## 🚀 Funcionalidades
- Envio de arquivo `.txt` ou `.pdf` **ou** colagem de texto direto no campo.
- Classificação do email em categorias.
- Sugestão de resposta automática.
- Interface simples e responsiva.

---

## 🛠️ Tecnologias utilizadas
- **FastAPI** (backend)
- **Uvicorn** (servidor ASGI)
- **OpenAI API** e **Google Generative AI**
- **HTML, CSS e JavaScript** (frontend)

---

## 📂 Estrutura do projeto

├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── use_cases/
│   └── utils/
├── email-examples/
│   ├── email-improdutivo.txt
│   └── email-produtivo.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .env
├── .env.example
├── .gitignore
└── readme.md

---

## ⚙️ Como rodar localmente

### 1. Clonar o repositório

```bash
    git clone https://github.com/leandroAndrekowicz/desafio-autoU
    cd desafio-autoU
```

### 2. Criar e ativar ambiente virtual

```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
    pip install -r backend/requirements.txt
```

### 4. Criar arquivo .env

Na raiz do projeto, crie um arquivo .env com suas chaves de API:

```bash
    OPENAI_API_KEY=sua_chave_aqui
    GOOGLE_API_KEY=sua_chave_aqui
    BASE_URL='url base para o frontend e backend'
```

### 5. Rodar o servidor
```bash
    uvicorn backend.main:app --reload
```

O servidor ficará disponível em:

- 👉 http://127.0.0.1:8000

Abra essa URL no navegador para usar o frontend.