# FastTalk AI 🧠

This project aims to seamlessly integrate your language model into a user-friendly web platform and Telegram bot, providing users with an interactive and engaging experience. In this project, I am trying to use the principles of clean architecture to ensure the reliability, maintainability and scalability of the application

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
poetry install
```
**4. Start Uvicorn:**
```bash
uvicorn src.neurogram.main.web:app --reload
```
