document.addEventListener('DOMContentLoaded', function () {
    // Get the element with id 'update_header'
    var updateHeaderElement = document.getElementById('update_header');
    // Add a click event listener to 'update_header'
    updateHeaderElement.addEventListener('click', function () {
        // Get the <header> element
        var headerElement = document.querySelector('header');
        // Update the text content of the <header> element
        headerElement.textContent = 'New Header!!!';
    });
});
