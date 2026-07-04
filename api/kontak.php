<?php
// ============================================
// API KONTAK (PUBLIC)
// POST: Simpan pesan dari form kontak
// ============================================

require_once __DIR__ . '/../config.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    jsonResponse(['error' => 'Method not allowed'], 405);
}

$db = getDB();

// Get input data
$input = json_decode(file_get_contents('php://input'), true);

// Fallback to POST data if JSON is empty
if (empty($input)) {
    $input = $_POST;
}

// Validate required fields
$nama   = isset($input['nama']) ? trim($input['nama']) : '';
$email  = isset($input['email']) ? trim($input['email']) : '';
$telepon = isset($input['telepon']) ? trim($input['telepon']) : '';
$subjek = isset($input['subjek']) ? trim($input['subjek']) : '';
$pesan  = isset($input['pesan']) ? trim($input['pesan']) : '';

$errors = [];
if ($nama === '')   $errors[] = 'Nama wajib diisi';
if ($email === '')  $errors[] = 'Email wajib diisi';
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Format email tidak valid';
if ($subjek === '') $errors[] = 'Subjek wajib dipilih';
if ($pesan === '')  $errors[] = 'Pesan wajib diisi';

if (count($errors) > 0) {
    jsonResponse(['error' => 'Validasi gagal', 'details' => $errors], 422);
}

// Insert to database
$stmt = $db->prepare("INSERT INTO kontak_pesan (nama, email, telepon, subjek, pesan) VALUES (:nama, :email, :telepon, :subjek, :pesan)");
$stmt->execute([
    ':nama'    => $nama,
    ':email'   => $email,
    ':telepon' => $telepon,
    ':subjek'  => $subjek,
    ':pesan'   => $pesan
]);

jsonResponse([
    'success' => true,
    'message' => 'Pesan Anda berhasil dikirim! Terima kasih telah menghubungi kami.',
    'id'      => $db->lastInsertId()
], 201);
