from fastapi import APIRouter, HTTPException, status
from app.schemas.calls_schema import IncomingCallsModel
from fastapi import Depends
from firebase_admin import auth

from app.services.calls_service import CallsService
from app.services.user_service import UserService


users_router = APIRouter()

@users_router.get('/all', summary="all users")#, response_model=UserOut)
async def check_incoming_call_spam():
    try:
        users = auth.list_users().iterate_all()
        users = [user.phone_number for user in users]


        return users #CallsService.evaluate_spam()
    except :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Calls service"
        )
    
    