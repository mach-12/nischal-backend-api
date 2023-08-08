from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
    #     "http://localhost:3000"
    # ]
    
    PROJECT_NAME: str = "Cybershell Backend API"

    FIREBASE_CONFIG: dict = {
        "apiKey": config("FIREBASE_API_KEY"),
        "authDomain": config("FIREBASE_AUTH_DOMAIN"),
        "projectId": config("FIREBASE_PROJECT_ID"),
        "storageBucket": config("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": config("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": config("FIREBASE_APP_ID"),
        "databaseURL": config("FIREBASE_DATABASE_URL"),
    }

    CERTIFICATE: dict = {
        "type": config("CERTIFICATE_TYPE"),
        "project_id": config("CERTIFICATE_PROJECT_ID"),
        "private_key_id": config("CERTIFICATE_PRIVATE_KEY_ID"),
        "private_key": config("CERTIFICATE_PRIVATE_KEY").replace(r'\n', '\n'),
        "client_email": config("CERTIFICATE_CLIENT_EMAIL"),
        "client_id": config("CERTIFICATE_CLIENT_ID"),
        "auth_uri": config("CERTIFICATE_AUTH_URI"),
        "token_uri": config("CERTIFICATE_TOKEN_URI"),
        "auth_provider_x509_cert_url": config("CERTIFICATE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": config("CERTIFICATE_CLIENT_X509_CERT_URL"),
        "universe_domain": config("CERTIFICATE_UNIVERSE_DOMAIN"),
    }

    
    class Config:
        case_sensitive = True
        
settings = Settings()