with open('produk.html', 'r') as f:
    html = f.read()

target = "  </section>\n  <!-- CTA Section -->"
replacement = """  </section>

  <!-- Promo Ad Section -->
  <section class="ad-section">
    <div class="container">
      <div class="ad-banner">
        <div class="ad-content">
          <span class="ad-badge">PROMO SPESIAL</span>
          <h2>Cashback 10% Pembelian Pulsa & Paket Data</h2>
          <p>Dapatkan cashback hingga Rp 50.000 untuk setiap transaksi pulsa dan paket data menggunakan saldo RakanPay. Promo terbatas!</p>
          <a href="promo.html" class="btn btn-white" style="color: var(--primary);">Klaim Sekarang</a>
        </div>
        <div class="ad-visual" style="background: linear-gradient(45deg, #1E3A8A, #3B82F6); position: relative; overflow: hidden;">
          <div style="position: absolute; width: 200px; height: 200px; border-radius: 50%; background: rgba(255,255,255,0.1); top: -50px; right: -50px;"></div>
          <div style="position: absolute; width: 150px; height: 150px; border-radius: 50%; background: rgba(255,255,255,0.1); bottom: -50px; left: -20px;"></div>
          <div style="display: flex; align-items: center; justify-content: center; height: 100%; color: white; font-size: 3rem; font-weight: 900; font-style: italic;">
            -10%
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->"""

html = html.replace(target, replacement)

with open('produk.html', 'w') as f:
    f.write(html)

css = """
/* ===== AD SECTION ===== */
.ad-section {
  padding: 40px 0 60px;
  background: var(--white);
}

.ad-banner {
  display: flex;
  background: var(--primary);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(37, 99, 235, 0.2);
  align-items: stretch;
}

.ad-content {
  flex: 1;
  padding: 48px;
  color: var(--white);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.ad-badge {
  background: rgba(255, 255, 255, 0.2);
  padding: 6px 12px;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1px;
  margin-bottom: 16px;
  backdrop-filter: blur(4px);
}

.ad-content h2 {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 12px;
  line-height: 1.2;
}

.ad-content p {
  font-size: 1rem;
  opacity: 0.9;
  margin-bottom: 24px;
  line-height: 1.6;
  max-width: 500px;
}

.ad-visual {
  flex: 0 0 35%;
  min-height: 100%;
}

@media (max-width: 768px) {
  .ad-banner {
    flex-direction: column-reverse;
  }
  .ad-visual {
    min-height: 200px;
  }
  .ad-content {
    padding: 32px 24px;
  }
  .ad-content h2 {
    font-size: 1.5rem;
  }
}
"""

with open('style.css', 'a') as f:
    f.write(css)

