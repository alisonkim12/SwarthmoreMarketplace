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
      this.response.forEach((item) => {
        let br = document.createElement('br')
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
        name.className = 'item_name'

        let list = document.createElement('ul')
        list.style = 'list-style: none'

        let price = document.createElement('li')
        price.innerHTML = 'Price: ' + item['price']
        
        let description = document.createElement('li')
        description.className = 'description'

        let email = document.createElement('li')

        let condition = document.createElement('li')
        condition.innerHTML = "Condition: " + item['condition']
        condition.className = 'condition'
        email.innerHTML = "Contact the seller at " + item['email']
        description.innerHTML = 'Description: ' + item['description']
        list.appendChild(price)
        list.appendChild(condition)
        list.appendChild(description)
        list.appendChild(email)
        container.appendChild(name)
        container.appendChild(br)
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

function setUserPosts() {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Response Received: " + this.response);
      let postings = document.getElementById('postings')
      this.response.forEach((item) => {
        let column = document.createElement('div')
        column.id = item['product_id']
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
        list.style = 'list-style: none'
        let price = document.createElement('li')
        price.innerHTML = 'Price: ' + item['price']
        let description = document.createElement('li')
        let condition = document.createElement('li')
        let deleteButton = document.createElement('button')
        deleteButton.innerHTML = 'Delete Post'
        deleteButton.className = 'deleteButton'
        deleteButton.onclick = () => deleteUserPost(item['product_id'])
        condition.innerHTML = "Condition: " + item['condition']
        description.innerHTML = 'Description: ' + item['description']
        list.appendChild(price)
        list.appendChild(description)
        list.appendChild(condition)
        list.appendChild(deleteButton)
        container.appendChild(name)
        container.appendChild(list)
        card.appendChild(image)
        card.appendChild(container)
        column.appendChild(card)
        postings.appendChild(column)
      })
    }
  };
  xhttp.open("GET", "/api/user/posts", true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}

function deleteUserPost(productId) {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Successfully deleted")
      let post = document.getElementById(productId)
      post.style = 'display: none';
    }
  };
  xhttp.open("DELETE", `/api/posts/${productId}`, true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}

function getUserPost(productId) {
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let postInfo = this.response
    }
  };
  xhttp.open("GET", `/api/posts/${productId}`, true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}