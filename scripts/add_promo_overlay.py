import re

# 1. Update style.css
with open('style.css', 'r') as f:
    css = f.read()

promo_css = """
/* Hero Promo Overlay */
.hero-promo-overlay {
  position: absolute;
  top: 25%;
  left: -5%;
  right: 5%;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.2), 0 5px 15px rgba(0,0,0,0.1);
  overflow: hidden;
  z-index: 10;
  display: flex;
  flex-direction: column;
  border: 2px solid #fff;
  transform: scale(0.9) rotate(-1deg);
}

.hpo-header {
  background: #0ea5e9;
  color: #fff;
  font-size: 0.6rem;
  font-weight: 600;
  padding: 6px 10px;
  text-align: left;
}

.hpo-body {
  background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%);
  display: flex;
  align-items: center;
  padding: 12px 15px;
  gap: 15px;
}

.hpo-text {
  flex: 1;
  text-align: left;
}

.hpo-text h4 {
  color: #fff;
  font-size: 1.1rem;
  font-weight: 900;
  margin-bottom: 4px;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
  line-height: 1.1;
}

.hpo-text p {
  color: rgba(255,255,255,0.9);
  font-size: 0.55rem;
  line-height: 1.3;
  margin-bottom: 0;
}

.hpo-qr {
  background: #fff;
  padding: 4px;
  border-radius: 6px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.hpo-qr svg {
  width: 100%;
  height: 100%;
}
"""

if "/* Hero Promo Overlay */" not in css:
    css += "\n" + promo_css

with open('style.css', 'w') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

overlay_html = """      <div class="hero-image" style="position: relative;">
        <img src="hero-mockup.png" alt="Rakan Ponsel Digital App">
        <div class="hero-promo-overlay">
          <div class="hpo-header">Selamat Datang Kembali Di Aplikasi RAKAN PONSEL, Se...</div>
          <div class="hpo-body">
            <div class="hpo-text">
              <h4>BIKIN QRIS TOKO<br>GRATISSS !!!</h4>
              <p>Tingkatkan penjualan toko Anda dengan menerima semua pembayaran e-Wallet cukup dengan 1 QRIS!</p>
            </div>
            <div class="hpo-qr">
              <svg viewBox="0 0 24 24" fill="#000"><path d="M3 3h6v6H3V3zm2 2v2h2V5H5zm8-2h6v6h-6V3zm2 2v2h2V5h-2zM3 13h6v6H3v-6zm2 2v2h2v-2H5zm13-2h-3v2h3v-2zm-3 4h3v2h-3v-2zm-2-6h2v2h-2v-2zm0 4h2v2h-2v-2zm-2-2h2v2h-2v-2zm0 4h2v2h-2v-2zm-2-6h2v2h-2v-2zm0 4h2v2h-2v-2z"/></svg>
            </div>
          </div>
        </div>
      </div>"""

html = html.replace('<div class="hero-image">\n        <img src="hero-mockup.png" alt="Rakan Ponsel Digital App">\n      </div>', overlay_html)

with open('index.html', 'w') as f:
    f.write(html)
