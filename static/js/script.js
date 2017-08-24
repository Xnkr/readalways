$(document).ready(function() {
    $('.approve').click(function() {
        return confirm("Are you sure you want to send your Email address to the requester?");
    })
    $(function() {
        $('[data-toggle="tooltip"]').tooltip();
        $('#borrowable').tooltip();
    })

    $('.delete').click(function() {
        return confirm("Are you sure you want to delete?");
    })

});