function googleTranslateElementInit() {
	new google.translate.TranslateElement(
		{
			pageLanguage:'en',
			gaTrack:true,
			gaId:'UA-31163327-1'
		},
		'google_translate_element'
	);
}

$(function(){
	var translate = $('#google_translate_element');

	translate.parents('.dropdown-menu').on(
		"click",
		function(event) {
			event.stopPropagation();
		}
	);

	$('[data-submenu]').submenupicker();
});
