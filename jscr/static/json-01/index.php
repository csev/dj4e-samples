<html>
<head>
</head>
<body>
<p>Howdy - Lets get some JSON</p>
<p id="back">Original static text</p>
<p>
<a href="syntax.php" target="_new">JSON Syntax</a> |
<a href="json.php" target="_new">json.php</a>
</p>
<script type="text/javascript" src="jquery.min.js">
</script>
<script type="text/javascript">
$(document).ready( function () {
  $.getJSON('json.php', function(data) {
      $("#back").html(data.first);
      window.console && console.log(data);
    })
  }
);
</script>
</body>
