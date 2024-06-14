document.addEventListener('DOMContentLoaded', function () {
    var addItemButton = document.getElementById('add_item');
    var removeItemButton = document.getElementById('remove_item');
    var clearListButton = document.getElementById('clear_list');
    var myList = document.querySelector('.my_list');

    // Event listener for adding a new item
    addItemButton.addEventListener('click', function () {
        // Create a new <li> element
        var newItem = document.createElement('li');
        newItem.textContent = 'Item'; // Set the text content (you can modify this as needed)

        // Append the new <li> element to the list
        myList.appendChild(newItem);
    });

    // Event listener for removing the last item
    removeItemButton.addEventListener('click', function () {
        // Check if there are items to remove
        if (myList.lastElementChild) {
            // Remove the last <li> element from the list
            myList.removeChild(myList.lastElementChild);
        } else {
            console.log('No items to remove');
        }
    });

    // Event listener for clearing the entire list
    clearListButton.addEventListener('click', function () {
        // Remove all <li> elements from the list
        myList.innerHTML = '';
    });
});
