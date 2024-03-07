const api = "http://127.0.0.1:8000";

const emailinput = document.getElementById("login-email");
const passwordinput = document.getElementById("login-password");
const button = document.getElementById("login-button");

async function login(){
    const email = emailinput.value.trim();
    const password = passwordinput.value.trim();

    if(email === '' || password === ''){
        alert("Please enter email / password");
        return;
    }

    try{
        const response = await fetch(`${api}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                user_password: password
            })
        });
        
        if(response.ok) {
            const data = await response.json();
            // Assuming the response contains information about the success of login
            if(data) {
                window.location.href = "account.html";
                // Redirect
            } else {
                alert("Login failed. Please check your credentials.");
            }
        } else {
            const errorMessage = await response.text();
            alert("Error: " + errorMessage);
        }
    } catch(error) {
        console.error('Error:', error);
        alert("An error occurred while trying to log in. Please try again later.");
    }
}

button.addEventListener("click", login);
