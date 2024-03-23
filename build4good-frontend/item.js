const menu_div = document.querySelector(".featured-items");

num_items = 50;
num_rows = Math.ceil(num_items/3)
height = num_rows * 80

document.querySelector(".featured-items").style.height = `${height}vh`;

data = [];
axios.get('http://localhost:3000/fetchData').then(response => {
    data = response.data;
    console.log(data);
    for (let i = 0; i < num_items; i++) {
        
        const newListItem = document.createElement("div");
    
        newListItem.textContent;
        newListItem.classList.add("item-box");
    
        newListItem.innerHTML = "<img src='images/bowl.png' class='item-img'>" 
                                    + "<h1 class='item-title'>" + data[i].properties.Name.title[0].plain_text + "</h1>"
                                    + "<p class='item-text'>Description</p>"
                                    + "<p class='item-cost'>Price: " + data[i].properties.Price.number + "</p>"
                                    + "<div class='item-button'>View Button</div>";
        menu_div.appendChild(newListItem);
    }
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
