from fastapi import APIRouter, HTTPException, status
from app.schemas.companies_schema import CompanyAPICallModel, RegisterCompanyModel
from firebase_admin import firestore

companies_router = APIRouter()

# Define endpoint to register a company
@companies_router.post('/register', summary="register company to api")
async def register_company(data: RegisterCompanyModel):
    try:
        firestore_client = firestore.client()  # Initialize Firebase
        
        # Create a document in "company_registration" collection
        registration_data = {
            'verification_document': data.verification_document,
            'company_name': data.company_name,
            'service_type': data.service_type
        }
        firestore_client.collection("company_registration").add(registration_data)
        
        return {'message': f'Registered company {data.company_name}'}
    
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Companies service: {exception}"
        )

# Define endpoint to send a message from a company
@companies_router.post('/send_message', summary="company can send messages to user for certain time period")
async def send_company_message(data: CompanyAPICallModel):
    try:
        firestore_client = firestore.client()  # Initialize Firebase
        
        # Create a document in "company_requests" collection
        request_data = {
            'company_name': data.company_name,
            'user_number': data.user_number,
            'company_number': data.company_number,
            'start_time': data.start_time,
            'validity': data.validity,
            'message': data.message
        }
        firestore_client.collection("company_requests").add(request_data)
        
        return {'message': 'Success'}
    
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Companies service: {exception}"
        )
