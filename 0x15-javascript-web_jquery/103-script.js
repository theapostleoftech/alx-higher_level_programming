/*
  this fetches and prints how to say “Hello” depending on the language
*/
$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const translator = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + translator;
    $.get(url, function (data, textStatus) {
      console.log(url, data, textStatus);
      if (data.code !== 'none') {
        $('DIV#hello').text(data.hello);
      } else {
        $('DIV#hello').text('Invalid Language code');
      }
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      const translator = $('INPUT#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + translator;
      $.get(url, function (data, textStatus) {
        console.log(url, data, textStatus);
        if (data.code !== 'none') {
          $('DIV#hello').text(data.hello);
        } else {
          $('DIV#hello').text('Invalid Language code');
        }
      });
    }
  });
});
