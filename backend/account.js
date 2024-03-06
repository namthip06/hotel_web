const api = "http://127.0.0.1:8000";

async function currentuser(){
    const userresponse = await fetch(`${api}/currentuser`); // Fetch data from '/hotel' endpoint
    const userdata = await userresponse.json(); // Parse the JSON response
}

async function userinfo(){
    document.getElementById("name").textContent = userdata._User__name;
    document.getElementById("email").textContent = userdata._User__email;
}

async function bookinglist(){
    const booking_list = document.getElementById("account-booking-list");
    booking_list.innerHTML = "" //Clear shit inside

    for (const reservation of userdata._User__reservation){
        booking_list.innerHTML +=
        
    }
}
currentuser();
userinfo();
bookinglist();