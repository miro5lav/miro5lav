// alert("💋 💋 💋 💖 Hello my friend ! 💋 💋 💋 💖")

function valid_email(booking_email) {

    if( /(.+)@(.+){2,}\.(.+){2,}/.test(booking_email) ){
    //alert('Valid email');
    return true;
    } else {
    //alert('Invalid email');
    return false;
    }
}

// make disabled button after click
function button_timeout(obj) {
    obj.disabled = true;
    setTimeout(function() {
        obj.disabled = false;
    }, 10000);
}​