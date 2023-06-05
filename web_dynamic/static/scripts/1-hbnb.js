// Appends the items checked to the page

const checkedbox = {};
$(document).ready(function () {
  $('input:checkbox').change(function () {
    if ($(this).is(':checked')) {
      checkedbox[$(this).data('id')] = $(this).data('name');
    } else {
      delete checkedbox[$(this).data('id')];
    }
    $('div.amenities h4').html(function () {
      const amenities = [];
      Object.keys(checkedbox).forEach(function (key) {
        amenities.push(checkedbox[key]);
      });
      if (amenities.length === 0) {
        return ('&nbsp');
      }
      return (amenities.join(', '));
    });
  });
});
