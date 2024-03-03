import main
import datetime

myHotel = main.HotelReservationSystem()
myHotel.hotel = main.Hotel("Dusit Thani Pattaya", main.Location("Thailand", "Pattaya", "https://maps.app.goo.gl/S1TfzFu1r7owKaT4A"))
myHotel.hotel = main.Hotel("APA Hotel Ueno Ekimae", main.Location("Japan", "Tokyo", "https://maps.app.goo.gl/UyMpFWLKPyz2RNru6"))
myHotel.hotel = main.Hotel("Radisson Collection Hyland Shanghai", main.Location("China", "Shanghai", "https://maps.app.goo.gl/4aEL8gDZ5UEwneEQ9"))
myHotel.hotel = main.Hotel("Hotel Cour du Corbeau Strasbourg", main.Location("France", "Strasbourg", "https://maps.app.goo.gl/Lptr6k9oVKpqEXkL7"))
myHotel.hotel = main.Hotel("Paris Marriott Champs Elysees Hotel", main.Location("France", "Paris", "https://maps.app.goo.gl/XvNgwXg3yT6KMqJLA"))
myHotel.hotel = main.Hotel("The Ritz-Carlton Tokyo", main.Location("Japan", "Tokyo", "https://maps.app.goo.gl/PCRaPdrkW9dg37Nx8"))
myHotel.hotel = main.Hotel("The Plaza Hotel", main.Location("USA", "New York", "https://maps.app.goo.gl/whUYzLXMh8RnM7EC6"))
myHotel.hotel = main.Hotel("Mandarin Oriental Bangkok", main.Location("Thailand", "Bangkok", "https://maps.app.goo.gl/yQb38PANxeCb5gd47"))
myHotel.hotel = main.Hotel("The Dorchester", main.Location("UK", "London", "https://maps.app.goo.gl/7L53ngktdbWLm4rV9"))
myHotel.hotel = main.Hotel("Rosewood London", main.Location("UK", "London", "https://maps.app.goo.gl/Qbkrp41wr6mPj28s7"))
myHotel.hotel = main.Hotel("The Peninsula Paris", main.Location("France", "Paris", "https://maps.app.goo.gl/SgMfQ2PVqDGfB6iY7"))
myHotel.hotel = main.Hotel("The St. Regis New York", main.Location("USA", "New York", "https://maps.app.goo.gl/ZJMxiR2UnS5C7t3J7"))
myHotel.hotel = main.Hotel("The Peninsula Shanghai", main.Location("China", "Shanghai", "https://maps.app.goo.gl/9Hr2CJBJ4v7qVj4E6"))
myHotel.hotel = main.Hotel("Hotel Eden - Dorchester Collection", main.Location("Italy", "Rome", "https://maps.app.goo.gl/swhhJsXqPX39Tb5r6"))
myHotel.hotel = main.Hotel("J.K. Place Roma", main.Location("Italy", "Rome", "https://maps.app.goo.gl/hok8XsEecg8PtncW8"))
myHotel.hotel = main.Hotel("Bangkok Marriott Marquis Queen's Park", main.Location("Thailand", "Bangkok", "https://maps.app.goo.gl/ZNqpvkjiaim29U2x7"))
myHotel.hotel = main.Hotel("Risonare Tomamu", main.Location("Japan", "Hokkaido", "https://maps.app.goo.gl/fAs4bZPBcwehc9N77"))
myHotel.hotel = main.Hotel("Conservatorium Hotel", main.Location("Netherlands", "Amsterdam", "https://maps.app.goo.gl/QGQqHso6AKj5KLRi8"))
myHotel.hotel = main.Hotel("Andaz Amsterdam Prinsengracht", main.Location("Netherlands", "Amsterdam", "https://maps.app.goo.gl/UzNP4yjmbnuJ54iA9"))
myHotel.hotel = main.Hotel("Lotte Hotel World", main.Location("Korea", "Seoul", "https://maps.app.goo.gl/BexHTjbYdEaFTnQ9A"))
myHotel.hotel = main.Hotel("Shilla Stay Gwanghwamun", main.Location("Korea", "Seoul", "https://maps.app.goo.gl/KHBj32WQoks1KBz76"))
myHotel.hotel = main.Hotel("The Westin Chosun Seoul", main.Location("Korea", "Seoul", "https://maps.app.goo.gl/djpTLspuzb5A5ms19"))
myHotel.hotel = main.Hotel("Hotel de Russie", main.Location("Italy", "Rome", "https://maps.app.goo.gl/6i89LRVGaohGueFS7"))
myHotel.hotel = main.Hotel("Niseko Hilton Village", main.Location("Japan", "Hokkaido", "https://maps.app.goo.gl/7sGLV8szgTDVhhoe9"))
myHotel.hotel = main.Hotel("Four Seasons Resort Chiang Mai", main.Location("Thailand", "Chiang Mai", "https://maps.app.goo.gl/tP2JMUCju12dNYoh9"))
myHotel.hotel = main.Hotel("Rachamankha", main.Location("Thailand", "Chiang Mai", "https://maps.app.goo.gl/LLYuZDEWMvDvAFvo9"))
myHotel.hotel = main.Hotel("Paradise Hotel Busan", main.Location("Korea", "Busan", "https://maps.app.goo.gl/Cfw7N74o5tFpjdSKA"))
myHotel.hotel = main.Hotel("The Langham Huntington, Pasadena", main.Location("USA", "California", "https://maps.app.goo.gl/QEVGXs7NnpVnX35C6"))
myHotel.hotel = main.Hotel("The Beverly Hills Hotel", main.Location("USA", "California", "https://maps.app.goo.gl/BexHTjbYdEaFTnQ9A"))
myHotel.hotel = main.Hotel("Park Hyatt Sydney", main.Location("Australia", "Sydney", "https://maps.app.goo.gl/opQpVeubiW5mNnyk8"))
myHotel.hotel = main.Hotel("The Langham, Melbourne", main.Location("Australia", "Melbourne", "https://maps.app.goo.gl/vdMUzWsGuA9iLh2X9"))
myHotel.hotel = main.Hotel("Victoria Xiengthong Palace", main.Location("Laos", "Luang Prabang", "https://maps.app.goo.gl/8MCxBDkhK5D3DJFy9"))
myHotel.hotel = main.Hotel("Pullman Luang Prabang", main.Location("Laos", "Luang Prabang", "https://maps.app.goo.gl/6BHFpQhHSXJa1F7e8"))
myHotel.hotel = main.Hotel("Amantaka", main.Location("Laos", "Luang Prabang", "https://maps.app.goo.gl/gBxxZmKa1dyghPRd6"))
myHotel.hotel = main.Hotel("Kiridara Luang Prabang", main.Location("Laos", "Luang Prabang", "https://maps.app.goo.gl/uJvdKrsswFXQ1CcB8"))

