const api = "http://127.0.0.1:8000";

document.addEventListener('DOMContentLoaded', function () {
    let start = JSON.parse(localStorage.getItem('lode_start'));
    let end = JSON.parse(localStorage.getItem('lode_end'));
    let location = JSON.parse(localStorage.getItem('lode_location'));
    let guests = JSON.parse(localStorage.getItem('lode_guests'));
    data = search_backend(start, end, guests, location, "", "0-100000", "0-1-2-3-4-5")
    search_hotel(data)
});

async function search_backend(start, end, guest, country, city, price, rating){
    let response = await fetch(`${api}/search/?start=${start}&end=${end}&guest=${guest}&country=${country}&city=${city}&price=${price}&rating=${rating}`);
    let data = await response.json();
    return data
}

function search_hotel(data) {
    let result = document.getElementById("result_search_hotel");
    let count_result = document.getElementById("count_result");
    let text = "";
    let count = 0;
    data.then(function(data) {
        Object.keys(data).forEach(function(key) {
            let rating = "";
            for (let i = 0; i < data[key]['Rating']; i++) {
                rating += `
                <h5 class="m-0 me-1"><i class="bi bi-star"></i></h5>
                `
            }
            count++
            text += `
                <div class="row gx-lg-5 py-5 border-bottom border-secondary-subtle" onclick="submitHotel('${key}')">
                    <div class="col-auto mx-4" style="width: 300px; height: 200px; background-image: url(https://picsum.photos/300/200);" ></div>
                    <div class="col-auto me-auto mt-lg-0 mt-4">
                        <h4 class="hotel_name mb-3 text-uppercase">${key}</h4>
                        <div class="d-flex align-items-center mb-2">
                            ${rating}
                        </div>
                        <div class="d-flex align-items-center mb-2">
                            <h5 class="m-0 me-3"><i class="bi bi-geo-alt"></i></h5>
                            <p class="m-0 text-capitalize text-body-secondary">${data[key]['Location']}</p>
                        </div>
                    </div>
                    <div class="col-auto align-self-end text-end">
                        <p class="m-0 mb-1 text-body-secondary text-decoration-line-through">THB ${data[key]['Price']}</p>
                        <h4 class="mb-3 fw-bolder">THB ${data[key]['Price']}</h4>
                        <button type="button" class="btn btn-dark fw-bold book_btn">Book Now</button>
                    </div>
                </div>
            `
        });
        result.innerHTML = text
        count_result.innerHTML = `${count} RESULTS`
    });
}

function submitHotel(hotel_name) {
    localStorage.setItem('lode_hotel_name', JSON.stringify(hotel_name));
    document.location.href = "detail.html";
}

document.getElementById("search_btn").addEventListener("click", function() {
    let search_hotel_name = document.getElementById("search_hotel_name").value.trim();
    let search_location = document.getElementById("search_location").value;
    let search_date_in = document.getElementById("search_date_in").value;
    let search_date_out = document.getElementById("search_date_out").value;
    let search_guests = document.getElementById("search_guests").value;
    // get option bar
    let rating = [...document.querySelectorAll('.checkbox_star:checked')].map(checkbox => checkbox.value).join('-');
    let price = [...document.querySelectorAll('.input_price')].map(input => input.value).join('-');

    if (search_date_in.length !== 0 && search_date_out.length !== 0) {
        let start = search_date_in.split("-").reverse().join("-");
        let end = search_date_out.split("-").reverse().join("-");
        if (price == "-") {
            price = "0-500000"
        }
        if (rating == "") {
            rating = "0-1-2-3-4-5"
        }
        data = search_backend(start, end, search_guests, search_location, "", price, rating);
        search_hotel(data)
    } else {
        alert("input date!")
    }
});