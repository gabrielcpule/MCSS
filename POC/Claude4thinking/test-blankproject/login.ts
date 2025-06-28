// login.ts - TypeScript logic for Bank Login page using MCSS

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm') as HTMLFormElement;
  const messageDiv = document.getElementById('login-message') as HTMLDivElement;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    messageDiv.textContent = '';
    messageDiv.className = 'u-text-center u-margin-md';

    const username = (document.getElementById('username') as HTMLInputElement).value.trim();
    const password = (document.getElementById('password') as HTMLInputElement).value;

    // Simple validation
    if (!username || !password) {
      messageDiv.textContent = 'Please enter both username and password.';
      messageDiv.classList.add('c-form-field__error');
      return;
    }

    // Simulate login (replace with real API call)
    (form.querySelector('button[type="submit"]') as HTMLButtonElement).setAttribute('data-mcs-state', 'loading');
    await new Promise((res) => setTimeout(res, 1200));
    (form.querySelector('button[type="submit"]') as HTMLButtonElement).removeAttribute('data-mcs-state');

    if (username === 'user' && password === 'password123') {
      messageDiv.textContent = 'Login successful! Redirecting...';
      messageDiv.classList.add('u-text-bold');
      messageDiv.style.color = 'var(--mcs-color-success)';
      setTimeout(() => {
        window.location.href = '/dashboard';
      }, 1500);
    } else {
      messageDiv.textContent = 'Invalid username or password.';
      messageDiv.classList.add('c-form-field__error');
    }
  });
});
