// src/main.ts

// Initialize the login form functionality
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form") as HTMLFormElement;

    if (loginForm) {
        loginForm.addEventListener("submit", handleLogin);
    }
});

// Handle form submission
function handleLogin(event: Event) {
    event.preventDefault();

    const usernameInput = document.getElementById("username") as HTMLInputElement;
    const passwordInput = document.getElementById("password") as HTMLInputElement;

    const loginData: LoginForm = {
        username: usernameInput.value,
        password: passwordInput.value,
    };

    // Simulate a login request
    simulateLoginRequest(loginData)
        .then((response: LoginResponse) => {
            if (response.success) {
                alert("Login successful!");
                // Redirect or perform further actions
            } else {
                alert("Login failed: " + response.message);
            }
        })
        .catch((error) => {
            console.error("Error during login:", error);
            alert("An error occurred. Please try again.");
        });
}

// Simulated login request function
function simulateLoginRequest(data: LoginForm): Promise<LoginResponse> {
    return new Promise((resolve) => {
        setTimeout(() => {
            // Simulate a successful login response
            resolve({ success: true, message: "Logged in successfully!" });
        }, 1000);
    });
}

// Define the LoginForm interface
interface LoginForm {
    username: string;
    password: string;
}

// Define the LoginResponse interface
interface LoginResponse {
    success: boolean;
    message: string;
}