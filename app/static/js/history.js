$(document).ready(function() {
  $("#history_tab a").click(function(e){
    e.preventDefault();
    $(this).tab('show');
  });
});
