from fastapi import FastAPI
from routes import chatbot,wealth,user

app=FastAPI(
title="WealthMate AI"
)

app.include_router(user.router)
app.include_router(wealth.router)
app.include_router(chatbot.router)


@app.get("/")
def home():
    return {
    "message":"WealthMate AI API Running"
    }
