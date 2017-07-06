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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$('#buy-button').on('click', function () {
    var product_id = $('.product-description h2').data('id');
    var wallet_money = $('.link-reqistration-page span b').text();
    var product_price = $('.product-description .price b').text();
    if (confirm('Вы действительно хотите приобрести товар?')) {
        $.ajax({
            url: buy_product_url,
            type: 'POST',
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function (response) {
                if (response.response === 'success') {
                    var new_balance = wallet_money-product_price;
                    $('.link-reqistration-page span b').text(new_balance);
                } else {
                    alert('У Вас недостаточно денег.')
                }
            },
            error: function () {
                alert('Что-то пошло не так. Попробуйте обновить страницу.');
            }
        })
    }
});