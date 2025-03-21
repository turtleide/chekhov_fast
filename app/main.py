from fastapi import FastAPI
from app.routers import users, reviews, plays, search
import os

app = FastAPI()

# 라우터 추가
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(plays.router, prefix="/plays", tags=["Plays"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Theater Review Service!"}