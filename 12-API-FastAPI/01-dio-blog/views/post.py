from pydantic import BaseModel
from datetime import datetime, UTC

class PostOut(BaseModel):
    title: str
    author: str
    date: datetime
