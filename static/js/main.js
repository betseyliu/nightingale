// Common JavaScript functions for the Florence Nightingale website

// Initialize common functionality when document is ready
$(document).ready(function() {
    // Add smooth scrolling to all links
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500, 'linear');
    });

    // Add active state to current navigation item
    const currentPath = window.location.pathname;
    $('nav a').each(function() {
        if ($(this).attr('href') === currentPath) {
            $(this).addClass('text-blue-500');
        }
    });
});

// Common utility functions
function fadeInContent(element, delay = 0) {
    $(element).hide().delay(delay).fadeIn(1000);
}

// Common animation functions
function animateOnScroll() {
    $('.animate-on-scroll').each(function() {
        const element = $(this);
        if (element.isInViewport()) {
            element.addClass('animated');
        }
    });
}

// Viewport checking utility
$.fn.isInViewport = function() {
    const elementTop = $(this).offset().top;
    const elementBottom = elementTop + $(this).outerHeight();
    const viewportTop = $(window).scrollTop();
    const viewportBottom = viewportTop + $(window).height();
    return elementBottom > viewportTop && elementTop < viewportBottom;
};

// Handle scroll events with lodash throttle
$(window).on('scroll', _.throttle(function() {
    animateOnScroll();
}, 100));