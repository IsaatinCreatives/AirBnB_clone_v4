// Jquery Script

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

  const apiStatus = $('DIV#api_status');
  $.ajax('http://0.0.0.0:5001/api/v1/status/').done(function (data) {
    if (data.status === 'OK') {
      apiStatus.addClass('available');
    } else {
      apiStatus.removeClass('available');
    }
  });
});
