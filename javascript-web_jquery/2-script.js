const $clickEvent = $('DIV#red_header');
const $header = $('header');

$clickEvent.click(function () {
  $header.css('color', '#FF0000');
});
