from fastapi import APIRouter

router=APIRouter(prefix="/wealth")


@router.get("/score")
def score():

 return {
 "financial_health_score":85
 }
