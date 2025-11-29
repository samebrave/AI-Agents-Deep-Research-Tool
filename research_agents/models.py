from pydantic import BaseModel

class SearchResults(BaseModel):
    title: str
    url: str
    summary: str