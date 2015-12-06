
window.kao = window.kao || {};

kao.sliderNext = function() {
	console.log('start sliderNext()');
	console.log('#slider-img-' + kao.currSilder);
	$('#slider-img-' + kao.currSlider).fadeOut(kao.sliderFadeInterval);
	kao.currSlider = kao.currSlider + 1;
	if (kao.currSlider > kao.sliderCount) kao.currSlider = 1;
	$('#slider-img-' + kao.currSlider).fadeIn(kao.sliderFadeInterval);
	
	setTimeout(kao.sliderNext, kao.sliderInterval);
};
kao.initSlider = function() {
	console.log('start initSlider()');
	kao.currSlider = 1;
	kao.sliderCount = 3;
	kao.sliderInterval = 8000;
	kao.sliderFadeInterval = 2000;
	
	setTimeout(kao.sliderNext, kao.sliderInterval);
};

kao.initPage = function() {
	console.log('start initPage()');
	kao.initSlider();
};
$(kao.initPage);