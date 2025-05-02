// Basic app.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('EduVision app loaded');
    
    // Handle login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('Login attempt');
            window.location.href = 'views/dashboard.html';
        });
    }
});