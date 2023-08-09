from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class RegisterCompanyModel(BaseModel):
    verification_document: str = Field(..., min_length=13, max_length=13, description="document that verifies authenticity of the company")
    company_name: str = Field(..., min_length=1, description="name of the company")
    service_type: str = Field(...,min_length=1,description="type of service")

class CompanyAPICallModel(BaseModel):
    company_name: str = Field(..., min_length=13, max_length=13, description="name of company")
    user_number: str = Field(..., min_length=1, description="name of user")
    company_number: str = Field(...,min_length=1,description="number of future caller")
    start_time: str = Field(...,min_length=1,description="timestamp of start of immunity")
    validity: str = Field(...,min_length=1,description="total dutration of immunity")
    message: str = Field(...,min_length=1,description="custom dispay message")