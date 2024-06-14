document.addEventListener('DOMContentLoaded', function () {
    // Get the element with id 'red_header'
    var redHeaderElement = document.getElementById('red_header');
    // Add a click event listener to 'red_header'
    redHeaderElement.addEventListener('click', function () {
        // Get the <header> element
        var headerElement = document.querySelector('header');
        // Add the 'red' class to the <header> element
        headerElement.classList.add('red');
    });
});
