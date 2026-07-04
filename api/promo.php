<?php
// ============================================
// API PROMO (PUBLIC)
// GET: Ambil daftar promo dengan filter kategori
// ============================================

require_once __DIR__ . '/../config.php';

$db = getDB();

$kategori = isset($_GET['kategori']) ? trim($_GET['kategori']) : '';

$where = [];
$params = [];

if ($kategori !== '' && $kategori !== 'Semua') {
    $where[] = "kategori = :kategori";
    $params[':kategori'] = $kategori;
}

$whereClause = count($where) > 0 ? 'WHERE ' . implode(' AND ', $where) : '';

$query = "SELECT * FROM promo $whereClause ORDER BY created_at DESC";
$stmt = $db->prepare($query);
$stmt->execute($params);
$promos = $stmt->fetchAll();

// Get unique categories
$catStmt = $db->query("SELECT DISTINCT kategori FROM promo ORDER BY kategori ASC");
$categories = $catStmt->fetchAll(PDO::FETCH_COLUMN);

jsonResponse([
    'success'    => true,
    'data'       => $promos,
    'categories' => $categories
]);
