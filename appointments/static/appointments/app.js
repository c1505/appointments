$( document ).ready(function() {
  $("#search").click( function(event) {
    var params = $("#searchInput").val()
    event.preventDefault();
    getAppointments(params);
    });
})

function getAppointments(params) {
  $.get( "app/", {params: params}, function( data ) {
    for (appointment of data.appointments) {
      var row = "<tr><td>" + appointment.datetime + "</td><td>" + appointment.description + "</td></tr>"
      $("#results").after(row)
    }
  });
}
