$(document).ready(function() {
    // Initialize animations
    function initializeAnimations() {
        // Fade in hero section
        $('.animate-fade-in').css('opacity', '0').animate({
            opacity: 1
        }, 1000);

        $('.animate-fade-in-delay').css('opacity', '0').delay(500).animate({
            opacity: 1
        }, 1000);

        // Animate sections on scroll
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    $(entry.target).animate({
                        opacity: 1
                    }, 1000);
                    sectionObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        $('.impact-section').each(function() {
            sectionObserver.observe(this);
        });
    }

    // Smooth scroll for navigation links
    $('.nav-link').on('click', function(e) {
        e.preventDefault();
        const target = $($(this).attr('href'));

        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top - 100
            }, 800);
        }
    });

    // Update active navigation link on scroll
    function updateActiveNavLink() {
        const scrollPosition = $(window).scrollTop();

        $('.impact-section').each(function() {
            const top = $(this).offset().top - 120;
            const bottom = top + $(this).outerHeight();

            if (scrollPosition >= top && scrollPosition <= bottom) {
                const id = $(this).attr('id');
                $('.nav-link').removeClass('text-blue-600');
                $(`.nav-link[href="#${id}"]`).addClass('text-blue-600');
            }
        });
    }

    // Back to top button functionality
    const backToTop = $('#backToTop');

    function updateBackToTopButton() {
        if ($(window).scrollTop() > 300) {
            backToTop.removeClass('invisible').animate({
                opacity: 1
            }, 300);
        } else {
            backToTop.animate({
                opacity: 0
            }, 300, function() {
                $(this).addClass('invisible');
            });
        }
    }

    backToTop.on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
    });

    // Handle scroll events with lodash throttle
    $(window).on('scroll', _.throttle(function() {
        updateActiveNavLink();
        updateBackToTopButton();
    }, 100));

    // Initialize animations
    initializeAnimations();

    // Handle window resize
    $(window).on('resize', _.debounce(function() {
        // Recalculate positions if needed
    }, 250));

    // Add hover effect to section images
    $('.impact-section img').hover(
        function() {
            $(this).addClass('scale-105');
        },
        function() {
            $(this).removeClass('scale-105');
        }
    );

    // Initialize tooltips if needed
    $('[data-tooltip]').each(function() {
        $(this).tooltip({
            placement: 'top',
            trigger: 'hover'
        });
    });
});