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
myHotel.hotel = main.Hotel("Kantary Hills Hotel", main.Location("Thailand", "Chiang Mai", "https://maps.app.goo.gl/AN5QJydoJgRP7XRv9"))
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
myHotel.hotel = main.Hotel("TIME Moonstone Hotel Apartments", main.Location("UAE", "Dubai", "https://maps.app.goo.gl/j7fLyXEZQqPs3iSz5"))
myHotel.hotel = main.Hotel("Arthotel Munich", main.Location("Germany", "Munich", "https://maps.app.goo.gl/kcUitC6fPTcZrkms6"))
myHotel.hotel = main.Hotel("Boutique Hotel Atrium Munchen", main.Location("Germany", "Munich", "https://maps.app.goo.gl/ivRreU8xH1HDTDw4A"))
myHotel.hotel = main.Hotel("Copthorne Hotel", main.Location("New Zealand", "Queenstown", "https://maps.app.goo.gl/bAGRjK3RkudP7T41A"))
myHotel.hotel = main.Hotel("Heartland Hotel", main.Location("New Zealand", "Queenstown", "https://maps.app.goo.gl/vEJZiCgSyctjM2FfA"))
myHotel.hotel = main.Hotel("mi-pad", main.Location("New Zealand", "Queenstown", "https://maps.app.goo.gl/ggwPjSy5xRR5zbhL9"))
myHotel.hotel = main.Hotel("Hotel Guillen Jr", main.Location("Mexico", "Tijuana", "https://maps.app.goo.gl/GLnMbNQ8WAm4KMgy8"))
myHotel.hotel = main.Hotel("Baja Inn Hoteles La Mesa", main.Location("Mexico", "Tijuana", "https://maps.app.goo.gl/qHZPWU6zsBCYvYqS7"))
myHotel.hotel = main.Hotel("Kabayan Hotel Pasay", main.Location("Philippines", "Manila", "https://maps.app.goo.gl/DF5kGb16druLHuAZ8"))
myHotel.hotel = main.Hotel("Radisson Blu Royal Viking Hotel", main.Location("Sweden", "Stockholm", "https://maps.app.goo.gl/moptJH8oFSxriPa8A"))
myHotel.hotel = main.Hotel("Thon Partner Hotel Kungsbron", main.Location("Sweden", "Stockholm", "https://maps.app.goo.gl/FbjSyP7Aoygn1yM99"))
myHotel.hotel = main.Hotel("Clarion Hotel Amaranten", main.Location("Sweden", "Stockholm", "https://maps.app.goo.gl/BnMQypvVyTWiDwEAA"))
myHotel.hotel = main.Hotel("Clarion Hotel Sign", main.Location("Sweden", "Stockholm", "https://maps.app.goo.gl/4MJHaKfmKLajwwQY8"))
myHotel.hotel = main.Hotel("Riu Plaza España", main.Location("Spain", "Madrid", "https://maps.app.goo.gl/kbvHHFSkawmJbExd7"))
myHotel.hotel = main.Hotel("Ilunion Alcalá Norte", main.Location("Spain", "Madrid", "https://maps.app.goo.gl/3L3UFJmmCwUPQQsq9"))
    
#Dusit Thani Pattaya
myHotel.hotel[0].imgsrc.extend(["https://lh5.googleusercontent.com/p/AF1QipPsybvTkTY_3x8JlX_q-4TzKXLrpubv7lkl1wGg=w203-h135-k-no",
                          "https://cf.bstatic.com/xdata/images/hotel/max1024x768/64762789.jpg?k=b310274778d31e6bb5a201bd622b2712b368170ced8b4b19c46aa38758452ef0&o=&hp=1",
                          "https://cf.bstatic.com/xdata/images/hotel/max1280x900/252343023.jpg?k=272079840535c50d0d509d83da54f50e4809c53171e3bed41452a4f469752257&o=&hp=1",
                          "https://cf.bstatic.com/xdata/images/hotel/max1280x900/252341827.jpg?k=25554b86d4713834e1b15e2f90ee46cfb6f329adc4382566f18f224928d5ae68&o=&hp=1"])
#APA Hotel Ueno Ekimae
myHotel.hotel[1].imgsrc.extend(["https://trvis.r10s.com/d/strg/ctrl/26/7eb1f94d78fcb92d41e8dea38be4d7d338bfa88b.47.9.26.3.jpg",
                          " https://cf.bstatic.com/xdata/images/hotel/max1280x900/169366217.jpg?k=058e4333e332726976483fff7e0d4989328620082ffbb357263410e5601f7f95&o=&hp=1",
                          "https://q-xx.bstatic.com/xdata/images/hotel/max750/309135188.jpg?k=4ccb435e54de8de5fb4196c76fc3e9f8c220f238ae5de5892b3f26e63b7870d5&o="])
