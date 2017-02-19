$( document ).ready(function() {
  $("#new").click( function(event) {
    $(".toggleHide").toggleClass("hidden");
  })
  $("#cancel").click( function(event) {
    $(".toggleHide").toggleClass("hidden");
  })

  $("#search").click( function(event) {
    $(".added").html("");
    var params = $("#searchInput").val();
    event.preventDefault();
    getAppointments(params);
    $("#searchInput").val("")
    });
})

function getAppointments(params) {
  $.get( "app/", {params: params}, function( data ) {
    var rows = ""
    for (appointment of data.appointments) {
      var row = "<tr class='added'><td>" + appointment.datetime + "</td><td>" + appointment.description + "</td></tr>"
      rows = rows + row
    }
    $("#results").after(rows);
  });
}
