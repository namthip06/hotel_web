const api = "http://127.0.0.1:8000";

// get api
async function search_backend(start, end, guest, country, city, price, rating){
  let response = await fetch(`${api}/search/?start=${start}&end=${end}&guest=${guest}&country=${country}&city=${city}&price=${price}&rating=${rating}`);
  let data = await response.json();
  return data
}

function radioCity(city) {
  let result = document.getElementById("result_city");
  let data = search_backend("1-1-2000", "2-1-2000", "1", "", city, "0-100000", "0-1-2-3-4-5")
  data.then(function(data) {
    let text = "";
    Object.keys(data).forEach(function(key) {
      text += `
        <a href="#">
            <div class="card mb-4 me-lg-5 me-1 shadow-sm" style="width: 15rem;">
                <img src="https://picsum.photos/300/200" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-title text-capitalize mb-1 fw-bold">${key}</p>
                    <div class="d-flex mb-1">
                        <i class="bi bi-star"></i>
                        <i class="bi bi-star"></i>
                        <i class="bi bi-star"></i>
                    </div>
                    <p class="m-0 text-body-secondary text-decoration-line-through"><small>THB ${data[key]['Price']}</small></p>
                    <p class="fw-semibold"><small>THB ${data[key]['Price']}</small></p>
                </div>
            </div>
        </a>
      `
    });
    result.innerHTML = text
  });
}

function radioInter(country) {
  let result = document.getElementById("result_inter");
  let data = search_backend("1-1-2000", "2-1-2000", "1", country, "", "0-100000", "0-1-2-3-4-5")
  data.then(function(data) {
    let text = "";
    Object.keys(data).forEach(function(key) {
      text += `
        <a href="#">
            <div class="card mb-4 me-lg-5 me-1 shadow-sm" style="width: 15rem;">
                <img src="https://picsum.photos/300/200" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-title text-capitalize mb-1 fw-bold">${key}</p>
                    <div class="d-flex mb-1">
                        <i class="bi bi-star"></i>
                        <i class="bi bi-star"></i>
                        <i class="bi bi-star"></i>
                    </div>
                    <p class="m-0 text-body-secondary text-decoration-line-through"><small>THB ${data[key]['Price']}</small></p>
                    <p class="fw-semibold"><small>THB ${data[key]['Price']}</small></p>
                </div>
            </div>
        </a>
      `
    });
    result.innerHTML = text
  });
}

document.querySelectorAll('.cities').forEach(function(button) {
  button.addEventListener('click', function() {
      radioCity(this.value)
  });
});

document.querySelectorAll('.international').forEach(function(button) {
  button.addEventListener('click', function() {
      radioInter(this.value)
  });
});

// event search btn
document.getElementById("search_btn").addEventListener("click", function() {
  // get search element
  let search_hotel_name = document.getElementById("search_hotel_name").value.trim();
  let search_location = document.getElementById("search_location").value;
  let search_date_in = document.getElementById("search_date_in").value;
  let search_date_out = document.getElementById("search_date_out").value;
  let search_guests = document.getElementById("search_guests").value;

  // check condition search
  if (search_date_in.length !== 0 && search_date_out.length !== 0) {
    let start = search_date_in.split("-").reverse().join("-");
    let end = search_date_out.split("-").reverse().join("-");
    localStorage.setItem('lode_start', JSON.stringify(start));
    localStorage.setItem('lode_end', JSON.stringify(end));
    localStorage.setItem('lode_location', JSON.stringify(search_location));
    localStorage.setItem('lode_guests', JSON.stringify(search_guests));

    document.location.href = "search.html";
  } else {
      alert("input date!")
  }
});

// start
radioCity("Bangkok")
radioInter("Japan")