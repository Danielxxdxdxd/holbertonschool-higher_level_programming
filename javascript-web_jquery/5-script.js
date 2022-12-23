const $list = $('ul.my_list');
const $clickEvent = $('div#add_item');

$clickEvent.click(function () {
  $list.append('<li>Item</li>');
});
