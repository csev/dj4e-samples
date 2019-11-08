<html>
<head>
</head>
<body>
<p>Here is some awesome page content</p>
<script type="text/javascript" src="jquery.min.js">
</script>
<script type="text/javascript">
$(window).resize(function() {
  window.console && console.log('.resize() called. width='+
    $(window).width()+' height='+$(window).height());
});
</script>
</body>
