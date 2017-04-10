$('#feedback-form').on('submit', function (e) {
    e.preventDefault();
    var form = e.target;
    var feedback_form = $(this).serialize();
    $.ajax({
        url: form.action,
        method: form.method,
        data: feedback_form,
        success: function (response) {
            if (response.response == 'success') {
                alert('Мы вам перезвоним');
                $('#feedback-form').trigger('reset');
            } else {
                alert('Упс! Что-то не так, попробуйте обновить страницу.')
            }
        }
    })
});