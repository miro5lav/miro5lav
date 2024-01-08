<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script type="text/javascript">
    (function() {
        emailjs.init('T04vjc-ugM4jOvwZ2');
    })();
</script>
<script type="text/javascript">
    window.onload = function() {
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault();
              this.button_timeout($('input[name=ejs_input]') ); 
              // generate a five digit number for the contact_number variable  
              this.contact_number.value = Math.random() * 100000 | 0;
              // these IDs from the previous steps
              emailjs.sendForm('service_4xyaq4h', 'template_fbrmfwm', this)
                  .then(function() {
                      console.log('SUCCESS!');
                      alert("Email has been send my friend 💖"));
                  }, function(error) {
                      console.log('FAILED...', error);
                      alert("Something went wrong.Check Console!"));
                  });   
          });
       
    }
</script>
<hr/>
<br>
<h1>
I am Data Engineer and Business Intelligence Consultant
</h1>

<br>
  <hr/>
<h3> If you wish to contact me fill data below</h3>
<div class="form" >
      <form class="form" id="contact-form">
        <input type="hidden" name="contact_number">
        <label>Name</label><br>
        <input type="text" name="user_name"><br>
        <label>Email</label><br>
        <input type="email" name="user_email"><br>
        <label>Full Phone with Country Code</label><br>
        <input type="phone" name="user_phone"><br>
        <label>Your Message</label><br>
        <textarea name="message" rows="12" cols="80"></textarea><br>
        <input type="submit" value="Send" name="ejs_input" >
        <!-- <button onclick="valid_email($('input[name=user_email]').val())"> Validate Email </button> -->
        </form>
</div>