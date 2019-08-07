// todo only do this in dev
window.setTimeout(() => {
    const reload = false;
    if (reload){
        location.href = "http://localhost:7665";
    }
}, 5000);

const redirectThanks = function() {
    if (window.location.pathname === '/thanks' || window.location.pathname === '/thanks/') {
        setTimeout(function(){
            window.location.href = 'https://benefielinthelove.com';
        }, 3000)
    }
}

$(document).ready(() => {
    redirectThanks();
});
