# Tic-Tac-Toe

## Project Overview

This repository contains a Tic-Tac-Toe application with a Svelte frontend and a FastAPI backend.

- `frontend/` contains the Svelte UI and frontend build setup.
- `backend/` contains the Python FastAPI server, game logic, and API endpoints.

The frontend sends requests to the backend to make moves, reset the board, and change difficulty.

## Requirements

- Python 3.10+ for the backend
- Node.js 18+ and npm for the frontend
- Git (optional, for cloning the repo)

## Backend Setup

1. Open a terminal and change to the backend folder:

   ```bash
   cd backend
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend server:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

The backend will run at `http://localhost:8000`.

## Frontend Setup

1. Open a second terminal and change to the frontend folder:

   ```bash
   cd frontend
   ```

2. Install the Node dependencies:

   ```bash
   npm install
   ```

3. Start the frontend development server:

   ```bash
   npm run dev
   ```

Open the browser at the address shown in the terminal, usually `http://localhost:5173`.

## Usage

- Start the backend first, then start the frontend.
- Use the game board in the browser to play Tic-Tac-Toe.
- The backend handles moves, game state, resetting the board, and difficulty updates.

## Dependency Files

- Backend dependencies: `backend/requirements.txt`
- Frontend dependencies: `frontend/package.json`

## Notes

- If the frontend cannot connect to the backend, verify that the backend is running on port `8000`.
- The backend allows all CORS origins so the frontend can connect from the development server.
