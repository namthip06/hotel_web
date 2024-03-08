const api = "http://127.0.0.1:8000";

document.addEventListener('DOMContentLoaded', function () {
  let hotel_name = JSON.parse(localStorage.getItem('lode_hotel_name'));
  let head_name = document.getElementById("head_name");
  let head_location = document.getElementById("head_location");
  let result_available_room = document.getElementById("result_available_room");
  let result_other_accommodation = document.getElementById("result_other_accommodation");
  let other_link = document.getElementById("other_link");
  let review_count = document.getElementById("review_count");
  let result_review = document.getElementById("result_review");
  let data = detail_backend(hotel_name);
  let text = "";

  head_name.innerHTML = hotel_name;
  data.then(function(data) {
    head_location.innerHTML = data['Hotel']['location'];
    // aviable rooms
    let rooms = data['Hotel']['available room'];
    for (let i = 0; i < rooms.length; i++) {
      text += `
        <div class="col py-5 border-bottom border-secondary-subtle">
            <div class="row gx-lg-5">
                <div class="col-auto">
                    <div class="bg-image-full" style="width: 300px; height: 200px; background-image: url(https://picsum.photos/300/200);"></div>
                </div>
                <div class="col-auto me-auto mt-lg-0 mt-4">
                    <h4 class="hotel_name mb-3 text-uppercase">${rooms[i]['detail']}</h4>
                    <div class="d-flex align-items-center mb-2">
                        <h5 class="m-0 me-3"><i class="bi bi-building"></i></h5>
                        <p class="m-0 text-capitalize text-body-secondary">1 bed</p>
                        <h5 class="m-0 ms-5 me-3"><i class="bi bi-person"></i></h5>
                        <p class="m-0 text-capitalize text-body-secondary">${rooms[i]['guests']} guests</p>
                    </div>
                </div>
                <div class="col-auto align-self-end text-end">
                    <p class="m-0 mb-1 text-body-secondary text-decoration-line-through">THB 1500.00</p>
                    <h4 class="mb-3 fw-bolder">THB ${rooms[i]['price']}</h4>
                    <button type="button" class="btn btn-dark fw-bold" style="width: 200px;" onclick="bookingHotel()">Book Now</button>
                </div>
            </div>
        </div>
      `;
    };
    result_available_room.innerHTML = text;
    text = "";
    // other accommodation
    for (let i = 0; i < data['Recommend nearby hotels'].length; i++) {
      let hotel = data['Recommend nearby hotels'][i];
      let rating = "";
      for (let i = 0; i < hotel['rating']; i++) {
        rating += `<i class="bi bi-star"></i>`
      };
      text += `
        <div class="card mb-4 me-lg-5 me-1 shadow-sm" style="width: 15rem;" onclick="submitHotel('${hotel['name']}')">
          <img src="https://picsum.photos/300/200" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title text-capitalize mb-1 fw-bold">${hotel['name']}</h5>
            <div class="d-flex mb-1">
                ${rating}
            </div>
            <div class="d-flex">
                <p class="m-0 me-1"><i class="bi bi-geo-alt"></i></p>
                <p class="text-body-secondary">${hotel['location']}</p>
            </div>
            <p class="m-0 text-body-secondary text-decoration-line-through"><small>THB 1500.00</small></p>
            <p class="fw-semibold">THB ${hotel['price']}</p>
          </div>
        </div>
      `;
    };
    result_other_accommodation.innerHTML = text;
    text = "";
    other_link.innerHTML = `<a href="#" class="a-black pb-1">See Other Accommodations in ${data['Hotel']['location']}</a>`;
    // reviews
    let feedback = data['Hotel']['feedback'];
    review_count.innerHTML = `<small>${feedback.length} verified reviews</small>`
    for (let i = 0; i < feedback.length; i++) {
      text += `
        <div class="col py-3 border-bottom border-secondary-subtle">
            <div class="row mt-2">
                <div class="col-auto mx-3">
                    <img src="https://picsum.photos/80/80" class="rounded-circle" alt="">
                </div>
                <div class="col">
                    <div class="d-flex flex-column">
                        <div class="d-flex">
                            <p class="m-0 pe-3 me-3 border-end border-secondary-subtle fw-bold">${feedback[i]['rating']}.0 Amazing</p>
                            <p class="m-0 text-secondary text-capitalize">${feedback[i]['user']}</p>
                        </div>
                        <p class="m-0 my-1 text-secondary">${feedback[i]['time']}</p>
                        <p>${feedback[i]['comment']}</p>
                    </div>
                </div>
            </div>
        </div>
      `;
    };
    result_review.innerHTML = text;
  });
});

function submitHotel(hotel_name) {
  localStorage.setItem('lode_hotel_name', JSON.stringify(hotel_name));
  document.location.href = "detail.html";
}

function bookingHotel() {
  document.location.href = "contact.html";
}

async function detail_backend(hotel_name){
  let response = await fetch(`${api}/hotel?name=${hotel_name.replaceAll(' ', '%20')}`);
  let data = await response.json();
  return data
}