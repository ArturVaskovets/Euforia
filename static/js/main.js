$(document).ready(function () {
    $(".main_slider.owl-carousel").owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        items: 1,
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1000
    });

    $(".footer .scroll_top").on("click", function () {
        $('html, body').animate({scrollTop: 0}, 1000);
    });

    // Jewelry
    $(".products_wrapper .products_items .item_color").on("click", function () {
        let selected_color = $(this).attr("data-color");
        $(this).addClass("active").siblings().removeClass("active");
        $(this).closest(".item_images").find(".item_image." + selected_color).show().siblings(".item_image").hide();
    });

    $(".products_wrapper .products_filters .filters_block_slider .price_slider").each(function () {
        let min_price = Number($(this).attr("data-min-price"));
        let max_price = Number($(this).attr("data-max-price"));

        $(this).slider({
            range: true,
            min: min_price,
            max: max_price,
            values: [min_price, max_price],
            slide: function (event, ui) {
                $(".products_wrapper .filters_block_slider .price_values .price_min").val(ui.values[0]);
                $(".products_wrapper .filters_block_slider .price_values .price_max").val(ui.values[1]);
                $(".products_wrapper .filters_block_slider .price_values .price_min_value").html(ui.values[0]);
                $(".products_wrapper .filters_block_slider .price_values .price_max_value").html(ui.values[1]);
            },
            stop: applyFilters
        });
    });

    $(".products_wrapper .products_filters .filters_block_item").on("click", function () {
        if (!$(this).hasClass("disabled"))
        {
            $(this).toggleClass("active");
            applyFilters();
        }
    });

    function applyFilters() {
        let all_items = $(".products_wrapper .products_items .item");
        all_items.show();

        filterBy("brand", all_items);
        filterBy("material", all_items);
        filterBy("color", all_items);
        filterByPrice(all_items);
    }

    function filterBy(filter_name, all_items) {
        let filter_elements = $(`.products_wrapper .filters_block.${filter_name} .filters_block_item.active`);
        if (filter_elements.length) {
            let filters = [];
            filter_elements.each(function () {
                filters.push($(this).attr(`data-filter-${filter_name}`));
            });

            all_items.each(function () {
                if (filter_name === "color") {
                    let filtered = true;
                    let item_colors = $(this).attr("data-colors").split(';');
                    for (let i = 0; i < item_colors.length; i++) {
                        if (filters.includes(item_colors[i])) {
                            filtered = false;
                            break;
                        }
                    }
                    if (filtered) {
                        $(this).hide();
                    }
                } else {
                    if (!filters.includes($(this).attr(`data-${filter_name}`))) {
                        $(this).hide();
                    }
                }

            });
        }
    }

    function filterByPrice(all_items) {
        let min_price = Number($(".products_wrapper .filters_block_slider .price_values .price_min").val());
        let max_price = Number($(".products_wrapper .filters_block_slider .price_values .price_max").val());

        all_items.each(function () {
            let current_price = Number($(this).attr("data-price"));
            if (current_price < min_price || current_price > max_price) {
                $(this).hide();
            }
        });
    }
});