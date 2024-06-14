document.addEventListener('DOMContentLoaded', function () {
    // URL of the Star Wars films API
    var url = 'https://swapi-api.hbtn.io/api/films/?format=json';

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
            // Get the array of movies from the data
            var movies = data.results;

            // Select the <ul> element with id 'list_movies'
            var listMoviesElement = document.getElementById('list_movies');

            // Iterate through the movies array
            movies.forEach(function (movie) {
                // Create a new <li> element
                var listItem = document.createElement('li');

                // Set the text content of the <li> to the movie title
                listItem.textContent = movie.title;

                // Append the <li> element to the <ul> list
                listMoviesElement.appendChild(listItem);
            });
        })
        .catch(function (error) {
            // Handle any errors that occurred during the fetch
            console.error('There was a problem with the fetch operation:', error);
        });
});