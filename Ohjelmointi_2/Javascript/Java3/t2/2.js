const target = document.getElementById("target");

const item1 = document.createElement("li");
item1.innerText = "First item";
target.appendChild(item1);

const item2 = document.createElement("li");
item2.innerText = "Second item";
item2.className = "my-item";
target.appendChild(item2);

const item3 = document.createElement("li");
item3.innerText = "Third item";
target.appendChild(item3);