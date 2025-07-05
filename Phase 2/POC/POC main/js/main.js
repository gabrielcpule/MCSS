// Placeholder for main JS logic if needed for interactivity
// You can add event listeners or other JS here for the demo

document.addEventListener('DOMContentLoaded', function () {
  const card = document.getElementById('interactive-card');
  const toggleBtn = document.getElementById('card-state-toggle');
  if (card && toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      if (card.getAttribute('data-state') === 'highlighted') {
        card.removeAttribute('data-state');
      } else {
        card.setAttribute('data-state', 'highlighted');
      }
    });
  }
});
