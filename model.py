from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    nickname: str
    content: str
    time: str