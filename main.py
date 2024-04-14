"""  This module contains the main FastAPI application setup."""
from fastapi import FastAPI
from config.database import SessionLocal, engine
from model import models
from routers import subscription
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(subscription.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],git 
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
