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
  $.get( "search/", {params: params}, function( data ) {
    var rows = ""
    for (appointment of data.appointments) {

      var date = new Date(appointment.datetime);
      var date = ($.format.date(appointment.datetime, "MMM d"))
      var time = ($.format.date(appointment.datetime, "h:mmp"))
      var row = "<tr class='added'><td>" + date + "</td><td>" + time + "</td><td>"+ appointment.description + "</td></tr>"
      rows = rows + row
    }
    $("#results").after(rows);
  });
}
