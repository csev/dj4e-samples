<?php
// To run local server
// php -S localhost:8000
$url_components = parse_url($_SERVER['HTTP_HOST']);
$domain = $url_components['host'];
?>
<html>
<head>
    <title>DJ4E Samples</title>
</head>
<body>
    <h1>Welcome to the DJ4e Samples</h1>
    <p>
    Here are some samples (Each will open in a new tab):
    <ul>
    <li><a href="http://<?= $domain ?>:8002" target="_blank">hello</a></li>
    <li><a href="http://<?= $domain ?>:8003" target="_blank">getpost</a></li>
    <li><a href="http://<?= $domain ?>:8004" target="_blank">users</a></li>
    <li><a href="http://<?= $domain ?>:8005" target="_blank">tracks</a></li>
    <li><a href="http://<?= $domain ?>:8006" target="_blank">views</a></li>
    <li><a href="http://<?= $domain ?>:8007" target="_blank">templates</a></li>
    <li><a href="http://<?= $domain ?>:8008" target="_blank">generic</a></li>
    <li><a href="http://<?= $domain ?>:8009" target="_blank">session</a></li>
    <li><a href="http://<?= $domain ?>:8010" target="_blank">form</a></li>
    <li><a href="http://<?= $domain ?>:8011" target="_blank">dj4ecrud</a></li>
    </ul>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples" target="_blank">
    https://github.com/csev/dj4e-samples</a>
    </p>
</body>
</html>
