const api = "http://127.0.0.1:8000";

const urlParams = new URLSearchParams(window.location.search);
const receivedData = JSON.parse(urlParams.get('data'));

const bg = document.getElementById("bg");
const hotel_location = document.getElementById("location");
const hotel_name = document.getElementById("name");
const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");

function processHotelDetails(data) {
  // Your logic to process the received hotel details data (e.g., display details, populate elements)
  console.log("Received hotel details:", data); // For debugging purposes
  document.getElementById("bg").style.backgroundImage = `url(${data['_Hotel__imgsrc'][0]})`
  document.getElementById("location").textContent = `${data['_Hotel__location']['_Location__city']} - ${data['_Hotel__location']['_Location__country']}`;
  document.getElementById("name").textContent = `${data['_Hotel__name']}`
}

processHotelDetails(receivedData)