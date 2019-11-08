<?php
require_once "pdo.php";
session_start();

if ( isset($_POST['delete']) && isset($_POST['id']) ) {
    $sql = "DELETE FROM tracks WHERE id = :zip";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(':zip' => $_POST['id']));
    $_SESSION['success'] = 'Record deleted';
    header( 'Location: index.php' ) ;
    return;
}

$stmt = $pdo->prepare("SELECT title, id FROM tracks where id = :xyz");
$stmt->execute(array(":xyz" => $_GET['id']));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ( $row === false ) {
    $_SESSION['error'] = 'Bad value for id';
    header( 'Location: index.php' ) ;
    return;
}

echo "<p>Confirm: Deleting ".htmlentities($row['title'])."</p>\n";

echo('<form method="post"><input type="hidden" ');
echo('name="id" value="'.$row['id'].'">'."\n");
echo('<input type="submit" value="Delete" name="delete">');
echo('<a href="index.php">Cancel</a>');
echo("\n</form>\n");

