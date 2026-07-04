import os

footer_html = """
  <!-- Footer New -->
  <footer class="footer-new">
    <div class="container footer-new-grid">
      <div class="fn-brand">
        <div class="fn-logo">
          <svg viewBox="0 0 40 40" fill="none"><rect width="40" height="40" rx="10" fill="#2563EB"/><path d="M12 12h4l4 8-4 8h-4l4-8-4-8z" fill="white"/><path d="M20 12h4l4 8-4 8h-4l4-8-4-8z" fill="white" opacity="0.7"/></svg>
          <div>RAKAN<span>PONSEL DIGITAL</span></div>
        </div>
        <div class="fn-social">
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          <a href="#" aria-label="TikTok"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1v-3.52a6.37 6.37 0 00-.79-.05A6.34 6.34 0 003.15 15.2a6.34 6.34 0 0010.86-4.43v-7a8.16 8.16 0 004.77 1.53V2a4.84 4.84 0 01-.19-.31z"/></svg></a>
          <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="white"/></svg></a>
        </div>
        <p>CV. RAKAN PONSEL DIGITAL<br>Jl. Muhammadiyah No.59, Batoh, Lueng Bata,<br>Kota Banda Aceh</p>
      </div>
      <div class="fn-links">
        <h4>Layanan</h4>
        <ul>
          <li><a href="#">Support Live Chat</a></li>
          <li><a href="#">QRIS Merchant</a></li>
          <li><a href="#">Pusat Bantuan</a></li>
        </ul>
      </div>
      <div class="fn-links">
        <h4>Lainnya</h4>
        <ul>
          <li><a href="#">Kebijakan Privasi</a></li>
          <li><a href="#">Syarat dan Ketentuan</a></li>
        </ul>
      </div>
      <div class="fn-apps">
        <div class="app-btn-mock">
          <svg viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          <div>
            <span>KOTAK SARAN</span>
            <strong>RAKAN PONSEL DIGITAL</strong>
          </div>
        </div>
        <div class="app-btn-mock google-play">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 3v18l14-9L3 3z"/></svg>
          <div>
            <span>GET IT ON</span>
            <strong>Google Play</strong>
          </div>
        </div>
      </div>
    </div>
    <div class="fn-bottom">
      <p>Copyright 2026 Rakan Ponsel Digital. All Right Reserved.</p>
    </div>
  </footer>
"""

nav_html = """  <nav class="navbar" id="navbar">
    <div class="container">
      <a href="index.html" class="navbar-logo">
        <svg viewBox="0 0 40 40" fill="none"><rect width="40" height="40" rx="10" fill="#2563EB"/><path d="M12 12h4l4 8-4 8h-4l4-8-4-8z" fill="white"/><path d="M20 12h4l4 8-4 8h-4l4-8-4-8z" fill="white" opacity="0.7"/></svg>
        <div>RAKAN<span>PONSEL DIGITAL</span></div>
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="index.html">Beranda</a></li>
        <li><a href="produk.html">Produk</a></li>
        <li><a href="berita.html" class="active">Berita</a></li>
        <li><a href="promo.html">Promo</a></li>
        <li><a href="about.html">Tentang Kami</a></li>
        <li><a href="kontak.html">Kontak</a></li>
      </ul>
      <div class="nav-right">
        <div class="nav-lang">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          ID <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="chevron"><polyline points="6 9 12 15 18 9"/></svg>
        </div>
        <a href="#" class="btn btn-primary">Login</a>
        <button class="mobile-toggle" id="mobileToggle"><span></span><span></span><span></span></button>
      </div>
    </div>
  </nav>"""

berita_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Berita - Rakan Ponsel Digital</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
{nav_html}

  <section class="berita-header-new">
    <h1>Berita</h1>
    <p>Dapatkan berita terkini dari rakan ponsel digital dan tips menarik lainnya</p>
  </section>

  <section class="berita-content-new">
    <div class="container">
      
      <a href="detail-berita.html" class="featured-article">
        <div class="fa-img">
          <img src="news1.png" alt="Featured">
        </div>
        <div class="fa-text">
          <span class="news-date">03 Agustus 2026</span>
          <h2>3 Aplikasi Untuk Bayar Zakat Fitrah Online</h2>
          <p>Bayar zakat fitrah online semakin mudah dengan kemajuan teknologi. Simak artikel berikut untuk rekomendasi aplikasi bayar zakat yang aman dan terpercaya. Bayar zakat fitrah online semakin mudah dengan kemajuan teknologi.</p>
        </div>
      </a>

      <div class="news-grid-new">
