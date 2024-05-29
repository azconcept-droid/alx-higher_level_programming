$(document).ready( function () {

    const code = $('#language_code').val()
    const translate = $('#btn_translate').val()

    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code, // api endpoint
        method: 'GET',
        success: function(data) {

            $('#btn_translate').on('click', function ( event ) {
                $('#hello').text(data.hello);
              });

            console.log(data)
        },
        error: function(error) {
            $('#hello').text("Can't fetch data, check your internet connection");
            console.error('Error fetching data:', error);
        }
    });
})
