import datetime 
from fastapi import FastAPI, HTTPException

app = FastAPI()

class HotelReservationSystem:
    def __init__(self):
        self.__hotel = []
        self.__user = []
        self.__location = []
        self.__payment = []
    
    @property
    def hotel(self):
        return self.__hotel
    
    @hotel.setter
    def hotel(self, hotel:object):
        self.__hotel.append(hotel)
    
    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user:object):
        self.__user.append(user)
    
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, location:object):
        self.__location.append(location)
    
    @property
    def payment(self):
        return self.__payment
    
    @payment.setter
    def payment(self, payment):
        self.__payment.append(payment)
    
    def show_user(self):
        user = self.search_user_by_id(id)
        result = {}
        result["my account"] = {
            "name" : user.name,
            "telephone" : user.telephone,
            "email" : user.email
        }
        result["my booking"] = user.reservation
        result["purchase list"] = user.receipt
        return result
    
    def search_hotel(self, start_date:str, end_date:str, guest:int = 1, country:str = None, city:str = None, price:int = "0-40000", ratings:int = "1-2-3-4-5"):
        hotel_list = []
        start_date = start_date.split('-')
        start_date = datetime.date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
        end_date = end_date.split('-')
        end_date = datetime.date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
        price = price.split('-')
        ratings = ratings.split('-')
        for hotel in self.__hotel:
            if country != hotel.location.country and country != None:
                continue
            if city != hotel.location.city and city != None:
                continue
            if price[0] < hotel.room.cheapest_room() or price[1] > hotel.room.cheapest_room():
                continue
            check_rate = False
            for rate in ratings:
                if round(hotel.average_rating()) == rate:
                    check_rate = True
            if check_rate == False:
                continue
            for room in hotel.room:
                if hotel in hotel_list:
                    break
                if room.guests < guest:
                    continue
                if room.reservation == []:
                    hotel_list.append(hotel)
                    break
                available = False
                for resevation in room.reservation:
                    if (start_date < resevation.date_in and end_date < resevation.date_out) or (start_date > resevation.date_in and end_date > resevation.date_out):
                        available = True
                    else:
                        available = False
                if available:
                    hotel_list.append(hotel)
        result = {}
        for hotel in hotel_list:
            result[hotel.name] = {
                "Location" : hotel.location.city + ", " + hotel.location.country,
                "Price" : hotel.room[0].price
            }
        return result
    
    def search_hotel_by_name(self, name):
        for hotel in self.__hotel:
            if hotel.name == name:
                return hotel
    
    def get_hotel_details(self, name: str):
        selected_hotel = None
        for hotel in self.__hotel:
            if name == hotel.name:
                selected_hotel = hotel
                
                return {
            'name': selected_hotel.name,
            'available room': [{'detail': room.detail, 'price': room.price, 'guests': room.guests} for room in selected_hotel.room if room.available],
            'feedback': [{'user': feedback.user.name, 'comment': feedback.comment, 'rating': feedback.rating, 'time': feedback.time} for feedback in selected_hotel.feedback]
        }
        else:
            raise HTTPException(status_code=404, detail="Hotel not found")
    
    def search_user_by_id(self, id:int):
        for user in self.__user:
            if id == user.user_id:
                return user
        return None

    def create_reservation(self, hotel_id, detail, user, start, end):
        for hotels in self.__hotel:
            for users in self.__user:
                if users.user_id == user:
                    if hotel_id == hotels.id: 
                        for rooms in hotels.room:
                            if detail == rooms.detail:
                                data = Reservation(users.name, start, end)
                                data.hotel_id = hotels.id
                                data.room_detail = detail
                                rooms.reservation = data
                                users.reservation = data
                                return {
                                    "ID" : data.id,
                                    "Hotel" : hotels.name,
                                    "User" : user,
                                    "Start date" : data.date_in,
                                    "End date" : data.date_out,
                                    "Price" : rooms.price,
                                    "Detail" : rooms.detail,
                                    "Guests" : rooms.guests
                                }
        return "404 User Not Found"
        
    
    def get_reservation_details(self, user): #User ID Parameter
        flag = 0
        target = None
        for users in self.__user:
            if users.user_id == user:
                target = users
                flag = 1
        if flag == 1:
            reserve = {}
            reserve["Reservation"] = target.reservation
            if target.reservation == []:
                return "No Reservation"
            return reserve
      
     def change_reservation(self, user_id, reservation_id, new_date_in, new_date_out):
        for user in self.__user:
            if user.user_id == user_id:
                for reservation in user.reservation:
                    if reservation.id == reservation_id:
                        new_date_in = new_date_in.split('-')
                        new_date_in = datetime.date(int(new_date_in[2]), int(new_date_in[1]), int(new_date_in[0]))
                        new_date_out = new_date_out.split('-')
                        new_date_out = datetime.date(int(new_date_out[2]), int(new_date_out[1]), int(new_date_out[0]))
                        if(new_date_out < new_date_in ):
                            return "Error"
                        
                        for hotels in self.__hotel:    
                            if hotels.id == reservation.hotel_id:
                                for rooms in hotels.room:
                                    if reservation.room_detail == rooms.detail:
                                        if rooms.isavailable(rooms,new_date_in,new_date_out):                   
                                            old_reservation_date_in = reservation.date_in
                                            old_reservation_date_out = reservation.date_out
                                            reservation.date_in = new_date_in
                                            reservation.date_out = new_date_out
                                            return {
                                                "Your Old Check in Date: " : old_reservation_date_in,
                                                "Your Old Check out Date: ": old_reservation_date_out,
                                                "Your New Check in Date:": reservation.date_in,
                                                "Your New Check out Date": reservation.date_out
                        }
                return "No Reservation ID"
        return "User Not Found"

        
    #Payment(name,price,hotel,room)
    def add_payment(self, payment):
        for users in self.__user:
            if payment.name() == users.name(): #THIS SHIT IS WRONG
                for hotels in self.__hotel:
                    if payment.hotel() == hotels.name():
                        for rooms in hotels.room():
                            if payment.room() == rooms.detail():
                                self.__payment.append(payment)
                                return {
                                    "Name" : payment.name(),
                                    "Hotel" : payment.hotel(),
                                    "Room" : payment.room()                                 
                                }
            return "ERROR"
        
        ## This Code IS FUCK UP

    def add_receipt(self, receipt):
        self.__receipt.append(receipt)
        return {
            "Name" : receipt.payment().name(),
            "Hotel" : receipt.payment().hotel(),
            "Room" : receipt.payment().room(),
            "Check in Date" : receipt.checkin(),
            "Check out Date" : receipt.checkout(),
            "Price" : receipt.payment().amount()
        }

