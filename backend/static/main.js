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

// function getUserInfo() {
//   var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//         console.log("Response Received: " + this.responseText);
//         return this.responseText
//       }
//     };
//     xhttp.open("GET", "/api/user", true);
//     xhttp.send();
//     console.log("Request Sent");
//   } 