from fastapi import APIRouter, HTTPException, status
from app.schemas.message_schema import IncomingMessagesModel
from fastapi import Depends

from app.services.user_service import UserService
from app.services.sms_service import SmsService  # Assuming you have a messages_service module

messages_router = APIRouter()

@messages_router.post('/incoming_message', summary="Incoming message")
async def check_incoming_message_spam(data: IncomingMessagesModel):
    try:
        is_valid_user = await UserService.authenticate(data.phone_number_of_messenger)
    
        # Check if the user is valid
        if is_valid_user:
            return {'spamStatus': 'Ham', 'message': 'User is verified'}
            
        # TODO: Check if the number is in the database (if needed)
        
        # Run algorithm to check spam using MessagesService
        return await SmsService.evaluate_spam_message()
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Messages service"
        )
