import os
import re

new_logo_svg = """<svg viewBox="0 0 120 120" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
          <path d="M 0 30 C 0 13.43 13.43 0 30 0 H 90 C 106.57 0 120 13.43 120 30 V 40 C 120 56.57 106.57 70 90 70 H 50 C 38.95 70 30 78.95 30 90 V 120 H 30 C 13.43 120 0 106.57 0 90 V 30 Z" fill="#1D4ED8"/>
          <path d="M 120 90 C 120 106.57 106.57 120 90 120 H 30 C 13.43 120 0 106.57 0 100 V 90 C 0 73.43 13.43 60 30 60 H 70 C 81.05 60 90 51.05 90 40 V 0 H 90 C 106.57 0 120 13.43 120 30 V 90 Z" fill="#38BDF8"/>
        </svg>"""

new_logo_text = """<div class="logo-text">
          <span class="rakan">Rakan</span>
          <span class="pay">Pay</span>
        </div>"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Replace Navbar logo
    # Regex to match the old navbar logo block
    navbar_pattern = re.compile(r'<a href="(index\.html|#)" class="navbar-logo">.*?</a>', re.DOTALL)
    
    new_navbar_logo = f"""<a href="index.html" class="navbar-logo rakanpay-logo">
        {new_logo_svg}
        {new_logo_text}
      </a>"""
    content = navbar_pattern.sub(new_navbar_logo, content)

    # 2. Replace Footer logo (old style)
    footer_pattern = re.compile(r'<div class="footer-logo">.*?</div>', re.DOTALL)
    new_footer_logo = f"""<div class="footer-logo rakanpay-logo">
          {new_logo_svg}
          {new_logo_text}
        </div>"""
    content = footer_pattern.sub(new_footer_logo, content)

    # 3. Replace Footer logo (new style)
    fn_logo_pattern = re.compile(r'<div class="fn-logo">.*?</div>', re.DOTALL)
    new_fn_logo = f"""<div class="fn-logo rakanpay-logo">
          {new_logo_svg}
          {new_logo_text}
        </div>"""
    content = fn_logo_pattern.sub(new_fn_logo, content)

    with open(file, 'w') as f:
        f.write(content)

# Add CSS for new logo
css = """
/* ===== RAKANPAY LOGO ===== */
.rakanpay-logo {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  text-decoration: none !important;
}
.rakanpay-logo svg {
  width: 36px !important;
  height: 36px !important;
}
.rakanpay-logo .logo-text {
  display: flex;
  flex-direction: column;
  line-height: 1.1;
  font-family: 'Inter', sans-serif;
  font-weight: 800;
  font-size: 1.15rem;
  letter-spacing: -0.02em;
}
.rakanpay-logo .rakan {
  color: #38BDF8 !important;
}
.rakanpay-logo .pay {
  color: #1D4ED8 !important;
}

/* Update footer overrides for the new logo */
.footer-logo.rakanpay-logo, .fn-logo.rakanpay-logo {
  margin-bottom: 20px;
}
"""

with open('style.css', 'a') as f:
    f.write(css)

