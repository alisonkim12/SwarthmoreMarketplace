function setUserName() {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Response Received: " + this.response);
      document.getElementById("hello").innerHTML = "Hello " + this.response['firstname'] + "!";
    }
  };
  xhttp.open("GET", "/api/user", true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}

function setUserInfo() {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Response Received: " + this.response);
      document.getElementById("name").innerHTML = this.response['firstname'] + " " + this.response['lastname'];
      document.getElementById('email').innerHTML = 'Email: ' + this.response['email']
      phone = this.response['mobile']
      if (phone) {
        document.getElementById("mobile").innerHTML = 'Mobile: ' + phone
      }
    }
  };
  xhttp.open("GET", "/api/user", true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}
  
function contactUser() {
  Email.send({
    SecureToken : "e207fbbf-12c8-4708-8840-5dda9e9823dd",
    To : 'awu2@swarthmore.edu',
    From : "swarthmoremarketplace@gmail.com",
    Subject : "This is the subject",
    Body : "And this is the body"
  }).then(
    message => alert(message)
  );
}