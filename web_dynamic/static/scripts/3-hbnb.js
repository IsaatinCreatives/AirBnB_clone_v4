// jQuery

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

$.ajax({
  type: 'POST',
  url: 'http://0.0.0.0:5001/api/v1/places_search/',
  contentType: 'application/json',
  data: '{}',
  success: function (data) {
    for (const currentPlace of data) {
      $('.places').append('<article> <div class="title"> <h2>' + currentPlace.name + '</h2><div class="price_by_night">' + '$' + currentPlace.price_by_night + '</div></div> <div class="information"> <div class="max_guest"> <i class="fa fa -users fa-3x" aria-hidden="true"></i><br />' + currentPlace.max_guest + ' Guests</div><div class="number_rooms"> <i class="fa fa -users fa-3x" aria-hidden="true"></i><br />' + currentPlace.number_rooms + ' Bedrooms</div><div class="number_bathrooms"> <i class="fa fa -users fa-3x" aria-hidden="true"></i><br />' + currentPlace.number_bathrooms + ' Bathroom </div></div> <div class="user"></div><div class="description">' + '$' + currentPlace.description + '</div></article>');
    }
  }
});
