# AI Chat App

## Overview

This is a full-fledged AI-powered chat application built using **React** for the frontend, **FastAPI** for the backend, and **PostgreSQL** as the database. The app supports real-time communication via **WebSockets** and integrates a lightweight **LLM (Language Model) from Hugging Face** for AI-generated responses. I will add more advanced LLM for better chat facility at later stages. The frontend uses **Bootstrap** for styling.

## Features

- **Real-time Chat** using WebSockets
- **AI-generated responses** using a local Hugging Face model
- **User Authentication** (JWT-based)
- **Persistent Chat History** (Stored in PostgreSQL)
- **Responsive UI** with Bootstrap
- **Docker Support** for easy deployment

## Tech Stack

### Frontend:

- React (with WebSockets)
- Bootstrap (for styling)

### Backend:

- FastAPI
- WebSockets for real-time communication
- PostgreSQL (via SQLAlchemy ORM)
- Hugging Face (DistilGPT2 or similar lightweight model)

## Project Structure

```
ai-chat-app/
│── backend/               # FastAPI Backend
│   ├── app/               # Main FastAPI application
│   │   ├── models.py      # Database models (if needed later)
│   │   ├── schemas.py     # Pydantic schemas for request/response validation
│   │   ├── auth.py        # API register routes
│   │   ├── wskt.py        # websocket
│   │   ├── main.py        # Entry point for FastAPI
│   │   ├── database.py    # database connection
│   ├── requirements.txt   # Python dependencies
│   ├── Dockerfile         # Deployment setup (optional)
│   ├── .env               # Environment variables (e.g., API keys)
│
│── frontend/              # React Frontend
│   ├── src/               # Source files
│   │   ├── components/    # Reusable UI components (ChatBox, Message, etc.)
│   │   ├── pages/         # Pages (ChatScreen, HomePage, etc.)
│   │   ├── services/      # API & WebSocket handling (API.js, WebSocket.js)
│   │   ├── App.jsx        # Main App component
│   │   ├── index.js       # Entry point
│   ├── public/            # Static files
│   ├── package.json       # Dependencies & scripts
│   ├── .env               # Environment variables (API URLs, WebSocket URL)
│
│── README.md              # Documentation
│── .gitignore             # Ignore unnecessary files
```

## Installation & Setup

### 1. Clone the repository

```sh
git clone https://github.com/lunatic-bot/AIChatApp-React-FastAPI.git
cd AIChatApp-React-FastAPI
```

### 2. Backend Setup (FastAPI & PostgreSQL)

```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup (React & Bootstrap)

```sh
cd frontend
npm install
npm start
```

### 4. Running with Docker (Optional)

```sh
docker-compose up --build
```

## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Login and get JWT token

### Chat

- `GET /messages` - Fetch chat history
- `WS /chat/{room_id}` - WebSocket connection for real-time chat

## Contributing

Feel free to submit issues or pull requests to improve the app!
