$(document).ready(function () {
    $(".qtyminus").on("click", function () {
        var now = $(".qty").val();
        if ($.isNumeric(now)) {
            if (parseInt(now) - 1 > 0) {
                now--;
            }
            $(".qty").val(now);
        }
    })
    $(".qtyplus").on("click", function () {
        var now = $(".qty").val();
        if ($.isNumeric(now)) {
            $(".qty").val(parseInt(now) + 1);
        }
    });
});

const indicator = document.getElementsByClassName('indicator')
const main = document.querySelector('.main')
for (let i = 0; i < indicator.length; i++) {
    indicator[i].onclick = (e) => {
        for (let a = 0; a < indicator.length; a++) {
            indicator[i].classList.remove('active')
        }
        indicator[i].classList.add('active')
        main.src = e.target.src;
    }
}
$(document).ready(function () {
    $('#SearchBoxBrand').on('keyup', function () {
        var query = $(this).val();
        $.ajax({
            url: '/',
            type: 'get',
            data: {
                'query': query
            },
            success: function (data) {
                console.log(data)
                // $('#resultSearchBrand').html(data);
                  $('#resultSearchBrand').empty();
                $.each(data, function (index, brand) {
                    $('#resultSearchBrand').append('<p>' + brand.name + '</p>');
                });
            }
        });
    });
});



