<?php
  sleep(2);
  header('Content-Type: application/json; charset=utf-8');
  $stuff = array('first' => 'first thing', 'second' => 'second thing');
  echo(json_encode($stuff));