class Hotel:
    __code = 0
    def __init__(self, name, location:object):
        Hotel.__code += 1
        self.__id = Hotel.__code
        self.__name = name
        self.__location = location
        self.__rooms = []
        self.__feedback = []
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def location(self):
        return self.__location
    
    @property
    def room(self):
        return self.__rooms
    
    @room.setter
    def room(self, room:object):
        self.__rooms.append(room)
    
    @property
    def feedback(self):
        return self.__feedback
    
    @feedback.setter
    def feedback(self, feedback:object):
        self.__feedback.append(feedback)

    def cheapest_room(self):
        return min([room.price for room in self.__rooms])
    
    def average_rating(self):
        return sum(feedback.rating for feedback in self.__feedback) / len(self.__feedback)
    
    def search_room_by_name(self, name):
        for rooms in self.__rooms:
            if rooms.detail == name:
                return rooms
    
class Location:
    def __init__(self, country:str, city:str, coordinates:int):
        self.__country = country
        self.__city = city
        self.__coordinates = coordinates
    #     if country not in Location.__all_country:
    #         Location.__all_country.append(country)
    #     if city not in Location.__all_city:
    #         Location.__all_city.append(city)
    
    # @property
    # def all_country(self):
    #     return Location.__all_country
    
    # @property
    # def all_city(self):
    #     return Location.__all_city

    @property
    def country(self):
        return self.__country
    
    @property
    def city(self):
        return self.__city
    
    @property
    def coordinates(self):
        return self.__coordinates

