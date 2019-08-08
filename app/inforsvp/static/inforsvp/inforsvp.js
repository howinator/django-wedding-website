// todo only do this in dev
window.setTimeout(() => {
    const reload = false;
    if (reload){
        location.href = "http://localhost:7665";
    }
}, 5000);

var redirectThanks = function() {
    if (window.location.pathname === '/thanks' || window.location.pathname === '/thanks/') {
        setTimeout(function(){
            window.location.href = 'https://benefielinthelove.com';
        }, 3000)
    }
}

var scrollToId = function(id) {
    var aTag = $("#" + id);
    $('html,body').animate({scrollTop: aTag.offset().top},'slow');
}

var addAnchorEventListeners = function() {
    var clickMap = {
        "home-btn": "top",
        "story-btn": "our-story",
        "wedding-btn": "the-wedding",
        "getting-there-btn": "getting-there"
    };

    $.each(clickMap, function(key, val) {
        var el = document.getElementById(key);
        if (window.location.pathname === '/' || window.location.pathname === ''){
            el.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                scrollToId(val);
            })
        } else {
            el.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                window.location.href = 'https://benefielinthelove.com#' + val;
            })
        }
    })
}

$(document).ready(() => {
    redirectThanks();
    addAnchorEventListeners();
});
