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

function loadJSON(callback) {   

   var xobj = new XMLHttpRequest();
       xobj.overrideMimeType("application/json");
   xobj.open('GET', 'static/data/to_sun_2018.json', true); // Replace 'my_data' with the path to your file
   xobj.onreadystatechange = function () {
         if (xobj.readyState == 4 && xobj.status == "200") {
           // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
           callback(xobj.responseText);
         }
   };
   console.log(xobj.responseText)
   xobj.send(null);  
};

function init() {
 loadJSON(function(response) {
  // Parse JSON string into object
    actual_JSON = JSON.parse(response);
    console.log(actual_JSON);
    return actual_JSON
 });
}

init()

const months = {
	0: "Jan",
	1: "Feb",
	2: "Mar",
	3: "Apr",
	4: "May",
	5: "Jun",
	6: "Jul",
	7: "Aug",
	8: "Sep",
	9: "Oct",
	10: "Nov",
	11: "Dec"
}

var cdt = new Date();
function new_date() {
	cdt = new Date();
	return cdt;
}

function get_current_month() {
	cdtM = cdt.getMonth(); // returns int
	cdtM = months[cdtM];
	return cdtM;
}

function get_current_date() {
	cdtD = cdt.getDate();
	if (cdtD < 10) { cdtD = "0" + cdtD };
	return cdtD;
}

function get_current_time() {
	new_date();
	cdtHH = cdt.getHours();
	if (cdtHH < 10) { cdtHH = "0" + cdtHH };
	cdtMM = cdt.getMinutes();
	if (cdtMM < 10) { cdtMM = "0" + cdtMM };
	cdtTime = cdtHH.toString() + cdtMM.toString();
	return cdtTime;
}

function getSun() {
	get_current_month();
	get_current_date();
	get_current_time();
	for (i in actual_JSON) {
		obj = actual_JSON[i];
		objDayMo = obj.Date.split("-");
		objDay = objDayMo[0];
		objMo = objDayMo[1];
		if (objDay < 10) { objDay = "0" + objDay };
		objDate = objDay + objMo;
		currDayMo = cdtD + cdtM;
		if (objDate == currDayMo) {
			console.log(actual_JSON[i]);
			
			sunrise = actual_JSON[i].Sunrise;
			sunriseHH = sunrise.split(":")[0];
			sunriseMM = sunrise.split(":")[1];
			if (sunriseHH < 10) {
				sunriseHH = "0" + sunriseHH;
			}
			sunrise = sunriseHH + sunriseMM;

			sunset = actual_JSON[i].Sunset;
			sunsetHH = sunset.split(":")[0];
			sunsetMM = sunset.split(":")[1];
			if (sunsetHH < 10) {
				sunsetHH = "0" + sunsetHH;
			}
			sunset = sunsetHH + sunsetMM;
			both = [sunrise, sunset];
			return both;
		}
	}
}
