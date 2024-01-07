// alert("💋 💋 💋 💖 Hello my friend ! 💋 💋 💋 💖")

function valid_email(booking_email) {

    if( /(.+)@(.+){2,}\.(.+){2,}/.test(booking_email) ){
    // valid email
    alert('Valid email');
    return true;
    } else {
    // invalid email
    alert('Please Enter Business Email Address');
    return false;
    }
}
