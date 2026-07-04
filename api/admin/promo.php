<?php
// ============================================
// ADMIN API: PROMO (CRUD)
// ============================================

require_once __DIR__ . '/../../config.php';

$db = getDB();
$method = $_SERVER['REQUEST_METHOD'];

if (!isset($_SESSION['user_id'])) {
    jsonResponse(['error' => 'Unauthorized. Silakan login terlebih dahulu.'], 401);
}

switch ($method) {
    case 'GET':
        $stmt = $db->query("SELECT * FROM promo ORDER BY created_at DESC");
        jsonResponse(['success' => true, 'data' => $stmt->fetchAll()]);
        break;

    case 'POST':
        $input = json_decode(file_get_contents('php://input'), true);
        if (empty($input)) $input = $_POST;

        $stmt = $db->prepare("INSERT INTO promo (judul, deskripsi, badge, kategori, headline, sub_headline, gradient_start, gradient_end, tanggal_mulai, tanggal_selesai, is_active) VALUES (:judul, :deskripsi, :badge, :kategori, :headline, :sub_headline, :gradient_start, :gradient_end, :tanggal_mulai, :tanggal_selesai, :is_active)");
        $stmt->execute([
            ':judul'          => trim($input['judul'] ?? ''),
            ':deskripsi'      => trim($input['deskripsi'] ?? ''),
            ':badge'          => trim($input['badge'] ?? 'Promo'),
            ':kategori'       => trim($input['kategori'] ?? ''),
            ':headline'       => trim($input['headline'] ?? ''),
            ':sub_headline'   => trim($input['sub_headline'] ?? ''),
            ':gradient_start' => trim($input['gradient_start'] ?? '#1D4ED8'),
            ':gradient_end'   => trim($input['gradient_end'] ?? '#3B82F6'),
            ':tanggal_mulai'  => $input['tanggal_mulai'] ?? date('Y-m-d'),
            ':tanggal_selesai' => $input['tanggal_selesai'] ?? date('Y-m-d'),
            ':is_active'      => (int)($input['is_active'] ?? 1)
        ]);

        jsonResponse(['success' => true, 'message' => 'Promo berhasil ditambahkan', 'id' => $db->lastInsertId()], 201);
        break;

    case 'PUT':
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID promo wajib diisi'], 422);

        $stmt = $db->prepare("UPDATE promo SET judul = :judul, deskripsi = :deskripsi, badge = :badge, kategori = :kategori, headline = :headline, sub_headline = :sub_headline, gradient_start = :gradient_start, gradient_end = :gradient_end, tanggal_mulai = :tanggal_mulai, tanggal_selesai = :tanggal_selesai, is_active = :is_active WHERE id = :id");
        $stmt->execute([
            ':judul'          => trim($input['judul'] ?? ''),
            ':deskripsi'      => trim($input['deskripsi'] ?? ''),
            ':badge'          => trim($input['badge'] ?? 'Promo'),
            ':kategori'       => trim($input['kategori'] ?? ''),
            ':headline'       => trim($input['headline'] ?? ''),
            ':sub_headline'   => trim($input['sub_headline'] ?? ''),
            ':gradient_start' => trim($input['gradient_start'] ?? '#1D4ED8'),
            ':gradient_end'   => trim($input['gradient_end'] ?? '#3B82F6'),
            ':tanggal_mulai'  => $input['tanggal_mulai'] ?? date('Y-m-d'),
            ':tanggal_selesai' => $input['tanggal_selesai'] ?? date('Y-m-d'),
            ':is_active'      => (int)($input['is_active'] ?? 1),
            ':id'             => $id
        ]);

        jsonResponse(['success' => true, 'message' => 'Promo berhasil diupdate']);
        break;

    case 'DELETE':
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID promo wajib diisi'], 422);

        $stmt = $db->prepare("DELETE FROM promo WHERE id = :id");
        $stmt->execute([':id' => $id]);

        jsonResponse(['success' => true, 'message' => 'Promo berhasil dihapus']);
        break;

    default:
        jsonResponse(['error' => 'Method not allowed'], 405);
}
