document.addEventListener("DOMContentLoaded", function() {
    $('#table-reports').DataTable( {
        searching: true,
        "columns": [
            { "width": "5%" },
            { "width": "10%" },
            { "width": "60%" },
            null,
            { "width": "15%"},
          ],
    });
});