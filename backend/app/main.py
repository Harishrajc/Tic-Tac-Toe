from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import (
    MoveRequest,
    DifficultyRequest
)

from app.game_logic import (
    make_move,
    reset_game,
    difficulty
)

app = FastAPI()

# allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Backend working"
    }

@app.post("/move")
def move(data: MoveRequest):

    return make_move(data.position)

@app.post("/reset")
def reset():

    return reset_game()

@app.post("/difficulty")
def set_difficulty(data: DifficultyRequest):

    import app.game_logic as game_logic

    game_logic.difficulty = data.difficulty

    return {
        "difficulty": game_logic.difficulty
    }