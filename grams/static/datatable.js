$(document).ready(function () {
    $('#myTable').DataTable();
} );

$(document).ready(function() {

    $('#myTable tr').click(function() {
        var href = $(this).find("a").attr("href");
        if(href) {
            window.location = href;
        }
    });

});