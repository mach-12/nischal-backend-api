from fastapi import APIRouter, HTTPException, status
from app.schemas.companies_schema import RegisterCompanyModel



companies_router = APIRouter()

@companies_router.get('/list', summary="get companies")#, response_model=UserOut)
async def get_all_companies(data):
    try:
        all_companies = {'company_id': ['1312', '5234', '8928']} 
        return all_companies
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in  service"
        )
    
@companies_router.post('/register', summary="register company to api")#, response_model=UserOut)
async def register_company(data: RegisterCompanyModel):
    try:
        return {'message': f'registered company {data.company_name}'}
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong in Companies service"
        )