#Radisson Collection Hyland Shanghai
myHotel.hotel[2].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1280x900/332055080.jpg?k=cbd2365c62f7541f88777d68f47b75b47f11a7806011b810a13b1ebceb2902d3&o=&hp=1",
                           "https://media.radissonhotels.net/image/radisson-collection-hotel-hyland-shanghai/standard--1/16256-140364-f71651095_4k.jpg?impolicy=CustomCrop&cwidth=800&cheight=610",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/21/a3/c5/4d/club-lounge.jpg?w=1100&h=-1&s=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/332055106.jpg?k=93944195df0f98979860c8a333393aedad29464b43ec126182e668ff1b978905&o=&hp=1"])
#Hotel Cour du Corbeau Strasbourg
myHotel.hotel[3].imgsrc.extend(["https://www.cour-corbeau.com/wp-content/uploads/sites/25/2017/02/0.1.-Vue-site-Cour-du-Corbeau@Jean-Marc-Bannwarth_RVB_HD.jpg",
                           "https://www.ahstatic.com/photos/7575_rosdd_00_p_1024x768.jpg",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/80/77/24/exterior.jpg?w=700&h=-1&s=1",
                           "https://dayuse.twic.pics/hotels/9806/6fd7a5aec14dfd7dee0457a03f08f311-cour-du-corbeau.png?twic=v1/cover=3840/quality=75"])
#Paris Marriott Champs Elysees Hotel
myHotel.hotel[4].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/451212164.jpg?k=7399719620d781dfa5b29494ec6a0a0c13613b80ab386bcd314e03b3923dddac&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/451212167.jpg?k=a71f271ae364d40d6d7935dfa715a9a060c5c9674a06df962fe5eed7209d0c2e&o=&hp=1",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/38/f6/49/executive-suite-guest.jpg?w=700&h=-1&s=1",
                           "https://s7d1.scene7.com/is/image/marriotts7prod/mc-pardt-pardt-brunch-1-38106:Classic-Hor?wid=1846&fit=constrain"])
#The Ritz-Carlton Tokyo
myHotel.hotel[5].imgsrc.extend(["https://media.vogue.com.tw/photos/645b961525c28f514bbb1c8e/2:3/w_2560%2Cc_limit/RC%2520Tokyo_exterior_spring.jpg",
                           "https://media.cntraveler.com/photos/59e7bba6ae4bf22242a1f774/16:9/w_2560,c_limit/Bedroom-RitzCarltonTokyo-Japan-CRHotel.jpg",
                           "https://www.hotelscombined.com/rimg/himg/7c/00/4c/leonardo-161041-147832474-890245.jpg?width=1366&height=768&crop=true",
                           "https://media.cntraveler.com/photos/53da3d466dec627b149de2e5/master/pass/ritz-carlton-tokyo-tokyo-japan-108912-1.jpg"])
#The Plaza Hotel
myHotel.hotel[6].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/496718760.jpg?k=608ceb5268219094ffb5f99c00dd1b869daf59485ca2ce071c49a9bd2feeba4f&o=&hp=1",
                           "https://media.cntraveler.com/photos/62a8e975d822d883b3c26a8d/16:9/w_2560,c_limit/The%20Plaza%20NYC_6011-40-2.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/496718977.jpg?k=7f45ce8630a259d59cda121fcc23316a6c5b3c75d16c0a52146bbd9390a3585f&o=&hp=1",
                           "https://www.theplazany.com/wp-content/uploads/2016/02/RoomsSuites_LegacySuites_Carnegie_Slideshow_Feature2.jpg"])
#Mandarin Oriental
myHotel.hotel[7].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/236665735.jpg?k=4c3f6d75164608eb834404cd231958eef074346113854124f0bf1c68dc029201&o=&hp=1",
                           "https://www.lavanguardia.com/files/image_948_465/uploads/2018/04/01/5fa4354c0dda2.jpeg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/251817639.jpg?k=9b3e6ecb42df8dd5e80b2f6761ea82271d34b321535fe5d52cb42a9a45bc2852&o=&hp=1",
                           "https://media.cntraveler.com/photos/5b97dceb84c0c47ae99de3e9/16:9/w_2560,c_limit/Mandarin-Oriental,-Bangkok_2018_MOBKK-ROYAL-LIVING-ROOM.jpg"]) 
#The Dorchester
myHotel.hotel[8].imgsrc.extend(["https://media.tatler.com/photos/64491d544b0c1dd744840940/4:3/w_5976,h_4482,c_limit/JS308250%20(1).jpg",
                           "https://robbreport.com/wp-content/uploads/2023/06/The_Dorchester6.jpg?w=1000",
                           "https://secure.s.forbestravelguide.com/img/properties/the-dorchester/the-dorchester-Park-Suite.jpg",
                           "https://static.standard.co.uk/s3fs-public/thumbnails/image/2012/10/24/11/Park-lane-suite.jpg?width=1200"])
