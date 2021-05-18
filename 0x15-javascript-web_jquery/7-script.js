$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function (result) {
    $('DIV#character').html(result.name);
  }
});
