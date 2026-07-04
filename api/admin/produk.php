<?php
// ============================================
// ADMIN API: PRODUK (CRUD)
// ============================================

require_once __DIR__ . '/../../config.php';

$db = getDB();
$method = $_SERVER['REQUEST_METHOD'];

// Check admin session
if (!isset($_SESSION['user_id'])) {
    jsonResponse(['error' => 'Unauthorized. Silakan login terlebih dahulu.'], 401);
}

switch ($method) {
    case 'GET':
        // List all produk
        $stmt = $db->query("SELECT * FROM produk ORDER BY created_at DESC");
        jsonResponse(['success' => true, 'data' => $stmt->fetchAll()]);
        break;

    case 'POST':
        // Tambah produk baru
        $input = json_decode(file_get_contents('php://input'), true);
        if (empty($input)) $input = $_POST;

        $kode        = trim($input['kode'] ?? '');
        $kategori    = trim($input['kategori'] ?? '');
        $nama_produk = trim($input['nama_produk'] ?? '');
        $status      = trim($input['status'] ?? 'Tersedia');

        if ($kode === '' || $kategori === '' || $nama_produk === '') {
            jsonResponse(['error' => 'Kode, kategori, dan nama produk wajib diisi'], 422);
        }

        // Check kode unik
        $check = $db->prepare("SELECT id FROM produk WHERE kode = :kode");
        $check->execute([':kode' => $kode]);
        if ($check->fetch()) {
            jsonResponse(['error' => 'Kode produk sudah digunakan'], 422);
        }

        $stmt = $db->prepare("INSERT INTO produk (kode, kategori, nama_produk, status) VALUES (:kode, :kategori, :nama_produk, :status)");
        $stmt->execute([
            ':kode'        => $kode,
            ':kategori'    => $kategori,
            ':nama_produk' => $nama_produk,
            ':status'      => $status
        ]);

        jsonResponse(['success' => true, 'message' => 'Produk berhasil ditambahkan', 'id' => $db->lastInsertId()], 201);
        break;

    case 'PUT':
        // Edit produk
        $input = json_decode(file_get_contents('php://input'), true);

        $id          = (int)($input['id'] ?? 0);
        $kode        = trim($input['kode'] ?? '');
        $kategori    = trim($input['kategori'] ?? '');
        $nama_produk = trim($input['nama_produk'] ?? '');
        $status      = trim($input['status'] ?? 'Tersedia');

        if ($id === 0) {
            jsonResponse(['error' => 'ID produk wajib diisi'], 422);
        }

        $stmt = $db->prepare("UPDATE produk SET kode = :kode, kategori = :kategori, nama_produk = :nama_produk, status = :status WHERE id = :id");
        $stmt->execute([
            ':kode'        => $kode,
            ':kategori'    => $kategori,
            ':nama_produk' => $nama_produk,
            ':status'      => $status,
            ':id'          => $id
        ]);

        jsonResponse(['success' => true, 'message' => 'Produk berhasil diupdate']);
        break;

    case 'DELETE':
        // Hapus produk
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) {
            jsonResponse(['error' => 'ID produk wajib diisi'], 422);
        }

        $stmt = $db->prepare("DELETE FROM produk WHERE id = :id");
        $stmt->execute([':id' => $id]);

        jsonResponse(['success' => true, 'message' => 'Produk berhasil dihapus']);
        break;

    default:
        jsonResponse(['error' => 'Method not allowed'], 405);
}
