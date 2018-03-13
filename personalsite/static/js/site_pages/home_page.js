$(document).ready(function(){
    $('a[href^="#"]').on('click',function (e) {
        e.preventDefault();

        var target = this.hash;
        console.log(target);
        var $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            window.location.hash = target;
        });
    });
});
// scrollMagic
var controller = new ScrollMagic.Controller();
var Sections = $('section');
for (var i = Sections.length - 1; i >= 0; i--) {
	Sections[i];

	var Str = "#section-";
	var scene = new ScrollMagic.Scene({triggerElement: Str + i})
					// trigger animation by adding a css class
					.setClassToggle(Str + i, "zap")
					// .addIndicators({name: "1 - add a class"}) // add indicators (requires plugin)
					.addTo(controller);
};

var scene = new ScrollMagic.Scene({triggerElement: "#contact-us"})
					// trigger animation by adding a css class
					.setClassToggle("#contact-us", "zap")
					// .addIndicators({name: "1 - add a class"}) // add indicators (requires plugin)
					.addTo(controller);

// light the tower
$('.red-light:lt(34)').each(function(i){
    var $li = $(this);
    setTimeout(function() {
      $li.addClass('red-light-animation');
    }, i*30 );
});
