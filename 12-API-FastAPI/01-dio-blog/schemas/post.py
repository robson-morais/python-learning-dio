from datetime import UTC, datetime
from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    author: str
    date: datetime = datetime.now(UTC)
    published: bool = False