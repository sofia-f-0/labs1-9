$(document).ready(function() {
    // Подсветка постов
    $('.one-post').hover(
        function() {
            $(this).find('.one-post-shadow').animate({ opacity: 0.2 }, 300);
        },
        function() {
            $(this).find('.one-post-shadow').animate({ opacity: 0 }, 300);
        }
    );

    // Анимация логотипа
    var $logo = $('.logo');
    if ($logo.length) {
        var originalWidth = $logo.width();
        $logo.hover(
            function() {
                $(this).animate({ width: originalWidth + 20 }, 200);
            },
            function() {
                $(this).animate({ width: originalWidth }, 200);
            }
        );
    }
});