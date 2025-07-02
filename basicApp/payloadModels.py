"""All payload models used in the FastAPI application are defiend here."""

from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    """Payload Model for create a post."""

    title: str | None = None
    content: str | None = None
    published: bool = True
    rating: Optional[float] = None
