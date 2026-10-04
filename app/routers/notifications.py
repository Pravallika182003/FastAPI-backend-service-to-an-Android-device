import os
from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.deps import get_current_user
from app.models import Notification, User, NotificationStatus
from app.schemas import NotificationCreate, NotificationOut 
from app.fcm import send_push_notification

router =  APIRouter(prefix="/notifications", tags=["notifications"])
DEFAULT_DEVICE_TOKEN = os.getenv("DEFAULT_DEVICE_TOKEN" ,"")

@router.post("/", response_model=NotificationOut, status_code=201)
def send_notification(payload:NotificationCreate,db:Session = Depends(get_db), current_user: User = Depends(get_current_user),):
    device_tokren= payload.device_token or DEFAULT_DEVICE_TOKEN
    if not device_tokren:
        raise HTTPException(status_code=400, detail="No device token provided")
    try:
        message_id=send_push_notification(device_tokren, payload.title, payload.body)
    except Exception as e:
        db.add(Notification(user_id=current_user.id, title=payload.title, body=payload.body, status=NotificationStatus.FAILED,))
        db.commit()
        raise  HTTPException(status_code=500, detail=f"Failed to send notification :  {e}")
    notification  = Notification(user_id=current_user.id, title=payload.title, body=payload.body, fcm_message_id=message_id, status=NotificationStatus.SENT,)
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

@router.get("",response_model=list[NotificationOut])
def list_notifications(db:Session   =  Depends(get_db), current_user: User=Depends(get_current_user),):
    return(
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )
                       
