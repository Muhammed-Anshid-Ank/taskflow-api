# prohject Architecture

taskflow-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── users.py
│       └── tasks.py
│
├── requirements.txt
└── README.md


# TaskFlow API

A minimal REST API built using FastAPI, SQLAlchemy, and PostgreSQL.

## Features
- User management
- Task creation and assignment
- Task status updates
- Clean REST architecture

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Python

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

Sample API Key: f49ffe091817532bafbf25bd98b906d6efe7cf2671ab135aac2886f01dcc8985
