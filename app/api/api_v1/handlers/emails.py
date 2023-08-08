from fastapi import APIRouter, HTTPException, status
from app.schemas.email_schema import IncomingEmailsModel
from app.services.user_service import UserService




email_router = APIRouter()

@email_router.post('/incoming', summary="Incoming call")#, response_model=UserOut)
async def check_incoming_email_spam(data: IncomingEmailsModel):
    try:
        is_valid_user = await UserService.authenticate(data.called_phone_number)
    
        # check if is valid user
        if is_valid_user:
            return {'spamStaus':'Ham', 'message':'user is verified'}
            
        # TODO: check if number is in database
        
        # Run algorithm to check spam
        return {'spamStatus': 'Spam', 'message': 'user is spam'}
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Emails service"
        )