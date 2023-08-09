from fastapi import APIRouter, HTTPException, status
from app.schemas.message_schema import IncomingMessagesModel
from firebase_admin import firestore
from app.services.user_service import UserService
from app.services.sms_service import SmsService  # Assuming you have a messages_service module
from app.services.text_spam_service import TextSpamService

messages_router = APIRouter()

# Normal,0
# Phishing,1
# Scams,2
# Spoofing,3
# Subscriptions,4

@messages_router.post('/incoming', summary="Incoming message")
async def check_incoming_message_spam(data: IncomingMessagesModel):
    try:

        phone_number_of_messenger = data.phone_number_of_messenger
        message = data.message_content

        model_output = await TextSpamService.evaluate_spam_message(message_content=message)
        # is_valid_user = await UserService.authenticate(phone_number_of_messenger)


    
        # Run algorithm to check spam using MessagesService
        spamStatus = 'Spam' if model_output['spam'] else 'Ham'

        firestore_client = firestore.client()  # Initialize Firebase
        
        # Create an SMS log dictionary
        sms_log = {
            'phone_number_of_messenger': data.phone_number_of_messenger,
            'called_name': data.called_name,
            'message_content': data.message_content,
            'call_spam': data.call_spam,
            'user_auth_id': data.user_auth_id,
            'spam_status': spamStatus,
            'spam_score': model_output['riskScore']
        }
        
        # Add SMS log to the "smslogs" collection in Firebase
        firestore_client.collection("smslogs").add(sms_log)
        
        return {'spamStaus': spamStatus, 'spamScore':model_output['riskScore'], 'message': f'user is {spamStatus}'}
    
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Messages service \n{error}"
        )
