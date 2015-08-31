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

});