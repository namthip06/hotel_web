const api = "http://127.0.0.1:8000";

async function current_user(){
    const userresponse = await fetch(`${api}/currentuser`); // Fetch data from '/hotel' endpoint
    const userdata = await userresponse.json(); // Parse the JSON response
    
    document.getElementById("name").textContent = userdata['_User__name'];
    document.getElementById("email").textContent = userdata['_User__email'];

    const booking_list = document.getElementById("account-booking-list");
    booking_list.innerHTML = ''; //Clear shit inside
    for(reservations of userdata['_User__reservation']){
        const booking = document.createElement('div');
        booking.classList.add('col');
        booking.innerHTML =
        `
        <div class="d-flex justify-content-between align-items-center">
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
}
current_user();
