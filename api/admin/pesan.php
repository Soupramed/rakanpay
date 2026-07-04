<?php
// ============================================
// ADMIN API: PESAN KONTAK
// GET: List pesan, PUT: Tandai dibaca, DELETE: Hapus
// ============================================

require_once __DIR__ . '/../../config.php';

$db = getDB();
$method = $_SERVER['REQUEST_METHOD'];

if (!isset($_SESSION['user_id'])) {
    jsonResponse(['error' => 'Unauthorized. Silakan login terlebih dahulu.'], 401);
}

switch ($method) {
    case 'GET':
        $stmt = $db->query("SELECT * FROM kontak_pesan ORDER BY created_at DESC");
        $pesan = $stmt->fetchAll();

        // Count unread
        $unreadStmt = $db->query("SELECT COUNT(*) as unread FROM kontak_pesan WHERE is_read = 0");
        $unread = $unreadStmt->fetch()['unread'];

        jsonResponse([
            'success' => true,
            'data'    => $pesan,
            'unread'  => (int)$unread
        ]);
        break;

    case 'PUT':
        // Mark as read
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID pesan wajib diisi'], 422);

        $stmt = $db->prepare("UPDATE kontak_pesan SET is_read = 1 WHERE id = :id");
        $stmt->execute([':id' => $id]);

        jsonResponse(['success' => true, 'message' => 'Pesan ditandai sudah dibaca']);
        break;

    case 'DELETE':
        $input = json_decode(file_get_contents('php://input'), true);
        $id = (int)($input['id'] ?? 0);

        if ($id === 0) jsonResponse(['error' => 'ID pesan wajib diisi'], 422);

        $stmt = $db->prepare("DELETE FROM kontak_pesan WHERE id = :id");
        $stmt->execute([':id' => $id]);

        jsonResponse(['success' => true, 'message' => 'Pesan berhasil dihapus']);
        break;

    default:
        jsonResponse(['error' => 'Method not allowed'], 405);
}
