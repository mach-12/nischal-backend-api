from fastapi import APIRouter, HTTPException, status
from app.schemas.email_schema import IncomingEmailsModel
from app.services import text_spam_service
from app.services.user_service import UserService
from firebase_admin import firestore

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
        
        model_output = await text_spam_service.TextSpamService.evaluate_spam_message(message_content=data.email_body)
        
        # Run algorithm to check spam
        spamStatus = 'Spam' if model_output['spam'] else 'Ham'

        firestore_client = firestore.client()  # Initialize Firebase
        
        # Create an email log dictionary
        email_log = {
            'email_head': data.email_head,
            'email_body': data.email_body,
            'email_sender': data.email_sender,
            'email_user': data.email_user,
            'call_spam': data.call_spam,
            'user_auth_id': data.user_auth_id,
            'spam_status': spamStatus,
            'spam_score': model_output['riskScore']
        }
        
        # Add email log to the "emaillogs" collection in Firebase
        firestore_client.collection("emaillogs").add(email_log)
        return {'spamStaus': spamStatus, 'spamScore':model_output['riskScore'], 'message': f'user is {spamStatus}'}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Emails service{e}"
        )
    




