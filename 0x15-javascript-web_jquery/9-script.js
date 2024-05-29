$(document).ready( function () {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr', // api endpoint
        method: 'GET',
        success: function(data) {
            // display hello
            $('#hello').text(data.hello)
        },
        error: function(error) {
            $('#hello').text("Can't fetch data, check your internet connection");
            console.error('Error fetching data:', error);
        }
    });
})
