<?php
// ============================================
// API AUTH (Login)
// POST: Login admin
// GET:  Check session
// ============================================

require_once __DIR__ . '/../config.php';

$db = getDB();

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'POST') {
    // LOGIN
    $input = json_decode(file_get_contents('php://input'), true);
    if (empty($input)) $input = $_POST;

    $email    = isset($input['email']) ? trim($input['email']) : '';
    $password = isset($input['password']) ? $input['password'] : '';

    if ($email === '' || $password === '') {
        jsonResponse(['error' => 'Email dan password wajib diisi'], 422);
    }

    // MOCK LOGIN (Bypass DB untuk simulasi)
    if ($email !== 'admin@rakanponsel.com' || $password !== 'rakanponsel123') {
        jsonResponse(['error' => 'Email atau sandi salah!'], 401);
    }
    
    $user = [
        'id' => 1,
        'nama' => 'Admin RakanPay',
        'email' => $email,
        'role' => 'admin'
    ];

    // Set session
    $_SESSION['user_id']   = $user['id'];
    $_SESSION['user_nama'] = $user['nama'];
    $_SESSION['user_email'] = $user['email'];
    $_SESSION['user_role']  = $user['role'];

    jsonResponse([
        'success' => true,
        'message' => 'Login berhasil',
        'user'    => [
            'id'    => $user['id'],
            'nama'  => $user['nama'],
            'email' => $user['email'],
            'role'  => $user['role']
        ]
    ]);

} elseif ($method === 'GET') {
    // CHECK SESSION
    if (isset($_SESSION['user_id'])) {
        jsonResponse([
            'success'       => true,
            'authenticated' => true,
            'user' => [
                'id'    => $_SESSION['user_id'],
                'nama'  => $_SESSION['user_nama'],
                'email' => $_SESSION['user_email'],
                'role'  => $_SESSION['user_role']
            ]
        ]);
    } else {
        jsonResponse(['success' => true, 'authenticated' => false]);
    }

} elseif ($method === 'DELETE') {
    // LOGOUT
    session_destroy();
    jsonResponse(['success' => true, 'message' => 'Logout berhasil']);

} else {
    jsonResponse(['error' => 'Method not allowed'], 405);
}
