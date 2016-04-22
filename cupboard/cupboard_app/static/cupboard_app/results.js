/**
 * JS for Cupboard
 **/

/**
 * Parallax Scrolling JavaScript
 **/


$(document).ready(function(){
    // Cache the Window object
    $window = $(window);
                
   $('section[data-type="background"]').each(function(){
     var $bgObj = $(this); // assigning the object
                    
      $(window).scroll(function() {
                    
        // Scroll the background at var speed
        // the yPos is a negative value because we're scrolling it UP!                              
        var yPos = -($window.scrollTop() / $bgObj.data('speed'));
        
        // Put together our final background position
        var coords = '50% '+ yPos + 'px';

        // Move the background
        $bgObj.css({ backgroundPosition: coords });
        
}); // window scroll Ends

 });

});
/* 
 * Create HTML5 elements for IE's sake
 */

document.createElement("article");
document.createElement("section");