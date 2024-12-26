$(document).ready(function() {
    // Initialize animations for hero section
    const animateHero = () => {
        $('.animate-fade-in').css('opacity', '0').animate({
            opacity: 1
        }, 1000);

        $('.animate-fade-in-delay').css('opacity', '0').delay(500).animate({
            opacity: 1
        }, 1000);

        $('.animate-fade-in-delay-2').css('opacity', '0').delay(1000).animate({
            opacity: 1
        }, 1000);

        $('.animate-fade-in-delay-3').css('opacity', '0').delay(1500).animate({
            opacity: 1
        }, 1000);
    };

    // Initialize animations for fact cards
    const animateFactCards = () => {
        $('.fact-card').each(function(index) {
            $(this).css('opacity', '0').delay(index * 200).animate({
                opacity: 1
            }, 1000);
        });
    };

    // Run animations on page load
    animateHero();
    animateFactCards();

    // Smooth scroll handling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        event.preventDefault();
        const target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 100
            }, 1000);
        }
    });

    // Parallax effect for hero image
    $(window).on('scroll', _.throttle(function() {
        const scrolled = $(window).scrollTop();
        $('.hero-image').css('transform', `translateY(${scrolled * 0.5}px)`);
    }, 50));
});