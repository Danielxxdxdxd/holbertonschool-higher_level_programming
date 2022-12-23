const $clickEvent = $('DIV#red_header');
const $header = $('header');

$clickEvent.click(function () {
  $header.addClass('red');
});
