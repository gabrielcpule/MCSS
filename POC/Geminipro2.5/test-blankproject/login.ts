// login.ts
// TypeScript logic for Bank Login Page using MCSS-POC framework

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm') as HTMLFormElement;
  const loginMessage = document.getElementById('loginMessage') as HTMLElement;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    loginMessage.textContent = '';
    form.removeAttribute('data-mcs-validation-state');

    const username = (document.getElementById('username') as HTMLInputElement).value.trim();
    const password = (document.getElementById('password') as HTMLInputElement).value;

    // Simple validation
    if (!username || !password) {
      form.setAttribute('data-mcs-validation-state', 'invalid');
      loginMessage.textContent = 'Please enter both username and password.';
      return;
    }

    // Simulate login (replace with real API call)
    if (username === 'user' && password === 'password123') {
      form.setAttribute('data-mcs-validation-state', 'valid');
      loginMessage.textContent = 'Login successful! Redirecting...';
      loginMessage.style.color = 'var(--mcs-color-success-500)';
      setTimeout(() => {
        window.location.href = 'dashboard.html';
      }, 1200);
    } else {
      form.setAttribute('data-mcs-validation-state', 'invalid');
      loginMessage.textContent = 'Invalid username or password.';
      loginMessage.style.color = 'var(--mcs-color-error-500)';
    }
  });
});
