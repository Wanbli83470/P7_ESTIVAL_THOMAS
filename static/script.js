///Initialization document ready

$(document).ready(function(){

///Hide items before user actions

	$("#icône").css('opacity','0')
	$("#googleMap").hide()
	$(".p1").hide()
	$(".p2").hide()
	$(".RANDOM").hide()
	$("#histoire").hide()

/// Appearance of the elements at the passage of the mouse

	$("#fond_code").mouseenter(5000, function(){
		$("#fond_code").css('opacity','1');
	});

	$("#fond_code").mouseleave(function(){
		$("#fond_code").css('opacity','0.7');
	});

///Appearance of the elements to the passages after the submit

	$('form').submit(function(){
		$("#icône").delay(400).fadeTo("slow", 1);
		$(".p1").delay(1600).fadeIn(2000);
		$(".RANDOM").delay(1600).fadeIn(2000);
		$("#icône").delay(1000).fadeTo("slow", 0);
		$("#googleMap").delay(2200).fadeIn(2000);
		$(".p2").delay(4000).fadeIn(2000);
	});

});