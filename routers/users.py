from fastapi import APIRouter ,Depends
from services import users_logic  
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

user  =  users_logic.Users()



@router.get("/all") 
def get_all() : 
    return user.get_all()


@router.get("/name") 
def get_by_name(name:str)  : 
    return user.get_user_by_name(name) 
