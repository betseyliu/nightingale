$(document).ready(function() {
    // Initialize timeline animations
    function initializeTimeline() {
        const timelineEvents = $('.timeline-event');

        // Function to check if element is in viewport
        function isElementInViewport(el) {
            const rect = el.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        }

        // Function to animate timeline events
        function animateTimelineEvents() {
            timelineEvents.each(function() {
                if (isElementInViewport(this)) {
                    $(this).animate({
                        opacity: 1
                    }, 1000);
                }
            });
        }

        // Initial animation
        animateTimelineEvents();

        // Animate on scroll using lodash throttle
        $(window).on('scroll', _.throttle(animateTimelineEvents, 100));
    }

    // Initialize timeline when document is ready
    initializeTimeline();

    // Handle window resize
    $(window).on('resize', _.debounce(function() {
        // Recalculate timeline positions if needed
        initializeTimeline();
    }, 250));

    // Smooth scroll to timeline events when clicking year markers
    $('.timeline-year').on('click', function(e) {
        e.preventDefault();
        const year = $(this).data('year');
        const targetEvent = $(`.timeline-event[data-year="${year}"]`);

        if (targetEvent.length) {
            $('html, body').animate({
                scrollTop: targetEvent.offset().top - 100
            }, 1000);
        }
    });
});