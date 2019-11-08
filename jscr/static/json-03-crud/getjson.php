<?php
require_once "pdo.php";
session_start();
header('Content-Type: application/json; charset=utf-8');
$stmt = $pdo->query("SELECT title, plays, rating, id FROM tracks");
$rows = array();
while ( $row = $stmt->fetch(PDO::FETCH_ASSOC) ) {
  $rows[] = $row;
}

echo json_encode($rows, JSON_PRETTY_PRINT);
