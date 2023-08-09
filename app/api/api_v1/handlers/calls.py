from fastapi import APIRouter, HTTPException, status
from app.schemas.calls_schema import IncomingCallsModel
from firebase_admin import firestore
from app.app import db
from app.services.user_service import UserService
from app.services.calls_service import CallsService


# Normal,0
# Robocalls,1
# Scams,2
# Caller ID Spoofing,3
# Tech Support Scams,4
# Debt Collection,5

calls_router = APIRouter()

@calls_router.post('/incoming', summary="Incoming call")
async def check_incoming_call_spam(data: IncomingCallsModel):
    try:
        # Run algorithm to check spam
        spam_status = 'Spam'
        spam_score = '0.94'
        message = 'user is spam'

        firestore_client = firestore.client()
        

        # Create a call log dictionary
        call_log = {
            'caller_phone_number': data.caller_phone_number,
            'call_duration': data.call_duration,
            'call_timestamp': data.call_timestamp,
            'caller_in_contact': data.caller_in_contact,
            'call_type': data.call_type,
            'call_spam': data.call_spam,
            'user_auth_id': data.user_auth_id,
            'spam_status': spam_status,
            'spam_score': spam_score,
        }
        
        # Add call log to the "callogs" collection in Firebase
        firestore_client.collection("calllogs").add(call_log)

        
        return {
            'spamStatus': spam_status,
            'spamScore': spam_score,
            'message': message
        }
    
    except Exception  as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Something went wrong in Calls service {exception}"
        )