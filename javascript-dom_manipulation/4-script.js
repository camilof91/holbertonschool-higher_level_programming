document.addEventListener('DOMContentLoaded', function () {
    // Get the element with id 'add_item'
    var addItemElement = document.getElementById('add_item');
    // Get the ul element with class 'my_list'
    var myListElement = document.querySelector('.my_list');
    // Add a click event listener to 'add_item'
    addItemElement.addEventListener('click', function () {
        // Create a new <li> element
        var newItem = document.createElement('li');
        // Set the text content of the new <li> element
        newItem.textContent = 'Item';
        // Append the new <li> element to the <ul> with class 'my_list'
        myListElement.appendChild(newItem);
    });
});
