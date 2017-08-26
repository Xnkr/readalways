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

    $('#bookModal').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var book_id = button.data('book-id') // Extract info from data-* attributes
        $.ajax({
            type: "GET",
            url: "/borrow/fetch",
            data: {
                book_id: book_id
            },
            success: function(data) {
                $('#book_desc').html(data);
                var name_find = /id=\"book_name\">(.*?)<\/h4>/g;
                var match = name_find.exec(data);
                $('#bookModalLabel').text(match[1]);
            }
        })
    })

});