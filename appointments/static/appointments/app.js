$( document ).ready(function() {
  $("#search").click( function(event) {
    event.preventDefault();
    getAppointments();
    });
})

function getAppointments() {
  $.get( "app/", function( data ) {
    for (appointment of data.appointments) {
      var row = "<tr><td>" + appointment.datetime + "</td><td>" + appointment.description + "</td></tr>"
      $("#results").after(row)
    }
  });
}
