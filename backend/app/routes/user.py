from fastapi import APIRouter

router=APIRouter(prefix="/user")

@router.get("/")
def user():
 return {
 "name":"Nakshatra Meena",
 "status":"active"
 }
