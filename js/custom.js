$(document).ready(function(){
  $("a").click(function(e){
    var target=$(this).attr('target');
    if(target.match(/^_.*/) == null){
      e.preventDefault();
      $.ajax({
        type: 'GET', 
        url: $(this).attr('href'),
        success: function(data){
          $(target).html(data);
        }
      });
    }
  });
});