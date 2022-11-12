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

function setPosts() {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Response Received: " + this.response);
      let cards = document.getElementById('cards')
      console.log(this.response)
      this.response.forEach((item) => {
        let column = document.createElement('div')
        column.className = 'column'
        let card = document.createElement('div')
        card.className = 'card'
        let image = document.createElement('img')
        image.src = item['image_url']
        image.alt = "Item_name"
        image.style = "width:50%"
        let container = document.createElement('div')
        container.className = 'container'
        let name = document.createElement('h3')
        name.innerHTML = item['name']
        let list = document.createElement('ul')
        let price = document.createElement('li')
        price.innerHTML = 'price: ' + item['price']
        let description = document.createElement('li')
        let interested = document.createElement('li')
        let condition = document.createElement('li')
        condition.innerHTML = item['condition']
        interested.innerHTML = "I'm interested"
        description.innerHTML = 'description: ' + item['description']
        list.appendChild(price)
        list.appendChild(description)
        list.appendChild(interested)
        container.appendChild(name)
        container.appendChild(list)
        card.appendChild(image)
        card.appendChild(container)
        column.appendChild(card)
        cards.appendChild(column)
      })
    }
  };
  xhttp.open("GET", "/api/posts", true);
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