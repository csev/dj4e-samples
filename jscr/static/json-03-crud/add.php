<?php
require_once "pdo.php";
session_start();

if ( isset($_POST['title']) && isset($_POST['rating']) 
     && isset($_POST['plays'])) {
    if ( $_POST['plays']+0 <= 0 || $_POST['rating']+0 <= 0 || 
        strlen($_POST['title']) < 1) {
        $_SESSION['error'] = 'Bad value for title, plays or rating';
        header( 'Location: index.php' ) ;
        return;
    }

    $sql = "INSERT INTO tracks (title, plays, rating) 
              VALUES (:title, :plays, :rating)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(
        ':title' => $_POST['title'],
        ':plays' => $_POST['plays'],
        ':rating' => $_POST['rating']));
   $_SESSION['success'] = 'Record Added';
   header( 'Location: index.php' ) ;
   return;
}
?>
<html><head></head><body>
<?php
if ( isset($_SESSION['error']) ) {
    echo '<p style="color:red">'.$_SESSION['error']."</p>\n";
    unset($_SESSION['error']);
}
?>
<p>Add A New Record</p>
<form method="post">
<p>Title:
<input type="text" name="title"></p>
<p>Plays:
<input type="text" name="plays"></p>
<p>Rating:
<input type="text" name="rating"></p>
<p><input type="submit" value="Add New"/>
<a href="index.php">Cancel</a></p>
</form>
</body>
