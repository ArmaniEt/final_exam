function dataPost(object, event) {
    event.preventDefault();
    let url = form_elem.attr('action');
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        url: url,
        data: {
            book_object: object,
            csrfmiddlewaretoken: csrftoken
        },
        type: 'POST',
    });

}