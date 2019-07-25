// Use querySelector to store the div in a variable.
const redButton = document.querySelector('#red');
const greenButton = document.querySelector('#green');
const blueButton = document.querySelector('#blue');
const thebox = document.querySelector('#response-box');
// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");
  thebox.style.backgroundColor= "red";
});
blueButton.addEventListener('click', (e) => {
  console.log("You clicked the blue button!");
  thebox.style.backgroundColor= "blue";

});
greenButton.addEventListener('click', (e) => {
  console.log("You clicked the green button!");
  thebox.style.backgroundColor= "green"
});
