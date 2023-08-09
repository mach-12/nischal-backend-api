from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class IncomingEmailsModel(BaseModel):
    email_head: str = Field(..., min_length=1, description="name of message sender")
    email_body: str = Field(...,min_length=1,description="content of the message sent")
    email_sender: str = Field(...,min_length=1,description="Email of the sender")
    email_user: str = Field(...,min_length=1,description="Email of the reciever")
    user_auth_id: str = Field(..., min_length=5, description="UUID in DB")