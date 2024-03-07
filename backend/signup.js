const api = "http://127.0.0.1:8000";

const emailinput = document.getElementById("signup-email");
const phoneinput = document.getElementById("signup-phone");
const passwordinput = document.getElementById("signup-password");
const confirmpasswordinput = document.getElementById("signup-confirm-password");
const button = document.getElementById("signup-button");

async function signup(){    
    const email = emailinput.value.trim();
    const phone = phoneinput.value.trim();
    const password = passwordinput.value.trim();
    const confirmpassword = confirmpasswordinput.value.trim();

    if(email === '' || password === ''){
        alert("Please enter email / password");
        return;
    }

    else if(password !== confirmpassword){
        alert("Passwords do not match!");
        return;
    }

    try{
        const response = await fetch(`${api}/sign_up`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_name: email,
                user_password: password,
                phone_number: phone,
                email: email
            })
        });
        if(response.ok) {
            const data = await response.json();
            // Assuming the response contains information about the success of login
            if(data) {
                window.location.href = "account.html";
                // Redirect
            } else {
                alert("Sign up failed. Please check your credentials.");
            }
        } else {
            const errorMessage = await response.text();
            alert("Error: " + errorMessage);
        }
    } catch(error) {
        console.error('Error:', error);
        alert("An error occurred while trying to sign up. Please try again later.");
    }
}

button.addEventListener("click", signup);
