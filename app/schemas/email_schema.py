from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class IncomingEmailsModel(BaseModel):
    phone_number_of_messenger: str = Field(..., min_length=13, max_length=13, description="email of message sender")
    email_head: str = Field(..., min_length=1, description="name of message sender")
    email_body: str = Field(...,min_length=1,description="content of the message sent")
    user_auth_id: str = Field(..., min_length=5, description="UUID in DB")