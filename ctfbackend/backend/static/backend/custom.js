$(document).ready(function(){

  /* dynamic content link handler */
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

      $("li.active").removeClass("active");
      $(this).parent().addClass("active");
      d=$(this).parent().parent().parent();
      if(d.hasClass("dropdown")) {
        d.toggleClass("active");
        // dropdown hover close-on-click handler
        $(".dropdown-menu").css("display","none");
      }
    }
  });

  /** dropdown on hover **/
  $('.dropdown').on({
    mouseover: function(){
      $('.dropdown-menu').css("display","block");
    },
    mouseleave: function(){
      $('.dropdown-menu').css("display","none");
    }
  });
  $('.dropdown-menu').on({
    mouseleave: function(){
      $('.dropdown-menu').css("display","none");
    }
  });

});