"""

for i in range(1, 7):
    img = f"news{(i%3)+1}.png"
    berita_html += f"""
        <a href="detail-berita.html" class="news-card-new">
          <img src="{img}" alt="News">
          <span class="news-date">03 Agustus 2026</span>
          <h3>3 Aplikasi Untuk Bayar Zakat Fitrah Online</h3>
          <p>Bayar zakat fitrah online semakin mudah dengan kemajuan teknologi. Simak artikel berikut untuk rekomendasi aplikasi bayar zakat yang aman dan terpercaya.</p>
        </a>"""

berita_html += f"""
      </div>
    </div>
  </section>

{footer_html}

  <script>
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{ navbar.classList.toggle('scrolled', window.scrollY > 10); }});
  </script>
</body>
</html>"""

with open('berita.html', 'w') as f:
    f.write(berita_html)

detail_berita_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Detail Berita - Rakan Ponsel Digital</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
{nav_html}

  <section class="db-section">
    <div class="container db-layout">
      
      <div class="db-main">
        <h1>3 Aplikasi Untuk Bayar Zakat Fitrah Online</h1>
        <span class="news-date">03 Agustus 2026</span>
        
        <img src="news1.png" alt="Cover" class="db-cover">
        
        <div class="db-body">
          <p>Zakat fitrah merupakan kewajiban bagi umat Islam. Nabi Muhammad SAW mewajibkan zakat fitrah untuk dibayarkan sebelum shalat Idul Fitri setiap tahunnya.</p>
          <p>Semakin berkembangnya teknologi, banyak umat Islam yang membayarkan zakat secara online karena kemudahan yang diberikan untuk menunaikan kewajiban. Hukum pembayaran zakat secara online telah dikaji oleh para ahli. Praktek pembayaran zakat online sah dilakukan dengan mengikuti syarat-syarat tertentu, seperti zakat harus disalurkan secara tunai, pemberi zakat harus menyalurkan zakat di daerah tempat ia tinggal, dan melalui lembaga penyalur zakat yang terpercaya.</p>
          <p>Dompet Dhuafa adalah organisasi yang menerima dan menyalurkan zakat, sedekah, donasi, dsb bagi yang berhak dan membutuhkan. Dompet Dhuafa adalah salah satu pelopor dompet digital untuk pembayaran zakat online.</p>
        </div>

        <div class="db-share">
          <h4>Bagikan Artikel</h4>
          <div class="share-icons-row">
            <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg></a>
            <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg></a>
            <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>
          </div>
        </div>
      </div>

      <div class="db-sidebar">
        <h3>Postingan Terbaru</h3>
        <div class="recent-posts">
"""

for i in range(4):
    detail_berita_html += f"""
          <a href="#" class="recent-post-item">
            <div class="rp-date-badge">
              <strong>12</strong>
              <span>Agt</span>
              <small>2026</small>
            </div>
            <p>Lorem ipsum dolor sit amet, consectetur. Diam quis lacinia duis.</p>
          </a>"""

detail_berita_html += f"""
        </div>
      </div>

    </div>
  </section>

{footer_html}

  <script>
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{ navbar.classList.toggle('scrolled', window.scrollY > 10); }});
  </script>
</body>
</html>"""

with open('detail-berita.html', 'w') as f:
    f.write(detail_berita_html)

