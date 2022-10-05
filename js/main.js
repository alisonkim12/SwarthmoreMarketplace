function sendRequest() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        // Do something here with this.responseText
        console.log("Response Received: " + this.responseText);
      }
    };
    xhttp.open("GET", "data/mydata.txt", true);
    xhttp.send();
    console.log("Request Sent");
  }
  