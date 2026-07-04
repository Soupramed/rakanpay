<?php
// ============================================
// API PRODUK (PUBLIC)
// GET: Ambil daftar produk dengan search, filter, pagination
// ============================================

require_once __DIR__ . '/../config.php';

$db = getDB();

// Parameters
$search   = isset($_GET['search']) ? trim($_GET['search']) : '';
$kategori = isset($_GET['kategori']) ? trim($_GET['kategori']) : '';
$sort     = isset($_GET['sort']) ? trim($_GET['sort']) : 'newest';
$page     = isset($_GET['page']) ? max(1, (int)$_GET['page']) : 1;
$limit    = isset($_GET['limit']) ? max(1, min(100, (int)$_GET['limit'])) : 10;
$offset   = ($page - 1) * $limit;

// Build query
$where = [];
$params = [];

if ($search !== '') {
    $where[] = "(kode LIKE :search OR nama_produk LIKE :search2 OR kategori LIKE :search3)";
    $params[':search']  = "%$search%";
    $params[':search2'] = "%$search%";
    $params[':search3'] = "%$search%";
}

if ($kategori !== '') {
    $where[] = "kategori = :kategori";
    $params[':kategori'] = $kategori;
}

$whereClause = count($where) > 0 ? 'WHERE ' . implode(' AND ', $where) : '';

// Sort
$orderBy = 'ORDER BY created_at DESC';
if ($sort === 'oldest') $orderBy = 'ORDER BY created_at ASC';
if ($sort === 'name')   $orderBy = 'ORDER BY nama_produk ASC';
if ($sort === 'kode')   $orderBy = 'ORDER BY kode ASC';

// Count total
$countQuery = "SELECT COUNT(*) as total FROM produk $whereClause";
$stmt = $db->prepare($countQuery);
$stmt->execute($params);
$total = $stmt->fetch()['total'];

// Fetch data
$query = "SELECT * FROM produk $whereClause $orderBy LIMIT :limit OFFSET :offset";
$stmt = $db->prepare($query);
foreach ($params as $key => $val) {
    $stmt->bindValue($key, $val);
}
$stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
$stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
$stmt->execute();
$produk = $stmt->fetchAll();

// Get unique categories for filter
$catStmt = $db->query("SELECT DISTINCT kategori FROM produk ORDER BY kategori ASC");
$categories = $catStmt->fetchAll(PDO::FETCH_COLUMN);

jsonResponse([
    'success' => true,
    'data'    => $produk,
    'categories' => $categories,
    'pagination' => [
        'page'       => $page,
        'limit'      => $limit,
        'total'      => (int)$total,
        'total_pages' => ceil($total / $limit)
    ]
]);
