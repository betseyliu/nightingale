$(document).ready(function() {
    // Initialize quotes with fade-in animation
    function initializeQuotes() {
        $('.quote-card').each(function(index) {
            const card = $(this);
            setTimeout(function() {
                card.removeClass('opacity-0 translate-y-4');
            }, index * 100);
        });
    }

    // Filter quotes by category
    $('.category-filter').on('click', function() {
        const category = $(this).data('category');

        // Update active state of filter buttons
        $('.category-filter').removeClass('bg-blue-500 text-white').addClass('bg-gray-200 text-gray-700');
        $(this).removeClass('bg-gray-200 text-gray-700').addClass('bg-blue-500 text-white');

        let visibleCount = 0;

        // Filter quotes
        $('.quote-card').each(function() {
            const card = $(this);
            if (category === 'all' || card.data('category') === category) {
                card.show();
                setTimeout(() => {
                    card.removeClass('opacity-0 translate-y-4');
                }, 100);
                visibleCount++;
            } else {
                card.addClass('opacity-0 translate-y-4');
                setTimeout(() => {
                    card.hide();
                }, 500);
            }
        });

        // Show/hide no results message
        if (visibleCount === 0) {
            $('#no-results').removeClass('hidden');
        } else {
            $('#no-results').addClass('hidden');
        }
    });

    // Initialize quotes when document is ready
    initializeQuotes();

    // Handle window resize
    $(window).on('resize', _.debounce(function() {
        // Recalculate layout if needed
    }, 250));

    // Smooth scroll to top when filter is clicked
    $('.category-filter').on('click', function() {
        $('html, body').animate({
            scrollTop: $('.category-filter').first().offset().top - 100
        }, 500);
    });

    // Add hover effect to quote cards
    $('.quote-card').hover(
        function() {
            $(this).find('blockquote').addClass('text-blue-600');
        },
        function() {
            $(this).find('blockquote').removeClass('text-blue-600');
        }
    );

    // Handle keyboard navigation
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape') {
            // Reset filters
            $('.category-filter[data-category="all"]').click();
        }
    });
});