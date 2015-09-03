$(document).ready(function(){

    /* Adjust dropdown alignment according to panel position */
    $('.dropdown-toggle').on("click", function() {
        var dropdown = $(this).parent().children('.dropdown-menu'),
            offsetLeft = $(this).offset().left,
            dropdownWidth = dropdown.width(),
            docWidth = $(window).width();

        if (!(offsetLeft + dropdownWidth <= docWidth))
            dropdown.addClass('pull-right');
    });

    /* Prevent challenge dropdown close on click to allow copy of text */
    $('.btn-group-chal .dropdown-menu').on("click", function(e) {
        e.stopPropagation();
    });

    /* Allow multi-level dropdowns */
    $('div.dropdown-menu .dropdown-toggle').on('click', function() {
        $(this).parent().toggleClass('open');
    });

});