from fastapi import FastAPI

from app.routers import auth , notifications

app  = FastAPI(tittle="Notifications Service",  Version="1.0.0")

app.include_router(auth.router)
app.include_router(notifications.router)


@app.get("/health")
def health():
    return {"status":  "ok"}
