from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class IncomingCallsModel(BaseModel):
    caller_phone_number: str = Field(..., min_length=13, max_length=13, description="number of incoming caller")
    call_duration: str = Field(..., min_length=1, description="duration (in secs) of call")
    call_timestamp: str = Field(..., min_length=1, description="timestamp of call")
    caller_in_contact: str = Field(..., min_length=1, description="in/not in contacts (0/1) of caller")
    call_type: str = Field(..., min_length=1, description="incoming/outgoing (0/1) call")
    call_spam: str = Field(..., min_length=1, max_length=1, description="Type of Call Spam")
    user_auth_id: str = Field(..., min_length=5, max_length=50, description="UUID in DB") 