myHotel.hotel[0].imgsrc = "https://lh5.googleusercontent.com/p/AF1QipPsybvTkTY_3x8JlX_q-4TzKXLrpubv7lkl1wGg=w203-h135-k-no" #dusit thani
myHotel.hotel[1].imgsrc = "https://trvis.r10s.com/d/strg/ctrl/26/7eb1f94d78fcb92d41e8dea38be4d7d338bfa88b.47.9.26.3.jpg" #APA Hotel Ueno Ekimae
myHotel.hotel[2].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1280x900/332055080.jpg?k=cbd2365c62f7541f88777d68f47b75b47f11a7806011b810a13b1ebceb2902d3&o=&hp=1" #Radisson Collection Hyland Shanghai
myHotel.hotel[3].imgsrc = "https://www.cour-corbeau.com/wp-content/uploads/sites/25/2017/02/0.1.-Vue-site-Cour-du-Corbeau@Jean-Marc-Bannwarth_RVB_HD.jpg" #Hotel Cour du Corbeau Strasbourg
myHotel.hotel[4].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/451212164.jpg?k=7399719620d781dfa5b29494ec6a0a0c13613b80ab386bcd314e03b3923dddac&o=&hp=1" #Paris Marriott Champs Elysees Hotel
myHotel.hotel[5].imgsrc = "https://media.vogue.com.tw/photos/645b961525c28f514bbb1c8e/2:3/w_2560%2Cc_limit/RC%2520Tokyo_exterior_spring.jpg" #The Ritz-Carlton Tokyo
myHotel.hotel[6].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/496718760.jpg?k=608ceb5268219094ffb5f99c00dd1b869daf59485ca2ce071c49a9bd2feeba4f&o=&hp=1" #The Plaza Hotel
myHotel.hotel[7].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/236665735.jpg?k=4c3f6d75164608eb834404cd231958eef074346113854124f0bf1c68dc029201&o=&hp=1" #Mandarin Oriental
myHotel.hotel[8].imgsrc = "https://media.tatler.com/photos/64491d544b0c1dd744840940/4:3/w_5976,h_4482,c_limit/JS308250%20(1).jpg"#The Dorchester
myHotel.hotel[9].imgsrc = "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/1f/e4/48/rosewood-london.jpg?w=700&h=-1&s=1" #Rosewood London
myHotel.hotel[10].imgsrc = "https://www.peninsula.com/en/-/media/news-room/about-us/pr-company-profile.png?mw=905&hash=D2F2A2130F77BE2876FB195243EBAB2A" #The Peninsula Paris
myHotel.hotel[11].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/448885345.jpg?k=f50b995034d7cb05dc17d3675abda48a6d7a12ed4950f74d16deb729977b6f38&o=&hp=1" #The St. Regis New York
myHotel.hotel[12].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/28038346.jpg?k=2c2ef551dcfbb04a603bed1ceed4e056616e7d988d67a5719003cdc61ac8bb8a&o=&hp=1" #The Peninsula Shanghai
myHotel.hotel[13].imgsrc = "https://www.familyvacationcritic.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/sites/19/2014/08/hotel-eden.jpg.webp" #Hotel Eden - Dorchester Collection
myHotel.hotel[14].imgsrc = "https://elitevoyage.com/wp-content/uploads/2021/12/JK-Place-Roma-01.jpg" #J.K. Place Roma
myHotel.hotel[15].imgsrc = "https://photos.book5star.com/photos/7637/570b75b4_z.jpg" #Bangkok Marriott Marquis Queen's Park
myHotel.hotel[16].imgsrc = "https://media.hoshinoresorts.com/image/authenticated/s--LHIGtg7p--/c_fill,g_auto,h_630,w_1200/f_auto,q_auto/v1666159739/RISONARE_Tomamu_view_2_m5qxth.jpg" #Risonare Tomamu
myHotel.hotel[17].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/327045690.jpg?k=f2b656d53aa8f89680eaa23a2ea2745e7d702267dfb8a1b73613780c0b55d1c7&o=&hp=1" #Conservatorium Hotel
myHotel.hotel[18].imgsrc = "https://media-cdn.tripadvisor.com/media/photo-s/24/ff/6e/da/exterior.jpg" #Andaz Amsterdam Prinsengracht
myHotel.hotel[19].imgsrc = "https://cf.bstatic.com/xdata/images/hotel/max1024x768/438919681.jpg?k=8297c1e22522bfe2c1c1570265094549e8a32897f46f69b1803a0798ea0428c5&o=&hp=1" #Lotte Hotel World

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
