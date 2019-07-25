const mybutton= document.querySelector("#mybutton");
const mybox = document.querySelector("#box");
mybutton.addEventListener("click", (event) => {
  console.log("like button clicked!");
  mybutton.innerHTML="liked! ";
  mybutton.style.backgroundColor ='lightgreen';
});
