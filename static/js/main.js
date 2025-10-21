// Main JavaScript for wedding theme
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Lazy loading for images
    const lazyImages = [].slice.call(document.querySelectorAll('img[data-src]'));
    if ('IntersectionObserver' in window) {
        let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    let lazyImage = entry.target;
                    lazyImage.src = lazyImage.dataset.src;
                    lazyImage.classList.remove('lazy');
                    lazyImageObserver.unobserve(lazyImage);
                }
            });
        });

        lazyImages.forEach(function(lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    }
});

// Smooth page transitions
function setupPageTransitions() {
    // Prevent flash of content during page load
    document.addEventListener('DOMContentLoaded', function() {
        // Add fade-in to main content after entrance animation
        setTimeout(function() {
            const mainContent = document.querySelector('main');
            if (mainContent) {
                mainContent.style.opacity = '0';
                mainContent.style.transition = 'opacity 0.5s ease';
                
                setTimeout(function() {
                    mainContent.style.opacity = '1';
                }, 100);
            }
        }, 1600); // Match this with CSS animation duration
    });

    // Add loading state to navigation links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            // Only for internal links
            if (this.href && this.href.startsWith(window.location.origin)) {
                const linkText = this.textContent.trim();
                if (linkText === 'Gallery' || linkText === 'Blog') {
                    // The entrance animation will handle the transition
                    return;
                }
            }
        });
    });
}

// Initialize page transitions
setupPageTransitions();