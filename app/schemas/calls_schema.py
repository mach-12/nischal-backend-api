from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class IncomingCallsModel(BaseModel):
    called_phone_number: str = Field(..., min_length=13, max_length=13, description="number of incoming caller")
    called_name: str = Field(..., min_length=1, description="number of incoming caller")
    user_auth_id: str = Field(..., min_length=5, max_length=50, description="UUID in DB") 