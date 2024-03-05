import datetime 
from fastapi import FastAPI, HTTPException

app = FastAPI()

# ----------------------------
import main
import hotel_list
import schema
# ----------------------------
# ---------------------------------------------
# http://127.0.0.1:8000/search/?start=1-1-2023&end=10-1-2023
# uvicorn api:app --reload
# python -m uvicorn api:app --reload

@app.get("/")
async def index():
    result = {}
    result["best_location"] = None
    result["best_city"] = None
    result["recommend"] = hotel_list.myHotel.search_hotel('1-1-2000', '2-1-2000')
    return result

@app.get("/search/")
async def search(start:str, end:str, guest:int = 1, country:str = None, city:str = None, price = "0-40000", rating = "1-2-3-4-5"):
    return hotel_list.myHotel.search_hotel(start, end, guest, country, city, price, rating)

@app.get("/single-bed-rooms/")
async def get_single_bed_rooms(hotel_name: str):
    single_bed_rooms = hotel_list.myHotel.get_single_bed_rooms(hotel_name)
    return {"single_bed_rooms": single_bed_rooms}

@app.get("/double-bed-rooms/")
async def get_double_bed_rooms(hotel_name: str):
    double_bed_rooms = hotel_list.myHotel.get_double_bed_rooms(hotel_name)
    return {"double_bed_rooms": double_bed_rooms}

@app.get("/queen-size-bed-rooms/")
async def get_queen_size_bed_rooms(hotel_name: str):
    queen_size_bed_rooms = hotel_list.myHotel.get_queen_size_bed_rooms(hotel_name)
    return {"queen_size_bed_rooms": queen_size_bed_rooms}

@app.get("/king-size-bed-rooms/")
async def get_king_size_bed_rooms(hotel_name: str):
    king_size_bed_rooms = hotel_list.myHotel.get_king_size_bed_rooms(hotel_name)
    return {"king_size_bed_rooms": king_size_bed_rooms}

@app.get("/user/")
async def user(id:int):
    return hotel_list.myHotel.show_user(id)

# -------------------RESERVATION--------------------------
# http://127.0.0.1:8000/reservation/?name=hotel%20one&detail=Breakfast%20not%20included&user=01&start=1-1-2023&end=10-1-2023
@app.get("/reservation/")
async def create_reservation(hotel_id:int, detail:str, user:int, start:str, end:str):
    user_reservation = hotel_list.myHotel.create_reservation(hotel_id, detail, user, start, end)
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
    payment = hotel_list.myHotel.add_payment(payment_data.user_id , payment_data.reservation_id)
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
async def get_hotel_details(name: str):
    get_available_room = hotel_list.myHotel.get_hotel_details(name)
    return get_available_room

@app.get('/change/')
async def change_reservation(change_reservation: schema.ChangeReservation):
    change_reservation = hotel_list.myHotel.change_reservation(change_reservation.user, change_reservation.reservation_id, change_reservation.date_in, change_reservation.date_out)
    return change_reservation

@app.post('/feedback/')
async def add_feedback(review: schema.Review):
    add_feedback = hotel_list.myHotel.add_feedback(review.user_name, review.hotel_name, review.comment, review.rating, review.time, review.images)
    return add_feedback

@app.post('/sign up')
async def sign_up(sign_up: schema.Sign_up):
    sign_up = hotel_list.myHotel.sign_up(sign_up.user_name, sign_up.user_password, sign_up.phone_number, sign_up.email)
    return sign_up
 
@app.get('/login')
async def login(email: str, user_password: str):
    login = hotel_list.myHotel.log_in(email,user_password)
    return login

@app.delete('/cancel')
async def cancel_reservation(user: int, reservation_id: int):
    cancel_reservation = hotel_list.myHotel.cancel_reservation(user, reservation_id)
    return cancel_reservation

@app.post('/add_hotel')
async def add_hotel(user:int, add_hotel: schema.Hotel):
    add_hotel = hotel_list.myHotel.add_hotel(user, add_hotel.name, add_hotel.country, add_hotel.city, add_hotel.maps)
    return add_hotel

@app.post('/add_room')
async def add_room(user: int, hotel_id: int, add_room: schema.Room):
    add_room = hotel_list.myHotel.add_room(user, hotel_id, add_room.detail, add_room.price, add_room.guest)
    return add_room

@app.put("/admin/edit-room/")
def edit_room(user_id: int, edit_room: schema.RoomEditor):
    edit_room = hotel_list.myHotel.edit_room(user_id, edit_room.hotel_name, edit_room.room_detail, edit_room.new_price, edit_room.new_guests)
    return edit_room

@app.put('/admin/edit-hotel/')
def edit_hotel(user_id: int, edit_hotel: schema.HotelEditor):
    edit_hotel = hotel_list.myHotel.edit_hotel(user_id, edit_hotel.hotel_name, edit_hotel.country, edit_hotel.city, edit_hotel.maps, edit_hotel.imgsrc)
    return edit_hotel

@app.delete('/admin/remove-hotel/')
async def remove_hotel(user_id: int, hotel_name: str):
    remove_hotel = hotel_list.myHotel.remove_hotel(user_id, hotel_name)
    return remove_hotel

@app.delete('/admin/remove-room/') 
async def remove_room(user_id: int, hotel_name: str, room_detail: str):
    remove_room = hotel_list.myHotel.remove_room(user_id, hotel_name, room_detail)
    return remove_room  

@app.put('/user/change-info/')
def change_user_info(email:str, change_user_info: schema.UserInfoEditor):
    change_user_info = hotel_list.myHotel.change_user_info(email, change_user_info.new_name, change_user_info.new_password, change_user_info.new_telephone)
    return change_user_info
