# FastAPI + Docker + PostgreSQL

Projeto simples para estudo de **Docker Compose** com **Python** e **PostgreSQL**, validando conexão entre containers.

## 🧱 Stack

* Python 3.11
* PostgreSQL 13
* Docker & Docker Compose

## 📁 Estrutura

```
.
├─ docker-compose.yaml
├─ .env
└─ python/
   ├─ Dockerfile
   ├─ requirements.txt
   └─ app/
      └─ app.py
```

## ▶️ Como rodar

```bash
docker compose up --build
```

## ⚙️ Variáveis de ambiente

Arquivo `.env` (não versionado):

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mydatabase
```

## 🧪 Teste

A aplicação Python tenta conectar no banco ao subir e exibe o status no log.

## 🔐 Segurança

* Não versione o `.env`
* Use `.gitignore`

---

Projeto para fins educacionais.
