function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var location = document.getElementById("locations");
  var bathrooms = document.getElementById("bathrooms");
  var floor_no = document.getElementById("floor");
  var parking_size = document.getElementById("parking");
  var property_size = document.getElementById("size");
  var bhk_type = document.getElementById("bedrooms");
  var maintenance = document.getElementById("maintenance");

  var rent = document.getElementById("predict_rent");

  var url = "http://127.0.0.1:5000/predict";

  $.post(
    url,
    {
      localityId: location.value,
      bathroom: bathrooms.value,
      floor: floor_no.value,
      parking: parking_size.value,
      property_size: property_size.value,
      type_bhk: bhk_type.value,
      maintenance: maintenance.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      rent.innerHTML =
        "<h2> Predicted House Rent is: " +
        data.estimated_price.toString() +
        "</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("locations");
      $("#locations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#locations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
