<html>
<head>
</head>
<body>
<p id="para">Where is the spinner?
  <img id="spinner" src="spinner.gif" height="25" 
      style="vertical-align: middle; display:none;">
</p>
<a href="#" onclick="$('#spinner').toggle();
    return false;">Toggle</a>

<a href="#" onclick="$('#para').css('background-color', 'red');
    return false;">Red</a>

<a href="#" onclick="$('#para').css('background-color', 'green');
    return false;">Green</a>
<script type="text/javascript" src="jquery.min.js">
</script>
</body>