css_new = """
/* ===== NAV LANG ===== */
.nav-lang {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-dark);
  margin-right: 16px;
  cursor: pointer;
}
.nav-lang svg { width: 16px; height: 16px; }
.nav-lang svg.chevron { width: 14px; height: 14px; }

/* ===== BERITA NEW ===== */
.berita-header-new {
  text-align: center;
  padding: 120px 0 40px;
}
.berita-header-new h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--secondary);
  margin-bottom: 12px;
}
.berita-header-new p {
  font-size: 1rem;
  color: var(--text-gray);
  max-width: 600px;
  margin: 0 auto;
}

.berita-content-new {
  padding-bottom: 80px;
}

.featured-article {
  display: flex;
  background: var(--white);
  border-radius: var(--radius-xl);
  overflow: hidden;
  margin-bottom: 40px;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s, box-shadow 0.3s;
}
.featured-article:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}
.fa-img {
  flex: 0 0 50%;
}
.fa-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  min-height: 300px;
}
.fa-text {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.news-date {
  font-size: 0.85rem;
  color: var(--text-light);
  font-weight: 600;
  margin-bottom: 12px;
  display: block;
}
.fa-text h2 {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--secondary);
  margin-bottom: 16px;
  line-height: 1.3;
}
.fa-text p {
  color: var(--text-gray);
  line-height: 1.6;
}

.news-grid-new {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
.news-card-new {
  display: block;
  text-decoration: none;
  color: inherit;
}
.news-card-new img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: var(--radius-lg);
  margin-bottom: 16px;
}
.news-card-new h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--secondary);
  margin-bottom: 12px;
  line-height: 1.4;
}
.news-card-new p {
  color: var(--text-gray);
  font-size: 0.95rem;
  line-height: 1.6;
}

/* ===== DETAIL BERITA NEW ===== */
.db-section {
  padding: 120px 0 80px;
}
.db-layout {
  display: flex;
  gap: 60px;
}
.db-main {
  flex: 1;
}
.db-main h1 {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--secondary);
  margin-bottom: 12px;
  line-height: 1.3;
}
.db-cover {
  width: 100%;
  height: auto;
  border-radius: var(--radius-xl);
  margin: 32px 0;
}
.db-body p {
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--text-dark);
  margin-bottom: 24px;
}
.db-share {
  margin-top: 48px;
}
.db-share h4 {
  font-size: 1.1rem;
  margin-bottom: 16px;
  color: var(--secondary);
}
.share-icons-row {
  display: flex;
  gap: 12px;
}
.share-icons-row a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #F1F5F9;
  color: var(--text-gray);
  transition: all 0.2s;
}
.share-icons-row a:hover {
  background: var(--primary);
  color: white;
}
.share-icons-row a svg {
  width: 18px;
  height: 18px;
}

.db-sidebar {
  flex: 0 0 320px;
}
.db-sidebar h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--secondary);
  margin-bottom: 24px;
}
.recent-posts {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.recent-post-item {
  display: flex;
  gap: 16px;
  text-decoration: none;
  color: inherit;
  align-items: flex-start;
}
.rp-date-badge {
  background: #3F2A1D;
  color: white;
  border-radius: 8px;
  padding: 8px 12px;
  text-align: center;
  min-width: 60px;
}
.rp-date-badge strong { display: block; font-size: 1.2rem; font-weight: 800; line-height: 1; }
.rp-date-badge span { display: block; font-size: 0.75rem; font-weight: 600; margin: 2px 0; }
.rp-date-badge small { display: block; font-size: 0.65rem; opacity: 0.8; }
.recent-post-item p {
  font-size: 0.9rem;
  line-height: 1.5;
  color: var(--text-dark);
  font-weight: 500;
}
.recent-post-item:hover p {
  color: var(--primary);
}

/* ===== FOOTER NEW ===== */
.footer-new {
  background: var(--white);
  padding: 60px 0 24px;
  border-top: 1px solid var(--border);
}
.footer-new-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 40px;
}
.fn-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 16px;
}
.fn-logo svg { width: 32px; height: 32px; }
.fn-logo span { font-weight: 400; color: var(--secondary); display: block; font-size: 0.8rem; }
.fn-social {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}
.fn-social a {
  color: var(--text-gray);
  transition: color 0.2s;
}
.fn-social a:hover { color: var(--primary); }
.fn-social svg { width: 20px; height: 20px; }
.fn-brand p {
  font-size: 0.85rem;
  color: var(--text-gray);
  line-height: 1.6;
}

.fn-links h4 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 20px;
}
.fn-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.fn-links li { margin-bottom: 12px; }
.fn-links a {
  color: var(--text-gray);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s;
}
.fn-links a:hover { color: var(--primary); }

.fn-apps {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
}
.app-btn-mock {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1px solid var(--border);
  padding: 8px 16px;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  width: 100%;
  max-width: 200px;
}
.app-btn-mock svg { width: 24px; height: 24px; }
.app-btn-mock div { display: flex; flex-direction: column; text-align: left; }
.app-btn-mock span { font-size: 0.6rem; color: var(--text-gray); text-transform: uppercase; }
.app-btn-mock strong { font-size: 0.85rem; color: var(--secondary); }
.app-btn-mock.google-play { background: #000; color: white; border: none; }
.app-btn-mock.google-play span { color: rgba(255,255,255,0.7); }
.app-btn-mock.google-play strong { color: white; }

.fn-bottom {
  text-align: center;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  font-size: 0.8rem;
  color: var(--text-light);
}

@media (max-width: 1024px) {
  .news-grid-new { grid-template-columns: repeat(2, 1fr); }
  .db-layout { flex-direction: column; }
  .db-sidebar { flex: auto; }
}
@media (max-width: 768px) {
  .featured-article { flex-direction: column; }
  .news-grid-new { grid-template-columns: 1fr; }
  .footer-new-grid { grid-template-columns: 1fr; gap: 32px; }
}
"""

with open('style.css', 'a') as f:
    f.write(css_new)
