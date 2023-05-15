// $("div").click(function(){if($("div").hasClass("desktop1"))
//     $("div").click(function(){$("div").toggleClass("desktop1 desktop2").text("desktop2")});
//     else if($("div").hasClass("desktop2"))
//         $("div").click(function(){$("div").toggleClass("desktop2 desktop3").text("desktop3")});
//     else if($("div").hasClass("desktop3"))
//         $("div").click(function(){$("div").toggleClass("desktop3 desktop4").text("desktop4")});
//     });
//


$(document).ready(function () {
    var sildeNum = $('.desktop').length,
        wrapperWidth = 100 * sildeNum,
        slideWidth = 100/sildeNum;
    $('.wrapper').width(wrapperWidth + '%');
    $('.desktop').width(slideWidth + '%');

    $('div.desktop').click(function () {
        var slideNumber = $('#' + String($(this).attr("id"))).index('.desktop'),
            margin = slideNumber * -100 + '%';
        // var margin = 2 * -100 + '%';

        $('.wrapper').animate({marginLeft: margin},1000);
        return false;
    });
});

