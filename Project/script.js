// Grab the toggle button and the root HTML element
const themeToggle = document.getElementById('theme-toggle');
const rootElement = document.documentElement;

// Check local storage for layout setting consistency
const savedTheme = localStorage.getItem('theme') || 'dark';
rootElement.setAttribute('data-theme', savedTheme);
updateToggleIcon(savedTheme);

// Event listener for the theme button click
themeToggle.addEventListener('click', () => {
    const currentTheme = rootElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    rootElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateToggleIcon(newTheme);
});

// Update standard toggle text dynamically 
function updateToggleIcon(theme) {
    if (theme === 'dark') {
        themeToggle.textContent = '🌙';
    } else {
        themeToggle.textContent = '☀️';
    }
}