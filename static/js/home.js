if ($('.animate-med')) {
  $('.animate-med').hide();
  setTimeout(function () {
    $('.animate-med').fadeIn(650);
  }, 500);
}

if ($(".animate-loading")) {
  $(".animate-loading").delay(50).fadeIn(650);
}

$(".navbar").css("background-color", "rgba(255, 255, 255, 0)")