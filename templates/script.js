// script.js

document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector('.toggle-button');
    const tableResponsive = document.querySelector('.table-responsive');

    toggleButton.addEventListener('click', function () {
        if (tableResponsive.style.display === 'none' || tableResponsive.style.display === '') {
            tableResponsive.style.display = 'block';
        } else {
            tableResponsive.style.display = 'none';
        }
    });
});
