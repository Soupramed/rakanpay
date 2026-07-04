import re

# 1. Update style.css
with open('style.css', 'r') as f:
    css = f.read()

hero_css_replacement = """
.hero {
  padding-top: 140px;
  padding-bottom: 60px;
  background: transparent;
  position: relative;
}

.hero .container {
  background: linear-gradient(120deg, #7bd1f8 0%, #58a2f1 50%, #87a7f4 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 400px;
  padding: 60px 50px;
  gap: 40px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15);
}

/* Base shape for the curved bottom effect from screenshot */
.hero .container::after {
  content: '';
  position: absolute;
  bottom: -150px;
  left: 30%;
  right: -10%;
  height: 300px;
  background: #658df2;
  border-radius: 50%;
  z-index: 1;
}

.hero-content {
  flex: 1;
  max-width: 560px;
  position: relative;
  z-index: 2;
}

.hero-content h1 {
  font-size: 2.8rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 20px;
  letter-spacing: -0.02em;
  color: #FFFFFF;
}

.hero-content p {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 32px;
  line-height: 1.6;
}

.hero-content .btn-dark {
  background: #1D4ED8;
  color: #fff;
  border: none;
}
.hero-content .btn-dark:hover {
  background: #1E3A8A;
}

.hero-image {
  flex: 1;
  max-width: 500px;
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: flex-end;
}

.hero-image img {
  width: 120%;
  max-width: 600px;
  height: auto;
  margin-right: -40px;
  margin-bottom: -100px;
  display: block;
  transform: translateY(20px);
}
"""

# Regex to replace existing .hero block up to .hero-image img
css_pattern = re.compile(r'\.hero \{.*?(?=\.stats \{)', re.DOTALL)
css = css_pattern.sub(hero_css_replacement + "\n", css)

with open('style.css', 'w') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('hero_mockup.png', 'hero-mockup.png')
html = html.replace('<div class="hero-image">\n        <img src="hero-mockup.png" alt="Rakan Ponsel Digital App" width="420" height="420">\n      </div>', '<div class="hero-image">\n        <img src="hero-mockup.png" alt="Rakan Ponsel Digital App">\n      </div>')

with open('index.html', 'w') as f:
    f.write(html)
