import datetime 
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from nltk import edit_distance

app = FastAPI()

if __name__ == "__main__" :
    uvicorn.run("api:app", host="127.0.0.1", port=8000, log_level="info")

# ----------------------------
import main
import hotel_list
import schema
# ----------------------------
# ---------------------------------------------
# http://127.0.0.1:8000/search/?start=1-1-2023&end=10-1-2023
# uvicorn api:app --reload
# python -m uvicorn api:app --reload

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def index():
    result = {}
    result["best_location"] = None
    result["best_city"] = None
    result["recommend"] = hotel_list.myHotel.search_hotel('1-1-2000', '2-1-2000')
    return result

@app.get("/search/")
async def search(start:str, end:str, guest:int = 1, country:str = "", city:str = "", price = "0-40000", rating = "0-1-2-3-4-5"):
    return hotel_list.myHotel.search_hotel(start, end, guest, country, city, price, rating)

@app.get("/rooms/")
async def get_rooms_by_detail(hotel_name: str, room_detail: str):
    get_rooms_by_detail = hotel_list.myHotel.get_rooms_by_detail(hotel_name, room_detail)
    return get_rooms_by_detail

@app.get("/user/")
async def user(id:int):
    return hotel_list.myHotel.show_user(id)

# -------------------RESERVATION--------------------------
# http://127.0.0.1:8000/reservation/?name=hotel%20one&detail=Breakfast%20not%20included&user=01&start=1-1-2023&end=10-1-2023
@app.get("/reservation/")
async def create_reservation(hotel_id:int, detail:str, start:str, end:str):
    user_reservation = hotel_list.myHotel.create_reservation(hotel_id, detail, start, end)
    if user_reservation == None:
        return "User Not Login"
    return user_reservation
# @app.post('/reservation/')
# async def user_input_info(information:main.User_information):
#     return information
# --------------------------------------------------------

# ---------------------PAYMENT----------------------------
# http://127.0.0.1:8000/payment/?name=Anna&hotel=hotel%20one&room=Breakfast%20not%20included&checkin=11-09-2023&checkout=02-10-2023
# @app.get("/payment/")
# async def pay(user_id: int, reservation_id: int):
#     payment = hotel_list.myHotel.add_payment(user_id, reservation_id)
#     return payment
@app.post("/payment/")
async def pay(payment_data: schema.Payment):
    payment = hotel_list.myHotel.add_payment( payment_data.reservation_id, payment_data.discount_code)
    return payment
# --------------------------------------------------------

# ------------------------GET_RESERVATION--------------------------------
# http://127.0.0.1:8000/user_reservation/?user_id=01
# @app.get("/user_reservation/")
# async def get_reservation(user_id:str):
#     get_reservation = myHotel.get_reservation_details(user_id)
#     return get_reservation
# --------------------------------------------------------

# # -----------------------Select Hotel----------------------
# # http://127.0.0.1:8000/hotels
# @app.get('/hotels')
# def get_hotels():
#     search_hotel_by_name = hotel_list.myHotel.search_hotel_by_name
#     return search_hotel_by_name

# --------Search Available Room by Hotel's Name----------------
# http://127.0.0.1:8000/hotel?name=hotel%20one
@app.get('/hotel')
async def get_hotel_details(name: str, start: str, end: str):
    get_available_room = hotel_list.myHotel.get_hotel_details(name, start, end)
    return get_available_room

@app.get('/change/')
async def change_reservation(change_reservation: schema.ChangeReservation):
    change_reservation = hotel_list.myHotel.change_reservation( change_reservation.reservation_id, change_reservation.date_in, change_reservation.date_out)
    return change_reservation

@app.post('/feedback/')
async def add_feedback(review: schema.Review):
    add_feedback = hotel_list.myHotel.add_feedback(review.user_name, review.hotel_name, review.comment, review.rating, review.time, review.images)
    return add_feedback

@app.post('/sign_up')
async def sign_up(sign_up: schema.Sign_up):
    sign_up = hotel_list.myHotel.sign_up(sign_up.user_name, sign_up.user_password, sign_up.phone_number, sign_up.email)
    return sign_up
 
@app.post('/login')
async def login(login: schema.Login):
    login = hotel_list.myHotel.log_in(login.email, login.user_password)
    return login

@app.get('/logout')
async def logout():
    logout = hotel_list.myHotel.log_out()
    return logout

@app.delete('/cancel')
async def cancel_reservation( reservation_id: int):
    cancel_reservation = hotel_list.myHotel.cancel_reservation( reservation_id)
    return cancel_reservation

@app.post('/admin/add_hotel')
async def add_hotel( add_hotel: schema.Hotel):
    add_hotel = hotel_list.myHotel.add_hotel(add_hotel.name, add_hotel.country, add_hotel.city, add_hotel.maps)
    return add_hotel

@app.post('/admin/add_room')
async def add_room(hotel_id: int, add_room: schema.Room):
    add_room = hotel_list.myHotel.add_room(hotel_id, add_room.detail, add_room.price, add_room.guest)
    return add_room

@app.post('/admin/add_discount')
async def add_discount(hotel_id:int, detail:str, add_discount: schema.Discount):
    add_discount = hotel_list.myHotel.add_discount(hotel_id, detail, add_discount.discount_code, add_discount.discount_amount, add_discount.discount_expiration)
    return add_discount

@app.put("/admin/edit-room/")
def edit_room( edit_room: schema.RoomEditor):
    edit_room = hotel_list.myHotel.edit_room(edit_room.hotel_name, edit_room.room_detail, edit_room.new_price, edit_room.new_guests)
    return edit_room

@app.put('/admin/edit-hotel/')
def edit_hotel(edit_hotel: schema.HotelEditor):
    edit_hotel = hotel_list.myHotel.edit_hotel( edit_hotel.hotel_name, edit_hotel.country, edit_hotel.city, edit_hotel.maps, edit_hotel.imgsrc)
    return edit_hotel

@app.delete('/admin/remove-hotel/')
async def remove_hotel( hotel_name: str):
    remove_hotel = hotel_list.myHotel.remove_hotel(hotel_name)
    return remove_hotel

@app.delete('/admin/remove-room/') 
async def remove_room(hotel_name: str, room_detail: str):
    remove_room = hotel_list.myHotel.remove_room( hotel_name, room_detail)
    return remove_room  

@app.put('/user/change-info/')
def change_user_info(email:str, change_user_info: schema.UserInfoEditor):
    change_user_info = hotel_list.myHotel.change_user_info(email, change_user_info.new_name, change_user_info.new_password, change_user_info.new_telephone)
    return change_user_info

@app.get('/currentuser')
async def get_current_user():
    current_user = hotel_list.myHotel.current_user
    return current_user
