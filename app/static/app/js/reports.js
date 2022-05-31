document.addEventListener("DOMContentLoaded", function() {
    $('#table-reports').DataTable( {
        searching: true,
        paging: true,
        "lengthMenu": [ [20, -1] , [20, "All"]],
        info: true,
        "columns": [
            { "width": "5%" },
            { "width": "10%" },
            { "width": "50%" },
            null,
            { "width": "15%"},
            { "width": "10%"}
          ],
          rowCallback: function ( row, data ) {
            if ( data[3] == 'In progress' ) {
                $(row).css('background-color', '#edf582');
            }
            var dateString = moment(data[4], 'HH:mm DD.MM.YYYY');
            var dateObj = new Date(dateString);
            var a =  moment(new Date())
            if (a.diff(dateObj) > 10800000 && data[3] == 'Pending') {
                $(row).addClass('bad-row');
            }
          }
    });

    const cells = document.querySelectorAll('tr');
    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function (e) {
          row = e.path[1];
          console.log("Row id: " + row.id);
          window.location.href = "/view-malfunction/" + row.id;
        });
      }
});