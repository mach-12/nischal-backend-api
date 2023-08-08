from fastapi import APIRouter, HTTPException, status
from firebase_admin import auth

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
    
    