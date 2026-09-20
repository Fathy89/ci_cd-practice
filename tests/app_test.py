from fastapi.testclient import TestClient
import pprint
import sys
pprint.pprint(sys.path)
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the API"
    }
    

def test_get_all() : 
    response = client.get("/users/all")
    assert response.status_code == 200
    assert response.json()==[
        {
    "User"  : "Ahmed" , 
    "Age" :  18  ,  
    "Status" :  True
        }  , 
       {
    "User"  : "Fathy" , 
    "Age" :  20 ,  
    "Status" :  False
        }  ,
    {
    "User"  : "Ibrahem" , 
    "Age" :  23  ,  
    "Status" :  True
        }  , 
    ]
    
def test_get_by_name() : 
    response = client.get("/users/name",params={"name":"Fathy"}) 
    
    assert response.status_code==200
    assert response.json() ==  {
        "User"  : "Fathy" , 
        "Age" :  20 ,  
        "Status" :  False
            } 

def test_not_vaild(): 
    response= client.get("/users/name",params={"name":"bro"})
    
    assert response.status_code==200
    assert response.json() ==  {"message": "Not Found!"}