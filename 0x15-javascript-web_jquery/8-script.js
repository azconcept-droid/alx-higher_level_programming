$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json', // api endpoint
    method: 'GET',
    success: function(data) {
        // Assuming display the response
        for (const film of data.results) {
            $('#list_movies').append(`<li>${film['title']}</li>`);
        }
    },
    error: function(error) {
        $('#list_movies').text("Can't fetch data, check your internet connection");
        console.error('Error fetching data:', error);
    }
});
