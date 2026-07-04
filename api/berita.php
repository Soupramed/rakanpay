<?php
// ============================================
// API BERITA (PUBLIC)
// GET: Ambil daftar berita (featured + list)
// ============================================

require_once __DIR__ . '/../config.php';

$db = getDB();

$page  = isset($_GET['page']) ? max(1, (int)$_GET['page']) : 1;
$limit = isset($_GET['limit']) ? max(1, min(50, (int)$_GET['limit'])) : 6;
$offset = ($page - 1) * $limit;

// Get featured article
$featuredStmt = $db->query("SELECT * FROM berita WHERE is_featured = 1 ORDER BY tanggal DESC LIMIT 1");
$featured = $featuredStmt->fetch();

// Get non-featured articles (or all if no featured)
$countStmt = $db->query("SELECT COUNT(*) as total FROM berita WHERE is_featured = 0");
$total = $countStmt->fetch()['total'];

$stmt = $db->prepare("SELECT * FROM berita WHERE is_featured = 0 ORDER BY tanggal DESC LIMIT :limit OFFSET :offset");
$stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
$stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
$stmt->execute();
$articles = $stmt->fetchAll();

jsonResponse([
    'success'  => true,
    'featured' => $featured,
    'data'     => $articles,
    'pagination' => [
        'page'        => $page,
        'limit'       => $limit,
        'total'       => (int)$total,
        'total_pages' => ceil($total / $limit)
    ]
]);
