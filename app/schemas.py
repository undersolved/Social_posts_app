from pydantic import BaseModel  # noq


class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    title: str
    content: str
