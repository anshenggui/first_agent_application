from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    thread_id: str
    message: str
    image_url: Optional[str] = None

