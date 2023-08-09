from typing import Optional
from uuid import UUID
import random
from firebase_admin import firestore

# from app.schemas.calls_schema import 

# from app.schemas.user_schema import UserUpdate


class CallsService:
    @staticmethod    
    async def check_phone_number_spam(phone_number: str):
        try:
            firestore_client = firestore.client()  # Initialize Firebase
            
            # Fetch all call logs for the given phone number
            call_logs_ref = firestore_client.collection("calllogs").where("caller_phone_number", "==", phone_number).stream()
            
            total_logs = 0
            spam_logs = 0
            
            # Count spam logs
            for call_log in call_logs_ref:
                total_logs += 1
                if call_log.get("spam_status") == "Spam":
                    spam_logs += 1
            
            # Calculate spam score using a frequency-based approach
            spam_score = spam_logs / total_logs if total_logs > 0 else 0
            
            return {'spamScore': spam_score}
        except:
            return {'exception'}
        