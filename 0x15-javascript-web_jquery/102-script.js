$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/',
      type: 'get',
      data: { lang: $('INPUT#language_code').val() },
      success: function (msg) {
        $('DIV#hello').html(msg.hello);
      }
    });
  });
});
