$(document).ready(function () {
    $(".main_slider.owl-carousel").owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        items: 1,
        //autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1000
    });

    $(".footer .scroll_top").on("click", function () {
        $('html, body').animate({scrollTop: 0}, 1000);
    });
});