$(document).ready(function() {
    // Initialize gallery items with fade-in animation
    function initializeGallery() {
        $('.gallery-item').each(function(index) {
            const item = $(this);
            setTimeout(function() {
                item.removeClass('opacity-0 translate-y-4');
            }, index * 100);
        });
    }

    // Filter gallery items by category
    $('.category-filter').on('click', function() {
        const category = $(this).data('category');

        // Update active state of filter buttons
        $('.category-filter').removeClass('bg-blue-500 text-white').addClass('bg-gray-200 text-gray-700');
        $(this).removeClass('bg-gray-200 text-gray-700').addClass('bg-blue-500 text-white');

        // Filter items
        $('.gallery-item').each(function() {
            const item = $(this);
            if (category === 'all' || item.data('category') === category) {
                item.show();
                setTimeout(() => {
                    item.removeClass('opacity-0 translate-y-4');
                }, 100);
            } else {
                item.addClass('opacity-0 translate-y-4');
                setTimeout(() => {
                    item.hide();
                }, 500);
            }
        });
    });

    // Lightbox functionality
    const lightbox = $('#lightbox');
    const lightboxImage = $('#lightboxImage');
    const lightboxTitle = $('#lightboxTitle');

    // Open lightbox
    $('.gallery-image-container').on('click', function() {
        const imageUrl = $(this).data('image-url');
        const title = $(this).data('title');

        lightboxImage.attr('src', imageUrl);
        lightboxTitle.text(title);
        lightbox.removeClass('hidden').addClass('flex');

        // Prevent body scrolling
        $('body').css('overflow', 'hidden');
    });

    // Close lightbox
    $('#closeLightbox, #lightbox').on('click', function(e) {
        if (e.target === this) {
            lightbox.removeClass('flex').addClass('hidden');
            // Restore body scrolling
            $('body').css('overflow', '');
        }
    });

    // Handle keyboard events for lightbox
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape' && !lightbox.hasClass('hidden')) {
            lightbox.removeClass('flex').addClass('hidden');
            $('body').css('overflow', '');
        }
    });

    // Initialize gallery when document is ready
    initializeGallery();

    // Handle window resize
    $(window).on('resize', _.debounce(function() {
        // Recalculate gallery layout if needed
    }, 250));

    // Lazy load images as they come into view
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img.lazy').forEach(img => {
            imageObserver.observe(img);
        });
    }
});