const $header = $('header');
const $clickEvent = $('div#update_header');

$clickEvent.click(function () {
  $header.text('New Header!!!');
});
