from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class RegisterCompanyModel(BaseModel):
    verification_document: str = Field(..., min_length=13, max_length=13, description="document that verifies authenticity of the company")
    company_name: str = Field(..., min_length=1, description="name of the company")
    service_type: str = Field(...,min_length=1,description="type of service")