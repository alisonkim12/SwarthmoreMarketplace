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
        image.className = 'block-img'

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
        card.onclick = () => location.href = `/posts/${item['product_id']}`
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
        image.className = 'block-img'
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
        let condition = document.createElement('li')
        condition.className = 'condition'
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
        card.onclick = () => location.href = `/posts/${item['product_id']}`
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

function getPost() {
  console.log(window.location.href)
  let url = window.location.href
  let productId = url.split('/posts/')[1]
  var xhttp = new XMLHttpRequest();
  xhttp.responseType = 'json'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let postInfo = this.response
      let name = document.getElementById('item_name')
      name.innerHTML = postInfo['name']
      let price = document.getElementById('item_price')
      price.innerHTML = postInfo['price']
      let condition = document.getElementById('item_condition')
      condition.innerHTML = postInfo['condition']
      let email = document.getElementById('contact_info')
      email.innerHTML = postInfo['email']
      let image = document.getElementById('item-img')
      image.src = postInfo['image_url']
      let description = document.getElementById('item_description')
      description.innerHTML = postInfo['description']
    }
  };
  xhttp.open("GET", `/api/posts/${productId}`, true);
  xhttp.send();
  console.log("Request Sent");
  return xhttp
}