document.addEventListener('DOMContentLoaded', () => {
    const header = document.getElementById('header');
    
    // Header Scroll Effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Smooth Scrolling for Nav Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple Intersection Observer for Animations
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .section-title, .mockup').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });

    // Contact Form Submission (Web3Forms AJAX)
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const firstName = formData.get('first_name');
            const submitBtn = contactForm.querySelector('.btn-submit');
            
            // Visual feedback
            const originalBtnText = submitBtn.innerText;
            submitBtn.innerText = 'Sending...';
            submitBtn.disabled = true;

            try {
                const response = await fetch('https://api.web3forms.com/submit', {
                    method: 'POST',
                    body: formData
                });

                const result = await response.json();

                if (result.success) {
                    alert(`Thank you, ${firstName}! Your FREE Price & Process Guide is being sent to your email. Our Edmonton team will follow up shortly.`);
                    contactForm.reset();
                } else {
                    alert('Something went wrong. Please try again or contact us directly.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please check your connection and try again.');
            } finally {
                submitBtn.innerText = originalBtnText;
                submitBtn.disabled = false;
            }
        });
    }
});
