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

      $("li.active").toggleClass("active");
      $(this).parent().toggleClass("active");
      $(this).parent().parent().parent().toggleClass("active");
        // dropdown hover close-on-click handler
        $(".dropdown-menu").css("display","none");
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