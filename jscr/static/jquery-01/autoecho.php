<?php
  if ( !isset($_POST['val']) ) return;
  sleep(5);
  echo('You sent: '.$_POST['val']);

