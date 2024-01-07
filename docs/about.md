<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script type="text/javascript">
    (function() {
        // https://dashboard.emailjs.com/admin/account
        emailjs.init('T04vjc-ugM4jOvwZ2');
    })();
</script>
<script type="text/javascript">
    window.onload = function() {
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault();
            if valid_email($('input[name=user_email]').val())  {
              // generate a five digit number for the contact_number variable  
              this.contact_number.value = Math.random() * 100000 | 0;
              // these IDs from the previous steps
              emailjs.sendForm('service_4xyaq4h', 'template_fbrmfwm', this)
                  .then(function() {
                      console.log('SUCCESS!');
                  }, function(error) {
                      console.log('FAILED...', error);
                  });
          });
        }
    }
</script>
<hr/>
<br>
<h1>
I am Data Engineer and Business Intelligence Consultant
</h1>

<br>
<div class="form">
  <form id="form" class="form" method="post" halign="center" action="mailto:miro5lav@10g.pl">
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">
    <br>
    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">
    <br>
    <label for="country">Title</label>
    <select id="country" name="country">
      <option value="job">Job Offer</option>
      <option value="teamwork">Collaboration</option>
      <option value="money">Special Offer</option>
    </select>
    <br>
    <label for="subject">Subject</label> <br>
    <textarea halign="center" id="subject" name="subject" placeholder="Write something.." style="height:200px;"></textarea>
    <br>
    <input type="submit" value="Submit">   
  <hr/>
<h3> If you wish to subscribe to email fill data below</h3>
  </form>
      <form class="form" id="contact-form">
        <input type="hidden" name="contact_number">
        <label>Name</label>
        <input type="text" name="user_name"><br>
        <label>Email</label>
        <input type="email" name="user_email"><br>
        <label>Message</label>
        <textarea name="message"></textarea><br>
        <input type="submit" value="Send">
        <button onclick="valid_email($('input[name=user_email]').val())"> Validate Email </button>
        </form>
</div>