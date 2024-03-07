const api = "http://127.0.0.1:8000";

const logout_button = document.getElementById("logout-button");
const nav_login = document.getElementById("nav-login");
const nav_signup = document.getElementById("nav-signup");

async function current_user(){
    const userresponse = await fetch(`${api}/currentuser`); // Fetch data from '/hotel' endpoint
    const userdata = await userresponse.json(); // Parse the JSON response
    
    if(userdata !== null){
        document.getElementById("name").textContent = userdata['_User__name'];
        document.getElementById("email").textContent = userdata['_User__email'];
    
        const booking_list = document.getElementById("account-booking-list");
        booking_list.innerHTML = ''; //Clear shit inside
        for(reservations of userdata['_User__reservation']){
            const booking = document.createElement('div');
            booking.classList.add('col');
            booking.innerHTML =
            `
            <div class="d-flex justify-content-between align-items-center my-3">
                <div class="d-lg-flex align-items-center">
                    <img src="https://picsum.photos/180/120" alt="hotel_picture">
                    <div class="mx-lg-5 mt-lg-0 mt-4">
                        <p class="m-0">check in</p>
                        <h5 class="m-0" id="checkin">${reservations['_Reservation__date_in']}</h5>
                    </div>
                    <div class="pe-5 me-5 mt-lg-0 mt-4 border-end border-secondary-subtle">
                        <p class="m-0">check out</p>
                        <h5 class="m-0" id="checkout">${reservations['_Reservation__date_out']}</h5>
                    </div>
                    <div class="mt-lg-0 mt-4">
                        <p class="m-0">on time</p>
                        <p class="m-0" id="hotel">${reservations['_Reservation__hotel_id']}</p>
                        <p class="m-0" id="room">${reservations['_Reservation__room_detail']}</p>
                    </div>
                </div>
                <div>
                    <button type="button" class="btn btn-outline-dark me-3"><i class="bi bi-wrench-adjustable me-2"></i>Change</button>
                    <button type="button" class="btn btn-dark"><i class="bi bi-x-lg me-2"></i>Cancel</button>
                </div>
            </div>
            `
            booking_list.appendChild(booking);
        }
    } else{
        document.getElementById("name").textContent = 'Guest';
        document.getElementById("email").textContent = "You're not logged in!";
    
        const booking_list = document.getElementById("account-booking-list");
        booking_list.innerHTML = ''; //Clear shit inside
    }
}

async function log_out(){
    const userresponse = await fetch(`${api}/logout`); // Fetch data from '/hotel' endpoint
    if(userresponse.ok) { // Check for successful logout
        document.getElementById("name").textContent = 'Guest'; // Clear user name
        document.getElementById("email").textContent = "You're not logged in!"; // Clear user email
        const bookingList = document.getElementById("account-booking-list");
        bookingList.innerHTML = ""; // Clear booking list container

        logout_button.textContent = "Login";
        logout_button.removeEventListener("click", log_out);  // Remove logout listener
        logout_button.addEventListener("click", login_redirect);

      } else {
        // Handle logout error
        console.error("Error logging out!");
      }
}

async function login_redirect(){
    const userresponse = await fetch(`${api}/currentuser`); // Fetch data from '/hotel' endpoint
    const userdata = await userresponse.json(); // Parse the JSON response
    if(userdata == null){
    window.location.href = "login.html"
    }
}

logout_button.addEventListener("click", log_out);
nav_login.addEventListener("click", login_redirect)
current_user();
console.log(current_user.userdata)
