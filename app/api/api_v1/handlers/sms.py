from fastapi import APIRouter, HTTPException, status
from app.schemas.message_schema import IncomingMessagesModel

from app.services.user_service import UserService
from app.services.sms_service import SmsService  # Assuming you have a messages_service module
from app.services.text_spam_service import TextSpamService
messages_router = APIRouter()

@messages_router.post('/incoming', summary="Incoming message")
async def check_incoming_message_spam(data: IncomingMessagesModel):
    try:

        phone_number_of_messenger = data.phone_number_of_messenger
        message = data.message_content

        model_output = await TextSpamService.evaluate_spam_message(message_content=message)
        # is_valid_user = await UserService.authenticate(phone_number_of_messenger)

        # Check if the user is valid
        # if is_valid_user:
        #     return {'spamStaus':'Ham', 'spamScore':'0.15', 'message': 'User is verified'}
            
        # TODO: Check if the number is in the database (if needed)
        
    
        # Run algorithm to check spam using MessagesService
        spamStatus = 'Spam' if model_output['spam'] else 'Ham'
        return {'spamStaus': spamStatus, 'spamScore':model_output['riskScore'], 'message': f'user is {spamStatus}'}
    
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Messages service {error}"
        )
