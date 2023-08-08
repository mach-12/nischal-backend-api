from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    load_dotenv(dotenv_path='app/core/.env')
    API_V1_STR: str = "/api/v1"
    
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
    #     "http://localhost:3000"
    # ]
    
    PROJECT_NAME: str = "Cybershell Backend API"

    FIREBASE_CONFIG: dict = {
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID"),
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    }

    CERTIFICATE: dict = {
        "type": os.getenv("CERTIFICATE_TYPE"),
        "project_id": os.getenv("CERTIFICATE_PROJECT_ID"),
        "private_key_id": os.getenv("CERTIFICATE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("CERTIFICATE_PRIVATE_KEY").replace(r'\n', '\n'),
        "client_email": os.getenv("CERTIFICATE_CLIENT_EMAIL"),
        "client_id": os.getenv("CERTIFICATE_CLIENT_ID"),
        "auth_uri": os.getenv("CERTIFICATE_AUTH_URI"),
        "token_uri": os.getenv("CERTIFICATE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("CERTIFICATE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CERTIFICATE_CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("CERTIFICATE_UNIVERSE_DOMAIN"),
    }

    
    class Config:
        case_sensitive = True
        
settings = Settings()