#Rosewood London
myHotel.hotel[9].imgsrc.extend(["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/1f/e4/48/rosewood-london.jpg?w=700&h=-1&s=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/420340083.jpg?k=04d74bf050cd11a30109f1c520707ac2e541e4b84cd9dc173fb5c40df9682b23&o=&hp=1",
                           "https://q-xx.bstatic.com/xdata/images/hotel/max750/43460046.jpg?k=f12050429d03cd8266afb533a717571f915e433c13cd16b49bb9d97def2161fb&o=",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/141263407.jpg?k=2f4d920900347672c9027aca35cbc32e7e97ce735186f3d83570cb91aaf9a179&o=&hp=1"]) 
#The Peninsula Paris
myHotel.hotel[10].imgsrc.extend(["https://www.peninsula.com/en/-/media/news-room/about-us/pr-company-profile.png?mw=905&hash=D2F2A2130F77BE2876FB195243EBAB2A",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/436380737.jpg?k=34b8b22a60a8fa52bdb8f0a82fb736884251024bb9819451a65b3293cd6ab525&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/524556763.jpg?k=a1913c8c5432729d184a9bb7a7844a1525d06595195c263188e7cbe33a5d4049&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/124122671.jpg?k=707eac0812a97d3cc027dc58c99bd3fc40ed2088e80f1dbabbe456d72df3ffe0&o=&hp=1"]) 
#The St. Regis New York
myHotel.hotel[11].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/448885345.jpg?k=f50b995034d7cb05dc17d3675abda48a6d7a12ed4950f74d16deb729977b6f38&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/433353216.jpg?k=946f42e18a7a4dd5fd959240282a21769c01c8064ec1015117f4122aa908c4f4&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/433353180.jpg?k=02183568644b02dd35286beb1bb344092cb380ac4c6652922a174c2d68220489&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/433353210.jpg?k=0528602c5c54b83ad64bd457e953f6c9c2bf62cfa29b042a9e4069f550b989c7&o=&hp=1"] )
#The Peninsula Shanghai
myHotel.hotel[12].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/28038346.jpg?k=2c2ef551dcfbb04a603bed1ceed4e056616e7d988d67a5719003cdc61ac8bb8a&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/33960256.jpg?k=d87bd38c71a1f9210163ae24463833c156a1c43339e0053536081ee135746e60&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/33960683.jpg?k=c669825e19b9174e0d39b0cb0dd5c7bea439cf85c7b3204836ee7c1970072f4c&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/20391965.jpg?k=43c4847359acc3cb2fd222a5b0fc14c8e352812c89de4342c2a3ec55a20c5003&o=&hp=1"]) 
#Hotel Eden - Dorchester Collection
myHotel.hotel[13].imgsrc.extend(["https://www.familyvacationcritic.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/sites/19/2014/08/hotel-eden.jpg.webp",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/304829818.jpg?k=fe21164c2412fefcbeb550f000c8bcecb64c36e6868610bb1cfaf52660af087c&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/304829193.jpg?k=29d333a428a39554403c6e5620bbb7768ebdd9260a9a9bac610dda5abcc973c3&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/321866220.jpg?k=449c6e86884db6c72c882e8aa6b2d0970efe14f2a9dc819e8f9e42676459d8c3&o=&hp=1"] )
#J.K. Place Roma
myHotel.hotel[14].imgsrc.extend(["https://elitevoyage.com/wp-content/uploads/2021/12/JK-Place-Roma-01.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/377016592.jpg?k=3b65ff61fb2e648aebad66ea398c8c50da1b607df4c4aabbf5009674f0362ec9&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/375343237.jpg?k=7b8737088c48dd40984b52b8dcaab0d2cdbcd84937a189c226fc2e2856f378c1&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/377016585.jpg?k=27d737ff47789008b91148e06f2eda57e49560bae94f02103ae8eef829e8df88&o=&hp=1"] )
#Bangkok Marriott Marquis Queen's Park
myHotel.hotel[15].imgsrc.extend(["https://photos.book5star.com/photos/7637/570b75b4_z.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/480982302.jpg?k=04c23d33aa4a20cc4f2ddb38bc4d5fa2a1a37b2620717f7eb8ca98442a55f644&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/426578442.jpg?k=17db93c6682b43b6d49121ddf431b81b83951e769922432aed3ff0d9cee27948&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/480982205.jpg?k=f68218a9e5687ddb470a53b77e96b61aca1fec5ca187469533d3eab9cf4b6d7c&o=&hp=1"]) 
#Risonare Tomamu
myHotel.hotel[16].imgsrc.extend(["https://media.hoshinoresorts.com/image/authenticated/s--LHIGtg7p--/c_fill,g_auto,h_630,w_1200/f_auto,q_auto/v1666159739/RISONARE_Tomamu_view_2_m5qxth.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/511674778.jpg?k=0dd4645247bc61061a86e351de1bfa62f1c3561f6bcc76c56c9b5fe294faa292&o=&hp=1",
                           "https://japansnowaccommodation.com/images/krgallery/251/suite_room__2_.jpg",
                           "https://images.trvl-media.com/lodging/10000000/9630000/9622100/9622080/dce6f979.jpg?impolicy=fcrop&w=608&h=342&p=0.5&q=mediumHigh"] )
#Conservatorium Hotel
myHotel.hotel[17].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/327045690.jpg?k=f2b656d53aa8f89680eaa23a2ea2745e7d702267dfb8a1b73613780c0b55d1c7&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/327045511.jpg?k=366ff71672cba802ce05b8f8b0f053773c6e52761002f87da685957f63f6ca0d&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/327045717.jpg?k=6c34164104404111ef0794e3b1fc37ece374386851b78096ff588316373e77f6&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/327064919.jpg?k=37aa6dac93dee66442fba00552555d5993a59942c6c52b1903b7592380947189&o=&hp=1"]) 
#Andaz Amsterdam Prinsengracht
myHotel.hotel[18].imgsrc.extend(["https://media-cdn.tripadvisor.com/media/photo-s/24/ff/6e/da/exterior.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/531075771.jpg?k=cad5d43010ad9ee929f464daa040556c4458294e032b53efd91d927851231967&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/270115231.jpg?k=88a509010719a8dfb530c0232476da12c1ba660b26edd8c1f3c24dbca97a593c&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/157745302.jpg?k=2e8c015f686df4f531fceae932b31c1662304495e396288d82bc4eb1fadc9795&o=&hp=1"] )
#Lotte Hotel World
myHotel.hotel[19].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/438919662.jpg?k=1c7a6305bb1bf385cbdd08b9340bbecbb2c0f92a9286a0ced6f925b863add0a0&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/301779580.jpg?k=c831c5541996b9c7fa64154ee35f787eb15e4a33c959794ff006afaabf3e65e6&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/468908467.jpg?k=f0e0ac4a2c0682ad42133debe6b26e36f067caada01856b52856ebdeac908f51&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/305099580.jpg?k=eb8eb35e18954c30b00d3d8c8530e5d4528474c5d24711b4b33d8fa0ae38c4d5&o=&hp=1"]) 
#Shilla Stay Gwanghwamun
myHotel.hotel[20].imgsrc.extend(["https://cdn.shopify.com/s/files/1/0609/9376/5551/files/shilla-stay-gwanghwamun-seoul-hotel_1.jpg?v=1681792775",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/148119794.jpg?k=2c4c765fc6be81d7eb40e5664c54de3609b8224c57d1b0a18646a986b482a399&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/317253661.jpg?k=77cc3af2941977e3ce9cbd8adc5bc40ff7acc77693590ea2c35541da05e5f05e&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/250396822.jpg?k=6d79c3f63038f21846f3b2f8231690ade4c79aa4d6ad801cd156ccec6bd5b3c4&o=&hp=1"]) 
#The Westin Josun Seoul
myHotel.hotel[21].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/430818518.jpg?k=d664a3e098c2f9a5804edfb3822eda94c58437527b61e274d1b00b9bb85bf964&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/430818659.jpg?k=e3a0ca8ac8bc955da04f451b0d5e7c2b4247832161423d82d67f11c7c293c562&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/437056380.jpg?k=d05713ad51ca39f1dc9df32e6bad2a96ac76b33c37f23c304052cc7570550feb&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/430818535.jpg?k=79f7efa60959c97ad0af0624a548153dfc165d3842bcd0aedc073df6e7599875&o=&hp=1"]) 
#Hotel de Russie
myHotel.hotel[22].imgsrc.extend(["https://cdn.audleytravel.com/1050/750/79/15973672-hotel-de-russie-rome.webp",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/49755495.jpg?k=542c82baa098a36651cf62c52d56990621dbcafc54fdbd798e4368af00892241&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/49754398.jpg?k=c616593725f2f974ba946041a8d570ba0175413119fcc620574696ad93d47525&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/406413930.jpg?k=cf25a288a3ad37c3c8070c7d12899a886109c2573bcfa71993c93104741c9df5&o=&hp=1"]) 
#Niseko Hilton Village
myHotel.hotel[23].imgsrc.extend(["https://x.cdrst.com/foto/hotel-sf/1839c/granderesp/hilton-niseko-village-general-c175fb1.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/483828304.jpg?k=f387cce53a1166f1f4aae274578c34783dba0645958c66fc995c12da9f84569d&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/483828243.jpg?k=0f7c287fa46894e21e4969e0b1de2dd677f88b6e0c599a3041d0e25d3484ee62&o=&hp=1",
                           "https://cdn.jalan.jp/jalan/images/pict3L/Y3/Y300063/Y300063194.jpg"]) 
#Kantary Hills Hotel
myHotel.hotel[24].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/508072977.jpg?k=0199901d336955a2ec6a0752caeed2b59c21b3e960e861ba7b01a97808d615b0&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/135699205.jpg?k=71095b1d0b14ec3549301c8f0b6051f6d66f274c84bd3fb7c3ec1a92f7729e3e&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/508072945.jpg?k=e569e358ad5a99e4e7a187044d4faff1f0c5446870c5e2d949a417322ced4208&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/508072944.jpg?k=9caa6dd953eafc739f23c454c10bc281b40627b7ec90778f96c19d5b9d5fa8f4&o=&hp=1"]) 
#Rachamankha
myHotel.hotel[25].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/454322057.jpg?k=2cdf6ff5c1a8e6b782e8b98d9416361ff3283cc12fed4a234c4bcb74f2fb7270&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/209036784.jpg?k=e342062b2b157f35f77a6ef29e461fde938a5b3ed179a151b2675204adfb14d9&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/153918943.jpg?k=802be527849e4d77f8a8f3c7e28c5a5d76915f33fdfcba25d3764ca3c8e9931b&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/454322433.jpg?k=398889168d0ebc342962f41409350fec82dafe6df2ec44829e085a268a2c019e&o=&hp=1"]) 
#Paradise Hotel Busan
myHotel.hotel[26].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/89438720.jpg?k=c41f47656a1fc5c286f42bf37186b2d7ba36edeb43574bd599c385463e79ffa2&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/92178621.jpg?k=772446081db3779bcc6deb3f7ca4ce07a8e6c3dda0ae55fd62a3babfdd05c2b8&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/105912330.jpg?k=b0b5427942cec8eab7338887a43597411b8466021c7fba224b7611aef5e00599&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/33959835.jpg?k=3988992a9ba07b39935be2379da21ee851a1a2da5040a122138ad6004d9b5c7d&o=&hp=1"]) 
#The Langham Huntington, Pasadena
myHotel.hotel[27].imgsrc.extend(["https://assets.langhamhotels.com/is/image/langhamhotelsstage/tllax-plan-HSG_Event2:Large?wid=1350&hei=900",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/134509684.jpg?k=aecdce3b69300274f903e8a03bcbbb4bd3ad055b45cc60a0edbe17255820d08a&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/134507464.jpg?k=ad37aaa3a7ba3bbb6d01e4fa2b2e126ce62b7ec12655cf8ff40f17fedcf3306b&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/158924949.jpg?k=6b9ff2b7d161caeec155e5c61547847de74236cafa54b204a8ffc32b09dfedb5&o=&hp=1"]) 
#The Beverly Hills Hotel
myHotel.hotel[28].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/325188952.jpg?k=da945dbf1adaf47bbf9152e515bda19fed5de7abad5c53a137b01db68b991b12&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/228775896.jpg?k=31bb496faf2aead5495241dab5d9976deb002fc12edfb67bf4d481b8b64b3490&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/23601196.jpg?k=8b28c128d80197b54f49e9139409ee4c31149b4cfa9c21aeca6dc8dc49ee60b8&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/179060733.jpg?k=68199d7d7d58ab64af2f4c4e0f7ea7cffc9dfd9a8ed5994f2db29dddbac137e4&o=&hp=1"]) 
#Park Hyatt Sydney
myHotel.hotel[29].imgsrc.extend(["https://globeinfinite.com/wp-content/uploads/2023/07/Park-Hyatt-Sydney.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/481509584.jpg?k=10bd4835baded6f52a5f44b9f00aa679379700135faf65b84254b8bb8c37256b&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/481509527.jpg?k=6be8920fd3e97936f7c2c28c1dcc78c5209b2c3627b79201d84361baebd6e824&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/481509597.jpg?k=21beb580b37e3dcb54928e28d7956670b23a61638bb2f789860cb79511dfab44&o=&hp=1"]) 
#The Langham, Melbourne
myHotel.hotel[30].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/344650950.jpg?k=f4ba1b49a6235b525d2e4fb8b2eab61691f37a656b6ee8d31ea71710991dea9c&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/529897823.jpg?k=563ddd2b7364cd21cf3d230b7bf0317554633643eb6fcc3961c947ccaeee1010&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/344655260.jpg?k=e235b0ba0b0bb41fe433c1b2774d2afe195992476c38b46da93487e3771eb005&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/344652917.jpg?k=b4c0c34d06d22737b597e65633a4cb59ddeae2b9b2dfe1c79401547e3c90bd12&o=&hp=1"]) 
#Victoria Xiengthong Palace
myHotel.hotel[31].imgsrc.extend(["https://waybird.imgix.net/lodge_images/images/000/084/659/original/288-big.jpg?w=1400&h=960",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/475506259.jpg?k=2c444327e7e44ba392f0b32e6304dfabf36cc76b1b061805b5ee733de04f2541&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/476264720.jpg?k=7810ef883bbcb57e3a6960d22d7ed3769a09310c42fd6e2faa803a61e8e52e39&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/476265168.jpg?k=8bdaa88e75dfbcfa2fabaccce47e8677e797a71666d84327337e9ce81a477fed&o=&hp=1"]) 
#Pullman Luang Prabang
myHotel.hotel[32].imgsrc.extend(["https://www.ahstatic.com/photos/9112_ho_03_p_1024x768.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/251953314.jpg?k=df52af69f5f0dfdad18555b40986261b63024e6586a0cf727e62a12442d946e4&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/251953318.jpg?k=a6273e300b4de6c4a081af95533f7585802385197613a3d3325d6479c9c6db4f&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/251953337.jpg?k=e2a8a7aadbf135ca014c37333ba6c9a79bc1a8dbb259f24198cca0554039d060&o=&hp=1"] )
#Amantaka
myHotel.hotel[33].imgsrc.extend(["https://amantaka-hotel-luang-prabang.hotelmix.co.th/data/Photos/OriginalPhoto/11128/1112803/1112803884/Amantaka-Resort-Luang-Prabang-Exterior.JPEG",
                           "https://amantaka-hotel-luang-prabang.hotelmix.co.th/data/Photos/OriginalPhoto/772/77212/77212469/Amantaka-Resort-Luang-Prabang-Exterior.JPEG",
                           "https://www.aman.com/sites/default/files/styles/full_size_extra_large/public/2021-03/Amantaka_Dining-Hero-1.jpg",
                           "https://amantaka-hotel-luang-prabang.hotelmix.co.th/data/Photos/OriginalPhoto/772/77212/77212478/Amantaka-Resort-Luang-Prabang-Exterior.JPEG"]) 
#Kiridara Luang Prabang
myHotel.hotel[34].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/55548003.jpg?k=c081c488394520e2b07413f18929ee45a005e0b407c0213c99634da2cfc504c2&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/140170580.jpg?k=592c17d505f21974d78a9f220e991d5bdb59a55766d93e1c5a9c5904a70cf3de&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/140172035.jpg?k=7edd60ea0bb3c20edf063a71135eb2160bb03adde113fcf806bb106fdc29823d&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/140179107.jpg?k=aff1b41fef4fbee4c961c210d458d242153a5764a0628a9df8b2414d93d613da&o=&hp=1"]) 
#TIME Moonstone Hotel Apartments
myHotel.hotel[35].imgsrc.extend(["https://dnagw5kmh987u.cloudfront.net/www.timehotels.com-1785599525/cms/cache/v2/62396e761b420.jpg/1200x630/fit/80/8c92825b98628317df5a6d9003b78227.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/363364446.jpg?k=c7471827eca1e34677ad63735963691a308aefd999d7ac0d60074254fc26a8eb&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/363365684.jpg?k=ddfa8897fdee94db5a64287b08a7277bfd2a590be04a3011aa0af2cc62983a70&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/363368286.jpg?k=7af6fb18f0ac237e6c8a8d7308e9be94ea53c6abae8bf761bda6e577b49d8749&o=&hp=1"]) 
#Arthotel Munich
myHotel.hotel[36].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/125638208.jpg?k=fa8f9c473c4ca82a70ae27e7226ff96b96180d2725dee118395128b65a868563&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/64375688.jpg?k=db51598fc77acf5b79613e42cdda6d673a1403787b95aa387874c43b1ff5c2c1&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/84231966.jpg?k=a9456cb41f79c0e6b87fcf2ef9bbd8793fd90cb3f6662631425a2f744f0bb156&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/126068056.jpg?k=199cf7fadbb7beb241fabd5a29db728abb89c69dd14896f71e36c8651285ec54&o=&hp=1"]) 
#Boutique Hotel Atrium Munchen
myHotel.hotel[37].imgsrc.extend(["https://media-cdn.holidaycheck.com/w_768,h_432,c_fill,q_auto,f_auto/ugc/images/410c7c98-18cb-4af1-9134-3cb401df03d3",
                           "https://www.atrium-hotel.de/wp-content/uploads/2020/07/Twin_Boutique-Hotel-Atrium-Muenchen-575x380.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/527007335.jpg?k=2f6749d89a6643c4f17378088691328c1aa12380d05525bdb9c73a254128b926&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/247618466.jpg?k=fae4f9c14feb56c7d4e2636f296ab511633ca4b863681fccf41ef74c26895162&o=&hp=1"]) 
#Copthorne Hotel
myHotel.hotel[38].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/15434570.jpg?k=7edccefa4a2081ec34c62dcc538fbc058f322a17c7ee559048168d1022525527&o=&hp=1",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/2e/7e/7a/superior-twin.jpg?w=1200&h=-1&s=1",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/f0/06/69/copthorne-hotel-and-resort.jpg?w=1200&h=-1&s=1",
                           "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/19/5c/80/scenary-from-our-room.jpg?w=1200&h=-1&s=1"]) 
#Heartland Hotel
myHotel.hotel[39].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/10589621.jpg?k=5a918606f2768c93319d98e53a20054d163d8c8b852e7f7dea8892da3a7f9994&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/10589622.jpg?k=5ef66e3449f461c0289a38f68ccc79a4ceaf2819b5aaa631ccce0e73d673cb45&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/238306157.jpg?k=09c331401d9785d10b0db5519dfbadf070390b4b2847ca8d894879cc503c46df&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/10589619.jpg?k=0bcbbd23cab7da9f88be3f85e93c81249da83ed35e6e78fad636521ddcb202e2&o=&hp=1"]) 
#mi-pad
myHotel.hotel[40].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/296975843.jpg?k=17e967a673d2ae164aa7b4f37a4c3635ec107d7d9b0298ab6c808e5846329ff6&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/322995762.jpg?k=3bda06eb85e5a36fc75965394ef7291e40d02d109c9aaf2af6a296ed3032daad&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/146498738.jpg?k=4f48ebe1c96e96c19d0a90a2edf54a5d6e062feb0a710e791b296939e86754d1&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/146498753.jpg?k=909d2bc058c069f1ab46e61cb34e3e676bf4064c49ea30610f81089b100dc22e&o=&hp=1"]) 
#Hotel Guillen Jr
myHotel.hotel[41].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/124546360.jpg?k=c249e9790ffe2aefb0a2ae71e3780c2bcd55d23dfb734a792d6a8151255f0898&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/124458996.jpg?k=376cc593869ff6d27b82db7a9093dc54ecbc7e63f3710793b54eb28dc48661a7&o=&hp=1",
                           "https://guillen-jr.gettijuanahotels.com/data/Pictures/OriginalPhoto/5375/537547/537547227/picture-tijuana-hotel-guillen-jr-30.JPEG",
                           "https://images.trvl-media.com/lodging/26000000/25110000/25108400/25108324/f4dfd759.jpg?impolicy=resizecrop&rw=1200&ra=fit"]) 
#Baja Inn Hoteles La Mesa
myHotel.hotel[42].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/457312932.jpg?k=80869fc1eb2133d60dd6387ad30b9a922945edc85d7682d01f85ae76c23cd7cc&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/378026288.jpg?k=f4fb14a5b56a203ad5f3b76203acbae48456116b7ed7823672e6fc7d32257c12&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/457312932.jpg?k=80869fc1eb2133d60dd6387ad30b9a922945edc85d7682d01f85ae76c23cd7cc&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/161046478.jpg?k=d8bb9328cd66db2a5518b00ac1a20839b08fab1dd2b7dadca7609dcdfcec83f4&o=&hp=1"]) 
#Kabayan Hotel Pasay
myHotel.hotel[43].imgsrc.extend(["https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/420522486.jpg?k=16bbc9aa1726e669731a54f3f5ffbac03ce65c32a0064638e2f496b1012f90f8&o=",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/438552553.jpg?k=eb20bb948dd92559d12c07258389b7d502c068e9fa723b2854cd9fae1e6232cc&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/408959025.jpg?k=2d691677f18d07ab3d8c8c464f709b2c577358d37e7622bf6a2418e93377fc77&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/409145322.jpg?k=7d7850bf4334a929c7363fea49b6b660c5395713f0fa8ad58d94c538d2639a5d&o=&hp=1"]) 
#Radisson Blu Royal Viking Hotel
myHotel.hotel[44].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max500/277542505.jpg?k=18f7aeed0bc22fe83e1bb08c6ac67ed7774df6915e1bb458e354426d60dea862&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/481441225.jpg?k=54983c83bd9cf931e7dcb5d05928d0750f0ba3cbf57dafc07828a50c79bc49f1&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1280x900/460334529.jpg?k=2ebbffe0b94b0de9775b0e9e036c33181472972bc16019184673a5e374bf3c6e&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/481441375.jpg?k=b70f62367c0df1364a3332333d80a97544a614c22e948d7c5d7abda561c712b1&o=&hp=1"]) 
#Thon Partner Hotel Kungsbron
myHotel.hotel[45].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/51103894.jpg?k=c532ee256332c9e5c8e6eaf022bc56da4407147428f60ba6c028ab588753722a&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/354691754.jpg?k=16af94ad809313970eb6dceabc88e5471eabba31afe7f0c35594dd26b4df746d&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/354691747.jpg?k=84c1515cdaa85baad0ed5d5c905899ce1d1fee6ff585f1b548fa5446e4f99c8e&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/landmark/max1024/187348.webp?k=76f3735cc5ce4e024e947da91ab142a858bb422ddec60c2123b1be0426af00a3&o="]) 
#Clarion Hotel Amaranten
myHotel.hotel[46].imgsrc.extend(["https://cf.bstatic.com/xdata/images/hotel/max1024x768/26545057.jpg?k=945e3578bfe29a1bb0eeb2524cf40dd535aeb87cde6dd06db1eb5f6a2c1d79af&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/468250227.jpg?k=8bfbeab98e5b13686053c4da4545b90241a7cb37b53bd37c50882fd62ed93f8f&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/240920448.jpg?k=4dafde40a8dfe908a53f8a9048ed6182ba0168d23a7ed04f11f38663f5df3a6b&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/199889644.jpg?k=468bb3951f52643b0a8edaeb3a1fb71a7fc82221ffd6bd2f6949c7690b6e33a7&o=&hp=1"]) 
#Clarion Hotel Sign
myHotel.hotel[47].imgsrc.extend(["https://www.delegia.com/app/Data/ProjectImages/14020/Cropped/clarionSign-1024x570.jpg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/144326372.jpg?k=52f78910973af0c6d040411af3117d55ce06a8c2279c45d89c289ffa78dd7b02&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/144326272.jpg?k=354470ee4839e7cf0820700c48547249fb9167ddd5e983da0d0be5c5993f91b6&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/144326330.jpg?k=c5476e4defa294185eceb8610001771355b4d01448fe680bb9213f72607315da&o=&hp=1"]) 
#Riu Plaza España
myHotel.hotel[48].imgsrc.extend(["https://cdn0.bodas.net/tour3d/3768/3_2/960/jpg/3768_134731.jpeg",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/207314225.jpg?k=0f1478b0b65a2339ba5e868dc9b5f1771e0b977a284e6a5cef0e4cb6be6d8493&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/217566747.jpg?k=246d9766dcdcee6ad1cf4ed5687daa4f5ca7673f93fb674fc6fc30a0b3518f6a&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/332290075.jpg?k=334e1cd68afb5382ccfc8e3fab0d59961e74d3bc80dbceb7d7869cdfb095ecf1&o=&hp=1"]) 
#Ilunion Alcalá Norte
myHotel.hotel[49].imgsrc.extend(["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/75/68/f9/fachada.jpg?w=700&h=-1&s=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/68816013.jpg?k=1e6e478a5f03ba23a40b2d6dadae963c09da17c2365706ede91dbd2308837115&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/227872404.jpg?k=64b5c6ceff84c3dbd05f9af530fbdffc116755fe5015ee02a75bf0d8a817e58b&o=&hp=1",
                           "https://cf.bstatic.com/xdata/images/hotel/max1024x768/81814915.jpg?k=203261f08aaf8eaab1a4d74698927b33cd0ed8655c7ee8c9b91ae121ae094996&o=&hp=1"]) 

for hotel in myHotel.hotel:
    for i in range(3):
        hotel.room = main.Room("Single Bed", 1000, 1)
    for j in range(3):
        hotel.room = main.Room("Double Bed", 1500, 2)
    for k in range(2):
        hotel.room = main.Room("Queen Size Bed", 2500, 3)
    for l in range(2):
        hotel.room = main.Room("King Size Bed", 4000, 4)


for i in range(10):
    myHotel.hotel[i].feedback = main.Feedback("namthip","Best Hotel",5,datetime.date(2021,2,7))
for j in range(10,20,1):
    myHotel.hotel[j].feedback = main.Feedback("john","Decent Hotel",4,datetime.date(2020,12,7))
for k in range(20,30,1):
    myHotel.hotel[k].feedback = main.Feedback("Boggac","Ok Hotel",3,datetime.date(2021,5,17))
for l in range(30,40,1):
    myHotel.hotel[l].feedback = main.Feedback("namthip","Not Good",2,datetime.date(2019,4,24))
for m in range(40,50,1):
    myHotel.hotel[m].feedback = main.Feedback("Loventa","Worst Hotel",1,datetime.date(2023,5,19))

# myHotel.hotel[0].room = main.Room("Breakfast not included", 500, 1)
# myHotel.hotel[1].room = main.Room("Breakfast included", 1000, 2)
# myHotel.hotel[2].room = main.Room("Don't smoke", 1200, 3)
# myHotel.hotel[3].room = main.Room("Beautiful view", 1500, 2)
# myHotel.hotel[4].room = main.Room("Poolside bar", 2500, 4)
# myHotel.hotel[5].room = main.Room("Private pool", 4000, 6)
# myHotel.hotel[6].room = main.Room("There is wifi", 5000, 2)

myHotel.hotel[0].room[0].reservation = main.Reservation("namthip", datetime.date(2023, 1, 1), datetime.date(2023, 1, 5))
myHotel.hotel[0].room[0].reservation = main.Reservation("john", datetime.date(2023, 1, 6), datetime.date(2023, 1, 8))
myHotel.hotel[3].room[0].reservation = main.Reservation("jack", datetime.date(2023, 1, 4), datetime.date(2023, 1, 7))
 

myHotel.user = main.User("user1", "1111", "0816228411", "one@gmail.com","customer")
myHotel.user = main.User("user2", "2222", "0816228411", "two@gmail.com","customer")
myHotel.user = main.User("user3", "3333", "0816228411", "tree@gmail.com","customer")
myHotel.user = main.User("Admin1","1234admin","000000000","admin@gmail.com","admin")

feedback1 = main.Feedback(myHotel.user[0], "Great Hotel!", 4, "2024-02-21")
feedback2 = main.Feedback(myHotel.user[1], "Worst Hotel I've ever stayed", 1, "2023-11-09")
feedback3 = main.Feedback(myHotel.user[2], "Nice service!", 5, "2024-07-02")

myHotel.current_user = myHotel.user[0]
myHotel.create_reservation(1, "Single Bed", "11-10-2023", "15-10-2023")
myHotel.add_payment(4)
myHotel.create_reservation(2, "Double Bed", "1-12-2023", "9-12-2023")
myHotel.add_payment(5)
myHotel.current_user = None
