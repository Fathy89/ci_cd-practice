
from pydantic_settings import BaseSettings 
from dotenv import load_dotenv 

load_dotenv

class Config(BaseSettings):
    
    App_Name:str 
    db_password  : str
    db_name :str

    


