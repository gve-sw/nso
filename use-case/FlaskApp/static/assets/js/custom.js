
/*=============================================================
    Authour URI: www.binarytheme.com
    License: Commons Attribution 3.0

    http://creativecommons.org/licenses/by/3.0/

    100% Free To use For Personal And Commercial Use.
    IN EXCHANGE JUST GIVE US CREDITS AND TELL YOUR FRIENDS ABOUT US
   
    ========================================================  */

(function ($) {
    "use strict";
    var mainApp = {
        scroll_fun: function () {

            //CUSTOM SCROLL SCRIPT FUNCTION FOR NAVBAR 
          $(function () {
              $('.scrollclass a').bind('click', function (event) { //just pass scrollclass in design and start scrolling
                  var $anchor = $(this);
                  $('html, body').stop().animate({
                      scrollTop: $($anchor.attr('href')).offset().top
                  }, 1200, 'easeInOutExpo');
                  event.preventDefault();
              });
          });
            

        },
        
        gallery_fun: function () {
            /*====================================
                 FOR IMAGE/GALLERY POPUP
            ======================================*/
            $("a.preview").prettyPhoto({
                social_tools: false
            });

            /*====================================
            FOR IMAGE/GALLERY FILTER
            ======================================*/

            // MixItUp plugin
            // http://mixitup.io

            $('#port-folio').mixitup({
                targetSelector: '.portfolio-item',
                filterSelector: '.filter',


            });
        },
        nicescroll_fun:function()
        {
            $("html").niceScroll();
        },

      
        custom_fun:function()
        {
            /*====================================
             WRITE YOUR   SCRIPTS  BELOW
            ======================================*/




        },

    };
   
   
    $(document).ready(function () {
        mainApp.scroll_fun();
        mainApp.gallery_fun();
        mainApp.nicescroll_fun();
        mainApp.custom_fun();

    });
}(jQuery));


