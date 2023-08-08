from typing import Optional
from uuid import UUID
from firebase_admin import auth

# from app.schemas.calls_schema import 
# from app.schemas.user_schema import UserUpdate


class UserService:  
    @staticmethod
    async def authenticate(called_number:str):

        users = auth.list_users().iterate_all() 

        # Check if called number is registered
        phone_numbers = [user.phone_number for user in users]
        
        return called_number in phone_numbers
    
    # @staticmethod
    # async def get_user_by_email(email: str) -> Optional[User]:
    #     user = await User.find_one(User.email == email)
    #     return user
    
    # @staticmethod
    # async def get_user_by_id(id: UUID) -> Optional[User]:
    #     user = await User.find_one(User.user_id == id)
    #     return user
    
    # @staticmethod
    # async def update_user(id: UUID, data: UserUpdate) -> User:
    #     user = await User.find_one(User.user_id == id)
    #     if not user:
    #         raise pymongo.errors.OperationFailure("User not found")
    
    #     await user.update({"$set": data.dict(exclude_unset=True)})
    #     return user