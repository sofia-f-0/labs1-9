$(document).ready(function() {
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');

    $parallaxElements.each(function() {
        var originalTop = parseFloat($(this).css('top')) || 0;
        $(this).data('originalTop', originalTop);
    });

    var originalLogoTop = parseFloat($logo.css('top')) || 0;

    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();

        $parallaxElements.each(function(index) {
            var speedFactor = 0.15 * (index + 1);
            var originalTop = $(this).data('originalTop');
            $(this).css({ top: originalTop + scrolled * speedFactor });
        });

        var logoSpeed = 0.1;
        $logo.css({ top: originalLogoTop + scrolled * logoSpeed });
    });
});