class Room:
    def __init__(self, detail:str, price:int, guests:int):
        self.__detail = detail
        self.__price = price
        self.__guests = guests
        self.__reservation = []
        self.__isavailable = True

    @property
    def detail(self):
        return self.__detail
    
    @property
    def price(self):
        return self.__price
    
    @property
    def guests(self):
        return self.__guests
    
    @property
    def reservation(self):
        return self.__reservation
    
    @property
    def isavailable(self,start,end):
        start = start.split('-')
        end = end.split('-')
        start = datetime.date(int(start[2]), int(start[1]), int(start[0]))
        end = datetime.date(int(end[2]), int(end[1]), int(end[0]))
        for reservations in self.__reservation:
            reservestart = reservations.date_in
            reservestart = reservestart.split("-")
            reservestart = datetime.date(int(reservestart[2]), int(reservestart[1]), int(reservestart[0]))
            reserveend = reservations.date_out
            reserveend = reserveend.split("-")
            reserveend = datetime.date(int(reserveend[2]), int(reserveend[1]), int(reserveend[0]))
            if(start < reserveend and end > reservestart):
                return False
            return True
    @property
    def available(self):
        return self.__isavailable
    
    @property
    def toggle(self):
        self.__isavailable = not self.__isavailable
    
    @reservation.setter
    def reservation(self, reservation:object):
        self.__reservation.append(reservation)

    

class Reservation:
    __code = 0
    def __init__(self, user:object, date_in:object, date_out:object):
        Reservation.__code += 1
        self.__id = Reservation.__code
        self.__user = user
        self.__date_in = date_in
        self.__date_out = date_out
        self.__hotel_id = None
        self.__room_detail = None

    @property
    def id(self):
        return self.__id

    @property
    def user(self):
        return self.__user 
    
    @property
    def date_in(self):
        return self.__date_in
    
    @date_in.setter
    def date_in(self, date):
        self.__date_in = date
    
    @property
    def date_out(self):
        return self.__date_out
    
    @date_out.setter
    def date_out(self, date):
        self.__date_out = date

    @property
    def hotel_id(self):
        return self.__hotel_id
    
    @property
    def room_detail(self):
        return self.__room_detail
    
    @hotel_id.setter
    def hotel_id(self,hotel_id):
        self.__hotel_id = hotel_id
    
    @room_detail.setter
    def room_detail(self,room_detail):
        self.__room_detail = room_detail


class User:
    __code = 0
    def __init__(self, name:str, password:str, telephone:str, email:str):
        User.__code += 1
        self.__user_id = User.__code
        self.__name = name
        self.__password = password
        self.__telephone = telephone
        self.__email = email
        self.__receipt = []
        self.__reservation = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name    
    
    @name.setter     
    def name(self, name:str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password:str):
        self.__password = password
    
    @property 
    def telephone(self):
        return self.__telephone
    
    @telephone.setter
    def telephone(self, telephone:str):
        self.__telephone = telephone
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email:str):
        self.__email = email
    
    @property
    def receipt(self):
        return self.__receipt
    
    @receipt.setter
    def receipt(self, receipt:object):
        self.__receipt.append(receipt)

    @property
    def reservation(self):
        return self.__reservation
        
    @reservation.setter
    def reservation(self,reservation):
        self.__reservation.append(reservation)

class Feedback:
    def __init__(self, user:object, comment:str, rating:int, time:int):
        self.__user = user
        self.__comment = comment
        self.__rating = rating
        self.__time = time
    
    @property
    def user(self):
        return self.__user
    
    @property
    def comment(self):
        return self.__comment
    
    @property
    def rating(self):
        return self.__rating
    
    @property
    def time(self):
        return self.__time

class Payment:
    __code = 0
    def __init__(self,username,amount,hotelname,room):
        Payment.__code += 1
        self.id = Payment.__code
        self.__user = username
        self.__amount = amount
        self.__hotelname = hotelname
        self.__hotelroom = room

    @property
    def name(self):
        return self.__user
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def hotel(self):
        return self.__hotelname
    
    @property
    def room(self):
        return self.__hotelroom

class Discount: 
    def __init__(self, code, amount, expiration):
        self.__code = code
        self.__amount = amount
        self.__expiration = expiration
    
    @property
    def code(self):
        return self.__code
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def expiration(self):
        return self.__expiration

class Receipt:
    def __init__(self,payment,checkin,checkout):
        self.__payment = payment
        self.__checkin = checkin
        self.__checkout = checkout

    @property
    def payment(self):
        return self.__payment
    
    @property
    def checkin(self):
        return self.__checkin
    
    @property
    def checkout(self):
        return self.__checkout
    