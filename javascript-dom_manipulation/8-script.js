document.addEventListener('DOMContentLoaded', function() {
  // URL to fetch the translation from
  var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch the data from the API
  fetch(url)
    .then(function(response) {
      // Check if the request was successful
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Parse the JSON response
      return response.json();
    })
    .then(function(data) {
      // Extract the translation of "hello" from the response data
      var helloTranslation = data.hello;

      // Select the <div> element with id 'hello' and update its content
      var helloElement = document.getElementById('hello');
      helloElement.textContent = helloTranslation;
    })
    .catch(function(error) {
      // Handle any errors that occurred during the fetch
      console.error('There was a problem with the fetch operation:', error);
    });
});
