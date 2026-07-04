-- ============================================
-- DATABASE RAKANPAY
-- Rakan Ponsel Digital - Payment System
-- ============================================

CREATE DATABASE IF NOT EXISTS rakanpay
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE rakanpay;

-- ============================================
-- TABEL: users (Admin)
-- ============================================
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'editor') DEFAULT 'admin',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================
-- TABEL: produk
-- ============================================
CREATE TABLE IF NOT EXISTS produk (
  id INT AUTO_INCREMENT PRIMARY KEY,
  kode VARCHAR(20) NOT NULL UNIQUE,
  kategori VARCHAR(50) NOT NULL,
  nama_produk VARCHAR(150) NOT NULL,
  status ENUM('Tersedia', 'Harga Turun', 'Harga Naik', 'Gangguan') DEFAULT 'Tersedia',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================
-- TABEL: promo
-- ============================================
CREATE TABLE IF NOT EXISTS promo (
  id INT AUTO_INCREMENT PRIMARY KEY,
  judul VARCHAR(200) NOT NULL,
  deskripsi TEXT NOT NULL,
  badge VARCHAR(50) DEFAULT 'Promo',
  kategori VARCHAR(50) NOT NULL,
  headline VARCHAR(100) NOT NULL,
  sub_headline VARCHAR(150) DEFAULT NULL,
  gradient_start VARCHAR(7) DEFAULT '#1D4ED8',
  gradient_end VARCHAR(7) DEFAULT '#3B82F6',
  tanggal_mulai DATE NOT NULL,
  tanggal_selesai DATE NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================
-- TABEL: berita
-- ============================================
CREATE TABLE IF NOT EXISTS berita (
  id INT AUTO_INCREMENT PRIMARY KEY,
  judul VARCHAR(200) NOT NULL,
  isi TEXT NOT NULL,
  ringkasan VARCHAR(500) DEFAULT NULL,
  gambar VARCHAR(255) DEFAULT NULL,
  tanggal DATE NOT NULL,
  is_featured TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================
-- TABEL: kontak_pesan
-- ============================================
CREATE TABLE IF NOT EXISTS kontak_pesan (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  telepon VARCHAR(20) DEFAULT NULL,
  subjek VARCHAR(50) NOT NULL,
  pesan TEXT NOT NULL,
  is_read TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;


-- ============================================
-- SEED DATA
-- ============================================

-- Admin default (password: admin123)
INSERT INTO users (nama, email, password, role) VALUES
('Administrator', 'admin@rakanponsel.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin');

-- Produk
INSERT INTO produk (kode, kategori, nama_produk, status) VALUES
('S5', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 5.000', 'Tersedia'),
('S10', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 10.000', 'Harga Turun'),
('PL20', 'Token', 'Token Listrik Standart 20.000', 'Harga Naik'),
('STP25', 'Pulsa Transfer', 'Pulsa Transfer Telkomsel 25.000', 'Tersedia'),
('T25', 'Pulsa Reguler', 'Pulsa Reguler Three 25.000', 'Tersedia'),
('IN45', 'Pulsa Reguler', 'Pulsa Reguler Indosat 45.000', 'Harga Turun'),
('SM50', 'Pulsa Reguler', 'Pulsa Reguler Smartfren 50.000', 'Tersedia'),
('SM70', 'Pulsa Reguler', 'Pulsa Reguler Smartfren 70.000', 'Tersedia'),
('LA90', 'e-Wallet', 'Saldo LinkAja 90.000', 'Gangguan'),
('LA100', 'e-Wallet', 'Saldo LinkAja 100.000', 'Harga Naik'),
('S15', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 15.000', 'Tersedia'),
('S20', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 20.000', 'Tersedia'),
('S25', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 25.000', 'Tersedia'),
('S50', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 50.000', 'Tersedia'),
('S100', 'Pulsa Reguler', 'Pulsa Reguler Telkomsel 100.000', 'Tersedia'),
('XL10', 'Pulsa Reguler', 'Pulsa Reguler XL 10.000', 'Tersedia'),
('XL25', 'Pulsa Reguler', 'Pulsa Reguler XL 25.000', 'Harga Turun'),
('XL50', 'Pulsa Reguler', 'Pulsa Reguler XL 50.000', 'Tersedia'),
('IN10', 'Pulsa Reguler', 'Pulsa Reguler Indosat 10.000', 'Tersedia'),
('IN25', 'Pulsa Reguler', 'Pulsa Reguler Indosat 25.000', 'Tersedia'),
('PL50', 'Token', 'Token Listrik Standart 50.000', 'Tersedia'),
('PL100', 'Token', 'Token Listrik Standart 100.000', 'Tersedia'),
('PL200', 'Token', 'Token Listrik Standart 200.000', 'Tersedia'),
('GP50', 'e-Wallet', 'Saldo GoPay 50.000', 'Tersedia'),
('GP100', 'e-Wallet', 'Saldo GoPay 100.000', 'Tersedia'),
('OV50', 'e-Wallet', 'Saldo OVO 50.000', 'Tersedia'),
('OV100', 'e-Wallet', 'Saldo OVO 100.000', 'Harga Naik'),
('DN50', 'e-Wallet', 'Saldo DANA 50.000', 'Tersedia'),
('DN100', 'e-Wallet', 'Saldo DANA 100.000', 'Tersedia'),
('SP50', 'e-Wallet', 'Saldo ShopeePay 50.000', 'Tersedia');

-- Promo
INSERT INTO promo (judul, deskripsi, badge, kategori, headline, sub_headline, gradient_start, gradient_end, tanggal_mulai, tanggal_selesai) VALUES
('Cashback 10% Pulsa Telkomsel', 'Dapatkan cashback hingga 10% untuk setiap pembelian pulsa Telkomsel minimal Rp50.000. Berlaku untuk semua pengguna baru dan lama tanpa batas kuota promo.', 'Hot', 'Pulsa', 'CASHBACK 10%', 'Pembelian Pulsa Telkomsel', '#EF4444', '#B91C1C', '2024-12-01', '2024-12-31'),
('Diskon 15% Paket Data XL', 'Nikmati diskon spesial 15% untuk pembelian paket data XL Axiata mulai dari paket 5GB hingga 30GB. Cocok untuk kebutuhan streaming, kerja, dan belajar online.', 'Terbatas', 'Paket Data', 'DISKON 15%', 'Paket Data XL Hingga 30GB', '#F59E0B', '#B45309', '2024-12-05', '2024-12-25'),
('Bonus Saldo E-Wallet Rp25.000', 'Top up saldo e-wallet favorit Anda (GoPay, OVO, Dana, ShopeePay) minimal Rp100.000 dan dapatkan bonus saldo Rp25.000 langsung masuk ke akun Anda.', 'Baru', 'E-Wallet', 'BONUS Rp25K', 'Top Up GoPay, OVO, Dana', '#8B5CF6', '#6D28D9', '2024-12-10', '2024-12-31'),
('Gratis Biaya Admin PPOB', 'Bayar tagihan listrik, air PDAM, BPJS, internet, dan cicilan tanpa biaya administrasi. Promo berlaku untuk seluruh jenis tagihan PPOB selama periode promo.', 'Promo', 'PPOB', 'GRATIS ADMIN', 'Semua Tagihan PPOB', '#06B6D4', '#0E7490', '2024-12-01', '2025-01-15');

-- Berita
INSERT INTO berita (judul, isi, ringkasan, gambar, tanggal, is_featured) VALUES
('3 Aplikasi Untuk Bayar Zakat Fitrah Online', 'Bayar zakat fitrah online semakin mudah dengan kemajuan teknologi. Berikut ini adalah 3 aplikasi terbaik yang bisa Anda gunakan untuk menunaikan zakat fitrah secara online dengan aman dan terpercaya.\n\n1. RakanPay - Platform pembayaran digital terlengkap yang menyediakan fitur bayar zakat fitrah langsung dari smartphone Anda.\n\n2. Tokopedia - Marketplace terbesar di Indonesia yang juga menyediakan layanan pembayaran zakat melalui lembaga-lembaga zakat resmi.\n\n3. Kitabisa - Platform donasi dan zakat online yang bekerja sama dengan berbagai lembaga amil zakat nasional.', 'Bayar zakat fitrah online semakin mudah dengan kemajuan teknologi. Simak artikel berikut untuk rekomendasi aplikasi bayar zakat yang aman dan terpercaya.', 'news1.png', '2026-08-03', 1),
('Tips Hemat Beli Pulsa dan Paket Data', 'Membeli pulsa dan paket data secara rutin bisa menjadi pengeluaran yang cukup besar jika tidak dikelola dengan baik. Berikut beberapa tips yang bisa membantu Anda menghemat pengeluaran untuk pulsa dan paket data.\n\n1. Manfaatkan promo cashback dari platform pembayaran digital.\n2. Pilih paket data yang sesuai dengan kebutuhan.\n3. Gunakan WiFi ketika tersedia untuk menghemat kuota.', 'Membeli pulsa dan paket data bisa hemat dengan tips-tips berikut. Simak strategi pintar agar pengeluaran digital Anda lebih efisien.', 'news2.png', '2026-08-03', 0),
('Cara Mudah Bayar Tagihan Listrik Online', 'Membayar tagihan listrik kini bisa dilakukan dari mana saja tanpa perlu antri di loket pembayaran. Dengan menggunakan aplikasi pembayaran digital seperti RakanPay, Anda bisa membayar tagihan listrik bulanan dengan cepat dan mudah.\n\nCukup masukkan nomor meter atau ID pelanggan, pilih nominal pembayaran, dan konfirmasi transaksi. Pembayaran akan diproses dalam hitungan detik.', 'Bayar tagihan listrik online tanpa antri. Simak cara mudahnya menggunakan aplikasi pembayaran digital terpercaya.', 'news3.png', '2026-08-03', 0),
('Keuntungan Menggunakan E-Wallet di Era Digital', 'E-Wallet atau dompet digital telah menjadi bagian penting dari kehidupan sehari-hari masyarakat Indonesia. Dengan berbagai kemudahan yang ditawarkan, e-wallet menjadi pilihan utama untuk berbagai transaksi.\n\nBeberapa keuntungan menggunakan e-wallet antara lain: transaksi lebih cepat, banyak promo dan cashback, aman karena dilindungi PIN dan biometrik, serta bisa digunakan di berbagai merchant.', 'E-Wallet menawarkan banyak keuntungan di era digital. Simak berbagai manfaat menggunakan dompet digital untuk transaksi sehari-hari.', 'news1.png', '2026-08-03', 0),
('Panduan Lengkap Top Up Saldo Game Online', 'Top up saldo game online kini semakin mudah dengan hadirnya berbagai platform pembayaran digital. Tidak perlu lagi membeli voucher fisik di toko-toko game.\n\nRakanPay menyediakan layanan top up untuk berbagai game populer seperti Mobile Legends, Free Fire, PUBG Mobile, Genshin Impact, dan masih banyak lagi.', 'Top up saldo game online kini lebih mudah dengan platform pembayaran digital. Simak panduan lengkapnya di sini.', 'news2.png', '2026-08-03', 0),
('Update Terbaru Fitur RakanPay 2026', 'RakanPay terus berinovasi untuk memberikan pengalaman terbaik bagi para penggunanya. Di tahun 2026, kami menghadirkan beberapa fitur baru yang akan membuat transaksi Anda semakin mudah dan menyenangkan.\n\nFitur-fitur baru meliputi: QR Payment, Transfer Antar Bank Gratis, Notifikasi Real-time, dan Dashboard Analitik untuk mitra bisnis.', 'RakanPay menghadirkan fitur-fitur baru di tahun 2026. Simak update terbaru yang akan memudahkan transaksi digital Anda.', 'news3.png', '2026-08-03', 0);
