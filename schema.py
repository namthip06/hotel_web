from pydantic import BaseModel

class Payment(BaseModel):
    user_id : int
    reservation_id : int

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

# class EditRoomRequest(BaseModel):
#     hotel_name: str
#     room_detail: str
#     new_price: float
#     new_guests: int

# class RoomDetails(BaseModel):
#     room_type: str
#     price: float
#     max_guests: int

class Hotel(BaseModel):
    name : str
    country : str
    city : str
    maps : str

class Room(BaseModel):
    detail : str
    price : int
    guest : int 
