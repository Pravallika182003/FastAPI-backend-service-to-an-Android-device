from app.config import settings
import firebase_admin
from firebase_admin import  credentials,messaging

_intitalized = False

def _init():
    global _intitalized
    if _intitalized or not settings.FIREBASE_CREDENTIALS_PATH:
        return  
    import firebase_admin
    from firebase_admin import credentials
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
    _intitalized = True

def send_push_notification(device_token: str,title: str, body: str) -> str:
    """send push via FCM. Returns message id.Mock mode when no creds configured"""

    if not device_token:
        raise RuntimeError("No device token provided")
    if not firebase_admin._apps:
        cred_path = settings.FIREBASE_CREDENTIALS_PATH
        if not cred_path:
            return "mock-message-id"
        cred = credentials.Certificate(cred_path)

        firebase_admin.initialize_app(cred)

    message = messaging.Message(notification=messaging.Notification(title=title,body=body),
                    token=device_token,
            
    )
        


    return messaging.send(message)


        