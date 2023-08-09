from typing import Optional
from uuid import UUID
import random

class SmsService:
    @staticmethod
    async def evaluate_spam_message(message_content: str) -> str:
        return "Not Spam"
    
    @staticmethod
    async def Calculate_score(text:str):
        score = "0.5"
        
        return str(score)