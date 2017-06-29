function removeBook(id) {
    if (id) {
        $.ajax({
            url: '/books/' + id,
            type: 'DELETE',
            success: function(result) {
                location.reload();
            }
        });
    } else {
        alert('No id selected');
    }
}