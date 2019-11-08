<?php
    session_start();
    sleep(5);
    header('Content-Type: application/json; charset=utf-8');
    if ( !isset($_SESSION['chats']) ) $_SESSION['chats'] = array();
    echo(json_encode($_SESSION['chats'], JSON_PRETTY_PRINT));
