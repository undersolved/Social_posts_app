from pydantic import BaseModel  #noq


class PostCreate(BaseModel):
    title: str
    content: str

