from fastapi import APIRouter, HTTPException, status
from app.schemas.email_schema import IncomingEmailsModel
from app.services import text_spam_service
from app.services.user_service import UserService

email_router = APIRouter()

# Normal,0
# Phishing,1
# Scams,2
# Advertisements,3
# Malware and Virus,4

@email_router.post('/incoming', summary="Incoming email")#, response_model=UserOut)
async def check_incoming_email_spam(data: IncomingEmailsModel):
    try:
        # is_valid_user = await UserService.authenticate(data.called_phone_number)
        
        model_output = await text_spam_service.evaluate_spam_message(message_content=data.message)
        
        # Run algorithm to check spam
        spamStatus = 'Spam' if model_output['spam'] else 'Ham'
        return {'spamStaus': spamStatus, 'spamScore':model_output['riskScore'], 'message': f'user is {spamStatus}'}
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Emails service"
        )
    



