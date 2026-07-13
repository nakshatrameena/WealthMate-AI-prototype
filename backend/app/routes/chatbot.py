from fastapi import APIRouter
from ai.advisor_model import advisor

router=APIRouter(prefix="/chat")


@router.get("/{question}")
def chat(question:str):

 return {
 "answer":advisor(question)
 }
