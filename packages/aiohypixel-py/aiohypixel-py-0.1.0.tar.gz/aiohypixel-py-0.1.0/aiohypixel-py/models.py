from pydantic import BaseModel


class Key(BaseModel):
    """Model representing a Hypixel API key."""

    key: str
    owner: str
    limit: int
    queries_in_past_minute: int
    total_queries: int
