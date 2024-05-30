/*
  This adds the class red to <header> to red (#FF0000)
  when the user clicks on the tag DIV#red_header
*/
$('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
  