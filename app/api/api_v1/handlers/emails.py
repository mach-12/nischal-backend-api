from fastapi import APIRouter, HTTPException, status
from app.schemas.email_schema import IncomingEmailsModel
from app.services import text_spam_service
from app.services.user_service import UserService

email_router = APIRouter()

@email_router.post('/incoming', summary="Incoming call")#, response_model=UserOut)
async def check_incoming_email_spam(data: IncomingEmailsModel):
    try:
        # is_valid_user = await UserService.authenticate(data.called_phone_number)
        
        model_output = await text_spam_service.evaluate_spam_message(message_content=data.message)
        
        # check if is valid user
        # if is_valid_user:
        #     return {'spamStaus':'Ham', 'spamScore':'0.11', 'message':'user is verified'}
            
        # TODO: check if number is in database
        
        # Run algorithm to check spam
        spamStatus = 'Spam' if model_output['spam'] else 'Ham'
        return {'spamStaus': spamStatus, 'spamScore':model_output['riskScore'], 'message': f'user is {spamStatus}'}
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Emails service"
        )