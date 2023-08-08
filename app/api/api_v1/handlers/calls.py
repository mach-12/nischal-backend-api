from fastapi import APIRouter, HTTPException, status
from app.schemas.calls_schema import IncomingCallsModel
from fastapi import Depends

from app.services.user_service import UserService
from app.services.calls_service import CallsService



calls_router = APIRouter()

@calls_router.post('/incoming', summary="Incoming call")#, response_model=UserOut)
async def check_incoming_call_spam(data: IncomingCallsModel):
    try:
        is_valid_user = await UserService.authenticate(data.called_phone_number)
    
        # check if is valid user
        if is_valid_user:
            return {'spamStaus':'Ham', 'message':'user is verified'}
            
        # TODO: check if number is in database
        
        # Run algorithm to check spam
        return await CallsService.evaluate_spam()
    
    except :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Calls service"
        )