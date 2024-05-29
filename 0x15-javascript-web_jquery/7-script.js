$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json', // api endpoint
    method: 'GET',
    success: function(data) {
        // Assuming display the response
        $('#character').text(data.name);
    },
    error: function(error) {
        $('#character').text('An error occurred');
        console.error('Error fetching data:', error);
    }
});
