(function($) {
    'use strict';

    // ================================== Preloader ==================================

    $(window).on('load', function() {
        var preloaderFadeOutTime = 500;
        function hidePreloader() {
            var preloader = $('.spinner-wrapper');
            setTimeout(function() {
                preloader.fadeOut(preloaderFadeOutTime);
            }, 500);
        }
        hidePreloader();
    })
 // ================================== Button Back Top ==================================

    $(function() {

        // Scroll Event
        $(window).on('scroll', function() {
            var scrolled = $(window).scrollTop();
            if (scrolled > 300) $('.back-top').addClass('active');
            if (scrolled < 300) $('.back-top').removeClass('active');
        });


        $('.back-top').click(function() {
            $('html,body').animate({
                scrollTop: 0
            }, 700);
            return false;
        });
    });
    // ================================== Header ==================================
 // add class fixed for menu when scroll
    if ($('.bottom-header').hasClass('bottom-header'))  {
        var header_height = $('.bottom-header'),
            offset = header_height.offset();

        $(window).scroll(function() {
            if ($(window).scrollTop() > offset.top) {
                $(".bottom-header").addClass('header-fixed');
            } else {
                $(".bottom-header").removeClass('header-fixed');
            }
        });
    };

    // show menu when scroll up, hide menu when scroll down
    var lastScroll = 50;
    $(window).on('scroll load', function(event) {
        var st = $(this).scrollTop();
        if (st > lastScroll) {
            $('.bottom-header').addClass('hide-menu');
        } else if (st < lastScroll) {
            $('.bottom-header').removeClass('hide-menu');
        }
        if ($(window).scrollTop() == 0) {
            $('.bottom-header').removeClass('.header-fixed').removeClass('hide-menu');
        };
        lastScroll = st;

    });

        // ================================== Menu Responsive ==================================
    $(function() {
        $('.menu-mobile').click(function() {
            $('.block-menu-mobile').addClass('show1');
            $('.overlay-black').addClass('show2');

            return false;
        })
        $('.close-mobile').click(function() {
            $('.block-menu-mobile').removeClass('show1');
            $('.overlay-black').removeClass('show2');
            return false;
        })
        $('.overlay-black').click(function() {
            $('.block-menu-mobile').removeClass('show1');
            $(this).removeClass('show2');
            return false;
        })
    })

        // ================================== Catelories Responsive ==================================
    $(function() {
        $('.icon-catelory-mobile').click(function() {
            $('.block-catelory-mobile').addClass('show3');
            $('.overlay-black-2').addClass('show4');

            return false;
        })
        $('.close-mobile-cate').click(function() {
            $('.block-catelory-mobile').removeClass('show3');
            $('.overlay-black-2').removeClass('show4');
            return false;
        })
        $('.overlay-black-2').click(function() {
            $('.block-catelory-mobile').removeClass('show3');
            $(this).removeClass('show4');
            return false;
        })
    })

    $(function() {
        
        // Show - hide box search on menu
        $('.icon-search').on('click', function() {
            $('.nav-search').toggleClass('hide');
        });
        //hide box seach when click outside
        $('body').on('click', function(event) {
            if ($('.icon-search').has(event.target).length === 0 && !$('.icon-search').is(event.target) && $('.nav-search').has(event.target).length === 0 && !$('.nav-search').is(event.target)) {
                if ($('.nav-search').hasClass('hide') === false) {
                    $('.nav-search').toggleClass('hide');
                }
            }
        });
        
    });

        // ================================== Carousel Custom ==================================
       $(function() {
        $('#carousel-card-courses-1').owlCarousel({
            loop: true,
            margin: 18,
            smartSpeed: 100,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 1,
                    nav: true,
                    loop: false,
                    margin: 10
                },
                1200: {
                    items: 1,
                    nav: true,
                    loop: true,
                    margin: 20

                }
            }
        })
    })

        $(function() {
        $('#carousel-card-courses-2').owlCarousel({
            loop: true,
            margin: 18,
            smartSpeed: 100,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 3,
                    nav: true,
                    loop: false,
                    margin: 10
                },
                1200: {
                    items: 4,
                    nav: true,
                    loop: true,
                    margin: 20

                }
            }
        })
    })
     

        $(function() {
        $('#carousel-events').owlCarousel({
            loop: true,
            margin: 10,
            smartSpeed: 2000,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 1,
                    nav: true,
                    loop: false,
                    margin: 30
                },
                1170: {
                    items: 1,
                    nav: true,
                    loop: true,
                    margin: 30

                }
            }
        })
    })

          $(function() {
        $('#carousel-card-instrutor').owlCarousel({
            loop: true,
            margin: 20,
            smartSpeed: 100,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 2,
                    nav: true,
                    loop: false,
                    margin: 20
                },
                1200: {
                    items: 3,
                    nav: true,
                    loop: true,
                    margin: 25

                }
            }
        })
    })
              $(function() {
        $('#carousel-card-instrutor-2').owlCarousel({
            loop: true,
            margin: 20,
            smartSpeed: 100,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 2,
                    nav: true,
                    loop: false,
                    margin: 20
                },
                1200: {
                    items: 3,
                    nav: true,
                    loop: true,
                    margin: 25

                }
            }
        })
    })

           $(function() {
        $('#our-client-say').owlCarousel({
            loop: true,
            margin: 10,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 2,
                    nav: true,
                    loop: false,
                    margin: 30
                },
                1000: {
                    items: 2,
                    nav: true,
                    loop: false,
                    margin: 30
                }
            }
        })
    })
        

        // ================================== Count Number ==================================

        $(function() {
            var counters = $(".count");
            var countersQuantity = counters.length;
            var counter = [];
            for (var i = 0; i < countersQuantity; i++) {
                counter[i] = parseInt(counters[i].innerHTML);
            }
            var count = function(start, value, id) {
                var localStart = start;
                setInterval(function() {
                    if (localStart < value) {
                        localStart++;
                        counters[id].innerHTML = localStart;
                    }
                }, 80);
            }
            for (var j = 0; j < countersQuantity; j++) {
                count(0, counter[j], j);
            }
        });

 /*===================================*
    18. RATING STAR JS
    *===================================*/
    $(function(){
      $('.star_rating span').on('click', function(){
            var onStar = parseFloat($(this).data('value'), 10); // The star currently selected
            var stars = $(this).parent().children('.star_rating span');
            for (var i = 0; i < stars.length; i++) {
                $(stars[i]).removeClass('selected');
            }
            for (i = 0; i < onStar; i++) {
                $(stars[i]).addClass('selected');
            }
        });
    }); 
    

})(jQuery);