function responsiveSizes() {
    $('.iframe-responsive').each(function () {
        var em = $(this);

        if (em.hasClass('iframe-responsive')) {
            var currentWidth = em.attr('width');
            var currentHeight = em.attr('height');
            var ratio = 0.5625;

            if (!isNaN(currentWidth) && !isNaN(currentHeight))
                ratio = currentHeight / currentWidth;

            var newWidth = em.closest('article').width();
            var newHeight = newWidth * ratio;

            em.attr('width', newWidth);
            em.attr('height', newHeight);
        }

        if (em.hasClass('img-responsive')) {
            var path = em.data('path');
            if (path) {
                var width = em.closest('article').width();
                path = path.replace('image/', '');
                em.attr('src', '/image/resize/' + width + '/0/' + path);
            }
        }
    });
}


$(function () {
    responsiveSizes();
});
