from pydantic import BaseModel
class RequestChat(BaseModel):
    id: int
    message: str