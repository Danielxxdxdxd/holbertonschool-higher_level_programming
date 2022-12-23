const $clickEvent = $('DIV#toggle_header');
const $header = $('header');

$clickEvent.click(function () {
  const currentClass = $header.attr('class');
  
  if (currentClass === 'green') {
    $header.toggleClass(`${currentClass} red`)
  } else {
    $header.toggleClass(`${currentClass} green`)
  }
});
