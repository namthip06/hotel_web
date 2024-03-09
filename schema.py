from pydantic import BaseModel

class Payment(BaseModel):
    reservation_id : int
    discount_code : str

class Sign_up(BaseModel):
    user_name : str
    user_password : str
    phone_number : str
    email : str

class Review(BaseModel):
    user_name : str
    hotel_name : str
    comment : str
    rating : int
    time : str

class Hotel(BaseModel):
    name : str
    country : str
    city : str
    maps : str

class Room(BaseModel):
    detail : str
    price : int
    guest : int 

class Discount(BaseModel):
    discount_code : str
    discount_amount: float
    discount_expiration: str

class HotelEditor(BaseModel):
    hotel_name : str
    country : str
    city : str
    maps : str
    imgsrc : str

class RoomEditor(BaseModel):
    hotel_name : str
    room_detail : str
    new_price : int
    new_guests : int

class ChangeReservation(BaseModel):
    reservation_id : int
    date_in : str
    date_out : str

class UserInfoEditor(BaseModel):
    new_name : str
    new_password : str
    new_telephone : str

class Login(BaseModel):
    email : str
    user_password : str
