from pydantic import BaseModel

class Pay(BaseModel):
    name : str
    hotel : str
    room : str
    check_in : str
    check_out : str

class Sign_up(BaseModel):
    user_name : str
    user_password : str
    tel_num : str
    email : str
    
class Review(BaseModel):
    user_name : str
    hotel_name : str
    comment : str
    rating : int
    time : str
    images : list

class Hotel(BaseModel):
    name : str
    country : str
    city : str
    maps : str

class Room(BaseModel):
    detail : str
    price : int
    guest : int 
