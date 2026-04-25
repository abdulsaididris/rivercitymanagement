import os
import re

locations = [
    "Edmonton", "St. Albert", "Spruce Grove", "Stony Plain", "Leduc", "Beaumont", 
    "Fort Saskatchewan", "Sherwood Park", "Devon", "Morinville", "Legal", "Gibbons", 
    "Bon Accord", "Redwater", "Smoky Lake", "Lamont", "Andrew", "Mundare", "Vegreville", 
    "Tofield", "Ryley", "Holden", "Bruce", "Viking", "Kinsella", "Irma", "Wainwright", 
    "Vermilion", "Myrnam", "Two Hills", "St. Paul", "Elk Point", "Athabasca", "Westlock", 
    "Barrhead", "Mayerthorpe", "Sangudo", "Whitecourt", "Fox Creek", "Wabamun", 
    "Entwistle", "Evansburg", "Drayton Valley", "Breton", "Thorsby", "Calmar", "Warburg", 
    "Wetaskiwin", "Millet", "Maskwacis", "Ponoka", "Lacombe", "Blackfalds", "Red Deer", 
    "Penhold", "Sylvan Lake", "Bentley", "Rimbey", "Rocky Mountain House", "Stettler", 
    "Camrose", "Bawlf", "Daysland", "Killam", "Sedgewick", "Forestburg", "Hardisty", 
    "Lougheed", "Alliance", "Coronation", "Lac La Biche", "Bonnyville"
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{location} Property Management | River City Management | Full-Cycle Services</title>
    <meta name="description" content="Looking for the best {location} Property Management? River City Management offers premium rental, maintenance, and security solutions for condos and apartments in {location}, AB.">
    
    <link rel="stylesheet" href="style.css">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <header id="header" class="scrolled">
        <div class="container">
            <nav>
                <a href="index.html" class="logo">
                    <i data-lucide="building-2"></i>
                    River City <span>Management</span>
                </a>
                <div class="menu-toggle" id="mobile-menu">
                    <i data-lucide="menu"></i>
                </div>
                <ul class="nav-links">
                    <li><a href="index.html#services">Services</a></li>
                    <li><a href="index.html#security">Security</a></li>
                    <li><a href="index.html#blog">Insights</a></li>
                    <li><a href="index.html#contact">Contact</a></li>
                    <li class="mobile-only"><a href="index.html#portal" class="btn-portal">Client Portal</a></li>
                </ul>
                <a href="index.html#portal" class="btn-portal nav-cta">Client Portal</a>
            </nav>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero" style="background-image: linear-gradient(to right, rgba(5, 10, 20, 0.95), rgba(5, 10, 20, 0.6)), url('hero-bg.png');">
            <div class="container">
                <div class="hero-content animate-fade-in">
                    <h1>Premium <span>{location} Property Management</span> Solutions.</h1>
                    <p>Experience the future of property ownership in {location}. We handle the full cycle—from seamless rentals to intelligent maintenance and state-of-the-art building security.</p>
                    <div class="cta-group">
                        <a href="#contact" class="btn-portal">Get a Free Quote</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Main Content -->
        <section class="container" style="padding: 100px 0;">
            <div class="grid split-grid">
                <div class="text-content">
                    <h2>Expert Property Management in {location}</h2>
                    <p>When it comes to <strong>{location} property management</strong>, River City Management stands alone. We combine local expertise with cutting-edge technology to protect your investment and maximize your returns in {location} and the surrounding Alberta areas.</p>
                    <p style="margin-top: 1rem;">Our team understands the unique challenges of the {location} rental market, from seasonal maintenance to neighborhood-specific tenant placement. Whether you own a single condo or a multi-family building, we provide the localized care your property deserves.</p>
                    
                    <h3 style="margin-top: 2rem; color: var(--primary-light);">Why Choose Us for Your {location} Property?</h3>
                    <ul class="check-list" style="margin-top: 1rem;">
                        <li><i data-lucide="check-circle"></i> Local {location} Market Knowledge</li>
                        <li><i data-lucide="check-circle"></i> 24/7 Edmonton-Based Support</li>
                        <li><i data-lucide="check-circle"></i> Specialized Condo Management Services</li>
                        <li><i data-lucide="check-circle"></i> Proprietary Security & Delivery Systems</li>
                    </ul>
                </div>
                <div class="image-content">
                    <img src="portal-mockup.png" alt="River City Management Portal" class="mockup">
                </div>
            </div>
        </section>

        <!-- Services Section -->
        <section id="services" class="container" style="padding-top: 0;">
            <div class="section-title">
                <h2>Our Services in {location}</h2>
                <p>Comprehensive solutions for {location} property owners.</p>
            </div>
            <div class="grid">
                <div class="card glass">
                    <i data-lucide="key"></i>
                    <h3>Residential Rentals</h3>
                    <p>Expert marketing, tenant screening, and lease management for your {location} rental units.</p>
                </div>
                <div class="card glass">
                    <i data-lucide="wrench"></i>
                    <h3>Full-Cycle Maintenance</h3>
                    <p>24/7 emergency response and proactive preventative maintenance for buildings in {location}.</p>
                </div>
                <div class="card glass">
                    <i data-lucide="shield-check"></i>
                    <h3>Smart Security</h3>
                    <p>Proprietary building access control and delivery management systems for modern safety.</p>
                </div>
            </div>
        </section>

        <!-- Lead Capture Form Section -->
        <section id="contact" class="container">
            <div class="glass lead-form-container">
                <h2>Manage Your {location} Property with Confidence</h2>
                <span class="subtitle">Start Saving with Our FREE Price & Process Guide.</span>
                <p style="color: var(--text-gray); margin-bottom: 2rem;">We specialize in properties with 6+ units in {location}. Complete the form below to receive your custom proposal.</p>
                
                <form id="contact-form" action="https://api.web3forms.com/submit" method="POST">
                    <input type="hidden" name="access_key" value="2fdacc40-4270-4e1f-b482-b539e3c52bbe">
                    <input type="hidden" name="location" value="{location}">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="first_name">First Name</label>
                            <input type="text" id="first_name" name="first_name" required placeholder="John">
                        </div>
                        <div class="form-group">
                            <label for="last_name">Last Name</label>
                            <input type="text" id="last_name" name="last_name" required placeholder="Doe">
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" id="email" name="email" required placeholder="john@example.com">
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" name="phone" required placeholder="(780) 000-0000">
                        </div>
                    </div>
                    <button type="submit" class="btn-submit">Get My Free Guide & Proposal for {location}</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <a href="index.html" class="logo">
                        <i data-lucide="building-2"></i>
                        River City <span>Management</span>
                    </a>
                    <p>Edmonton's premier partner for full-cycle property management and building security solutions.</p>
                </div>
                <div class="footer-links">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="index.html#services">Rental Management</a></li>
                        <li><a href="index.html#services">Maintenance</a></li>
                        <li><a href="index.html#security">Security Systems</a></li>
                        <li><a href="index.html#services">Condo Management</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="index.html#blog">Insights</a></li>
                        <li><a href="index.html#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Contact</h4>
                    <p style="color: var(--text-gray);">Edmonton, AB<br>a.said@lagroupofcompanies.ca<br>(780) 479-3285</p>
                </div>
            </div>
            
            <p style="text-align: center; margin-top: 4rem; color: var(--text-gray); font-size: 0.9rem;">
                &copy; 2026 River City Management. Serving {location} and surrounding areas.
            </p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
\"\"\"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    text = text.replace(' ', '-')
    return text

output_dir = r"c:\\Users\\asaid\\.gemini\\antigravity\\scratch\\river-city-management"

for loc in locations:
    filename = f"property-management-{slugify(loc)}.html"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template.format(location=loc))
    print(f"Generated: {filename}")
