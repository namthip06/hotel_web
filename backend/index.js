const api = "http://127.0.0.1:8000";

const searchBar = document.getElementById("index-searchbar"); // Select the search bar input
const searchButton = document.getElementById("index-searchbutton"); // Select the search button

async function searchHotels() {
    const searchTerm = searchBar.value.trim(); // Get the search term from the input
  
    if (searchTerm.length === 0) {
      alert("Please enter a hotel name or location to search.");
      return;
    }
  
    try {
      const response = await fetch(`${api}/hotel?name=${searchTerm}`); // Fetch data from '/hotel' endpoint
      const data = await response.json(); // Parse the JSON response
  
      if (data.error) {
        alert("Error fetching hotels: " + data.error);
        return;
      }
  
      // Handle and display the search results here (e.g., create new elements or update existing ones)
      console.log("Search results:", data); // For debugging purposes
  
    } catch (error) {
      console.error("Error fetching hotels:", error);
      alert("An error occurred while searching for hotels.");
    }
 }

searchButton.addEventListener("click", searchHotels); // Add click event listener to the button
  