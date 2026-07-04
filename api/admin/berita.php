<?php
// ============================================
// ADMIN API: BERITA (CRUD)
// ============================================

require_once __DIR__ . '/../../config.php';

$db = getDB();
$method = $_SERVER['REQUEST_METHOD'];

if (!isset($_SESSION['user_id'])) {
    jsonResponse(['error' => 'Unauthorized. Silakan login terlebih dahulu.'], 401);
}

switch ($method) {
    case 'GET':
        $stmt = $db->query("SELECT * FROM berita ORDER BY tanggal DESC");
        jsonResponse(['success' => true, 'data' => $stmt->fetchAll()]);
        break;

    case 'POST':
        $input = json_decode(file_get_contents('php://input'), true);
        if (empty($input)) $input = $_POST;

        $judul      = trim($input['judul'] ?? '');
        $isi        = trim($input['isi'] ?? '');
        $ringkasan  = trim($input['ringkasan'] ?? '');
        $gambar     = trim($input['gambar'] ?? '');
        $tanggal    = $input['tanggal'] ?? date('Y-m-d');
        $is_featured = (int)($input['is_featured'] ?? 0);

        if ($judul === '' || $isi === '') {
            jsonResponse(['error' => 'Judul dan isi berita wajib diisi'], 422);
        }

        // If setting as featured, unset previous featured
        if ($is_featured) {
            $db->exec("UPDATE berita SET is_featured = 0 WHERE is_featured = 1");
        }

        $stmt = $db->prepare("INSERT INTO berita (judul, isi, ringkasan, gambar, tanggal, is_featured) VALUES (:judul, :isi, :ringkasan, :gambar, :tanggal, :is_featured)");
        $stmt->execute([
            ':judul'       => $judul,
            ':isi'         => $isi,
            ':ringkasan'   => $ringkasan,
            ':gambar'      => $gambar,
            ':tanggal'     => $tanggal,
            ':is_featured' => $is_featured
        ]);

        jsonResponse(['success' => true, 'message' => 'Berita berhasil ditambahkan', 'id' => $db->lastInsertId()], 201);
        break;

    case 'PUT':
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID berita wajib diisi'], 422);

        $is_featured = (int)($input['is_featured'] ?? 0);
        if ($is_featured) {
            $db->exec("UPDATE berita SET is_featured = 0 WHERE is_featured = 1");
        }

        $stmt = $db->prepare("UPDATE berita SET judul = :judul, isi = :isi, ringkasan = :ringkasan, gambar = :gambar, tanggal = :tanggal, is_featured = :is_featured WHERE id = :id");
        $stmt->execute([
            ':judul'       => trim($input['judul'] ?? ''),
            ':isi'         => trim($input['isi'] ?? ''),
            ':ringkasan'   => trim($input['ringkasan'] ?? ''),
            ':gambar'      => trim($input['gambar'] ?? ''),
            ':tanggal'     => $input['tanggal'] ?? date('Y-m-d'),
            ':is_featured' => $is_featured,
            ':id'          => $id
        ]);

        jsonResponse(['success' => true, 'message' => 'Berita berhasil diupdate']);
        break;

    case 'DELETE':
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID berita wajib diisi'], 422);

        $stmt = $db->prepare("DELETE FROM berita WHERE id = :id");
        $stmt->execute([':id' => $id]);

        jsonResponse(['success' => true, 'message' => 'Berita berhasil dihapus']);
        break;

    default:
        jsonResponse(['error' => 'Method not allowed'], 405);
}
