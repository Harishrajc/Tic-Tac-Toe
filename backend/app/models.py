from pydantic import BaseModel

class MoveRequest(BaseModel):
    position: int

class DifficultyRequest(BaseModel):
    difficulty: str