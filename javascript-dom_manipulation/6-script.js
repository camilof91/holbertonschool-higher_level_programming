document.addEventListener('DOMContentLoaded', function () {
    // URL of the Star Wars character API
    var url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    // Fetch the data from the API
    fetch(url)
        .then(function (response) {
            // Check if the request was successful
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Parse the JSON response
            return response.json();
        })
        .then(function (data) {
            // Extract the character name from the response data
            var characterName = data.name;

            // Select the <div> element with id 'character' and update its content
            var characterElement = document.getElementById('character');
            characterElement.textContent = characterName;
        })
        .catch(function (error) {
            // Handle any errors that occurred during the fetch
            console.error('There was a problem with the fetch operation:', error);
        });
});