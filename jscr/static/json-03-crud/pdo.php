<?php
try {
    $pdo = new PDO('mysql:host=localhost;port=8889;dbname=misc', 
        'fred', 'zap');
} catch (Exception $e) {
echo($e->getMessage());
    die("You need to create the database and table for this application:
<pre>
CREATE DATABASE misc DEFAULT CHARACTER SET utf8;
GRANT ALL ON misc.* TO 'fred'@localhost IDENTIFIED BY 'zap';
GRANT ALL ON misc.* TO 'fred'@127.0.0.1 IDENTIFIED BY 'zap';

Switch to the misc database:

CREATE TABLE tracks (
  id INT UNSIGNED NOT NULL
     AUTO_INCREMENT KEY,
  title VARCHAR(128), 
  plays INTEGER,
  rating INTEGER
);
</pre>
");
}
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
