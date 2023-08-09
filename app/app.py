from fastapi import FastAPI
import pyrebase
import firebase_admin
from firebase_admin import credentials
import uvicorn
from app.core.config import settings
from app.api.api_v1.router import router
import nltk 

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

firebase = None

@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    nltk.download('punkt')
    nltk.download('stopwords')

    global firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.CERTIFICATE)
        firebase_admin.initialize_app(cred)

    firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

app.include_router(router, prefix=settings.API_V1_STR)

@app.get('/')
async def index():
    return 'Welcome to Nischal Backend API'


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)