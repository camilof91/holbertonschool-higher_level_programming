document.addEventListener('DOMContentLoaded', function () {
    // Get the element with id 'toggle_header'
    var toggleHeaderElement = document.getElementById('toggle_header');
    // Add a click event listener to 'toggle_header'
    toggleHeaderElement.addEventListener('click', function () {
        // Get the <header> element
        var headerElement = document.querySelector('header');
        // Toggle the 'red' and 'green' classes on the <header> element
        if (headerElement.classList.contains('red')) {
            headerElement.classList.remove('red');
            headerElement.classList.add('green');
        } else if (headerElement.classList.contains('green')) {
            headerElement.classList.remove('green');
            headerElement.classList.add('red');
        } else {
            // Default behavior: Add 'green' class if neither 'red' nor 'green' is present
            headerElement.classList.add('green');
        }
    });
});
