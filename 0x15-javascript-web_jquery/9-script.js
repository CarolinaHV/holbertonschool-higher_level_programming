$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (result) {
    $('DIV#hello').html(result.hello);
  }
});
