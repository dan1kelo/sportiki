// tailwind.config.js
module.exports = {
  darkMode: 'class', // или 'media' для автоматического по системной теме
  theme: {
    extend: {},
  },
  plugins: [],
}
document.documentElement.classList.toggle('dark');
document.addEventListener('DOMContentLoaded', function() {
  const toggleDarkMode = document.getElementById('toggle-dark-mode');
  if (toggleDarkMode) {
    toggleDarkMode.addEventListener('click', function() {
      document.documentElement.classList.toggle('dark');
    });
  }
});