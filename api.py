import datetime 
from fastapi import FastAPI, HTTPException

app = FastAPI()

# ----------------------------
import main
# ----------------------------

myHotel = main.HotelReservationSystem()
myHotel.hotel = main.Hotel("Dusit Thani Pattaya", main.Location("Thai", "Pattaya", (12.9505757,100.732853)))
myHotel.hotel = main.Hotel("APA Hotel Ueno Ekimae", main.Location("Japan", "Pattaya", (35.7102846,139.7770179)))
myHotel.hotel = main.Hotel("Radisson Collection Hyland Shanghai", main.Location("China", "Shanghai", (31.2354936,121.4804668)))
myHotel.hotel = main.Hotel("Hotel Cour du Corbeau Strasbourg", main.Location("Strasbourg", "France", (13.763677399809191, 100.53466861970999)))
myHotel.hotel = main.Hotel("hotel five", main.Location("thai", "pattaya", (13.763677399809191, 100.53466861970999)))
myHotel.hotel = main.Hotel("hotel six", main.Location("thai", "pattaya", (13.763677399809191, 100.53466861970999)))
myHotel.hotel = main.Hotel("hotel seven", main.Location("japan", "tokyo", (13.763677399809191, 100.53466861970999)))

myHotel.hotel[0].imgsrc = "https://lh5.googleusercontent.com/p/AF1QipPsybvTkTY_3x8JlX_q-4TzKXLrpubv7lkl1wGg=w203-h135-k-no" #dusit thani

myHotel.hotel[0].room = main.Room("Breakfast not included", 500, 1)
myHotel.hotel[1].room = main.Room("Breakfast included", 1000, 2)
myHotel.hotel[2].room = main.Room("Don't smoke", 1200, 3)
myHotel.hotel[3].room = main.Room("Beautiful view", 1500, 2)
myHotel.hotel[4].room = main.Room("Poolside bar", 2500, 4)
myHotel.hotel[5].room = main.Room("Private pool", 4000, 6)
myHotel.hotel[6].room = main.Room("There is wifi", 5000, 2)

myHotel.hotel[0].room[0].reservation = main.Reservation("namthip", datetime.date(2023, 1, 1), datetime.date(2023, 1, 5))
myHotel.hotel[0].room[0].reservation = main.Reservation("john", datetime.date(2023, 1, 6), datetime.date(2023, 1, 8))
myHotel.hotel[3].room[0].reservation = main.Reservation("jack", datetime.date(2023, 1, 4), datetime.date(2023, 1, 7))
 
 
myHotel.user = main.User("user1", "1111", "0816228411", "one@gmail.com")
myHotel.user = main.User("user2", "2222", "0816228411", "two@gmail.com")
myHotel.user = main.User("user3", "3333", "0816228411", "tree@gmail.com")

feedback1 = main.Feedback(myHotel.user[0], "Great Hotel!", 4, "2024-02-21")
feedback2 = main.Feedback(myHotel.user[1], "Worst Hotel I've ever stayed", 1, "2023-11-09")
feedback3 = main.Feedback(myHotel.user[2], "Nice service!", 5, "2024-07-02")

myHotel.create_reservation(1, "Breakfast not included", 1, "1-10-2023", "5-10-2023")
myHotel.add_payment(main.Payment(1,500,"Dusit Thani Pattaya","Breakfast not included"))
myHotel.create_reservation(2, "Breakfast included", 1, "1-12-2023", "9-12-2023")
myHotel.add_payment(main.Payment(1,1000,"APA Hotel Ueno Ekimae","Breakfast included"))

# ---------------------------------------------
# http://127.0.0.1:8000/search/?start=1-1-2023&end=10-1-2023
# uvicorn api:app --reload

@app.get("/")
async def index():
    result = {}
    result["best_location"] = None
    result["best_city"] = None
    result["recommend"] = myHotel.search_hotel('1-1-2000', '2-1-2000')
    return result

@app.get("/search/")
async def search(start:str, end:str, guest:int = 1, country:str = None, city:str = None, price = "0-40000", rating = "1-2-3-4-5"):
    return myHotel.search_hotel(start, end, guest, country, city, price, rating)

@app.get("/user/")
async def user(id:int):
    return myHotel.show_user(id)

# -------------------RESERVATION--------------------------
# http://127.0.0.1:8000/reservation/?name=hotel%20one&detail=Breakfast%20not%20included&user=01&start=1-1-2023&end=10-1-2023
@app.get("/reservation/")
async def create_reservation(hotel_id:int, detail:str, user:int, start:str, end:str):
    user_reservation = myHotel.create_reservation(hotel_id, detail, user, start, end)
    return user_reservation
 
@app.post('/reservation/')
async def user_input_info(information:main.User_information):
    return information
# --------------------------------------------------------

# ---------------------PAYMENT----------------------------
# http://127.0.0.1:8000/payment/?name=Anna&hotel=hotel%20one&room=Breakfast%20not%20included&checkin=11-09-2023&checkout=02-10-2023
@app.get("/payment/")
async def pay(name:int,hotel:str,room:str,checkin:str,checkout:str):
    hotel = myHotel.search_hotel_by_name(hotel)
    room = hotel.search_room_by_name(room)
    price = room.final_price
    payment = myHotel.add_payment(main.Payment(name,price,hotel.name,room.detail)) 
    return payment
# --------------------------------------------------------

# ------------------------GET_RESERVATION--------------------------------
# http://127.0.0.1:8000/user_reservation/?user_id=01
# @app.get("/user_reservation/")
# async def get_reservation(user_id:str):
#     get_reservation = myHotel.get_reservation_details(user_id)
#     return get_reservation
# --------------------------------------------------------

# -----------------------Select Hotel----------------------
# http://127.0.0.1:8000/hotels
@app.get('/hotels')
def get_hotels():
    search_hotel_by_name = myHotel.search_hotel_by_name
    return search_hotel_by_name

# --------Search Available Room by Hotel's Name----------------
# http://127.0.0.1:8000/hotel?name=hotel%20one
@app.get('/hotel')
async def get_hotel_details(name: str):
    get_available_room = myHotel.get_hotel_details(name)
    return get_available_room

@app.get('/change/')
async def change_reservation(user:int,reservation_id:int,date_in:str,date_out:str,hotel_id:int):
    change_reservation = myHotel.change_reservation(user,reservation_id,date_in,date_out,hotel_id)
    return change_reservation

@app.get('/feedback/')
async def add_feedback(user: str, comment: str, rating: int, time: str):
    for users in myHotel.user:
        if users.name == user: 
            add_feedback = myHotel.add_feedback(user, comment, rating, time)
            return add_feedback
        

@app.get('/cancel')
async def cancel_reservation(user:int,reservation_id:int):
    cancel_reservation = myHotel.cancel_reservation(user,reservation_id)
    return cancel_reservation
