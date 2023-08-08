from typing import Optional
from uuid import UUID
import random

class SmsService:
    @staticmethod
    async def is_spam(content: str) -> bool:
        
        return "spam" in content.lower()

    @staticmethod
    async def evaluate_spam_message(message_content: str) -> str:
        is_spam_result = await SmsService.is_spam(message_content)
        
        if is_spam_result:
            return "Spam"
        else:
            return "Not Spam"
        
    
    @staticmethod
    async def Calculate_score(text:str):
        score = ""
        
        return str(score)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """is_spam = random.randint(0, 1)
        
        if is_spam:
            return {'spamStatus':'Spam', 'message':'model output'}
        else:
            return {'spamStatus':'Ham', 'message':'model output'}"""
