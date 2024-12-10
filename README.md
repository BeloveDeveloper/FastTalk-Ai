# NeuroGram 🧠

This is my first pet project for python. I aimed to practice and apply the principles of clean architecture.

## Technologies Used

- **Frontend:** Svelte 5
- **Bot:** Aiogram + AiogramDialog
- **Backend:** Python (FastAPI, SqlAlchemy, Dishka)

## Installation and Setup

**1. Clone the repository:**
```bash
git clone https://github.com/DmitriySergeevic/NeuroGram.git
```
**2. Provide env variables:**
```bash
export BOT_TOKEN='Your telegram bot token'
export DB_URL='postgresql+asyncpg://postgres:postgres@localhost:5432/neurogram'
export JWT_SECRET='Some secret long string to work with JWT tokens'
```
**3. Install poetry:**
```bash
cd backend
poetry init
poetry install
```
**1. Clone the repository:**
```bash
uvicorn src.neurogram.main.web:app --reload
```