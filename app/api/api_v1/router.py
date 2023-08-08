from fastapi import APIRouter
from app.api.api_v1.handlers import calls, users, sms, companies

router = APIRouter()

router.include_router(calls.calls_router, prefix='/call', tags=['calls'])
router.include_router(users.users_router, prefix='/users', tags=['users'])
router.include_router(sms.messages_router, prefix='/sms',tags=['sms'])
router.include_router(companies.companies_router, prefix='/companies',tags=['companies'])