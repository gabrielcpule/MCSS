// Login page logic using TypeScript

function handleLogin(event: Event) {
  event.preventDefault();
  const email = (document.getElementById('email') as HTMLInputElement).value;
  const password = (document.getElementById('password') as HTMLInputElement).value;
  // Simple validation (for demo)
  if (!email || !password) {
    alert('Please enter both email and password.');
    return;
  }
  // Simulate login
  alert(`Logged in as ${email}`);
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('login-form');
  if (form) {
    form.addEventListener('submit', handleLogin);
  }
});
