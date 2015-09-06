$(document).ready(function(){

    /* Adjust dropdown alignment according to panel position */
    function adjustDDAlign(el) {
        var dropdown = el.parent().children('.dropdown-menu'),
            offsetLeft = el.offset().left,
            dropdownWidth = dropdown.width(),
            docWidth = $(window).width();

        if (!(offsetLeft + dropdownWidth <= docWidth))
            dropdown.addClass('dropdown-menu-right');
    }
    $('.dropdown-toggle').on("click", function() {
        adjustDDAlign($(this));
    }).each(function() {
        adjustDDAlign($(this));
    });

    /* Prevent dropdown close on click to allow copy of text */
    $('.dropdown-menu').on("click", function(e) {
        $('.dropdown-menu').not(
            $(this)).not($('.dropdown-menu .btn-group').closest('.dropdown-menu')
        ).parent().removeClass('open');
        e.stopPropagation();
    });

    /* Allow multi-level dropdowns */
    $('.dropdown-menu .dropdown-toggle').on('click', function(e) {
        if(!$(this).parent().hasClass('open'))
            $('.dropdown-menu').not(
                $('.dropdown-menu .btn-group').closest('.dropdown-menu')
            ).parent().removeClass('open');
        $(this).parent().toggleClass('open');
        e.stopPropagation(); // prevent close caused by button click event on parent
    });

});