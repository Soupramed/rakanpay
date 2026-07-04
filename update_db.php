<?php
require_once 'config.php';

echo "<h1>Database Update</h1>";

try {
    $db = getDB();
    
    // Create kontak_pesan table if it doesn't exist
    $query = "CREATE TABLE IF NOT EXISTS kontak_pesan (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nama VARCHAR(100) NOT NULL,
      email VARCHAR(100) NOT NULL,
      telepon VARCHAR(20) DEFAULT NULL,
      subjek VARCHAR(50) NOT NULL,
      pesan TEXT NOT NULL,
      is_read TINYINT(1) DEFAULT 0,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;";
    
    $db->exec($query);
    echo "<p style='color: green;'>✅ Tabel <b>kontak_pesan</b> berhasil dibuat/sudah ada.</p>";

    echo "<p><a href='index.html'>Kembali ke Beranda</a></p>";
} catch (PDOException $e) {
    echo "<p style='color: red;'>❌ Terjadi kesalahan: " . $e->getMessage() . "</p>";
}
