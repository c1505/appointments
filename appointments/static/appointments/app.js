$( document ).ready(function() {
  $("#search").click( function(event) {
    event.preventDefault();
    getAppointments();
    });
})

function getAppointments() {
  $.get( "app/", function( data ) {
    for (appointment of data.appointments) {
      $("#results").append("<p>" + "time: " + appointment.datetime + "description: " + appointment.description + "</p>")
    }
  });
}
