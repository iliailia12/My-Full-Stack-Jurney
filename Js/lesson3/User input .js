// მომხმარებლის შეყვანა JavaScript-ში
// JavaScript-ში მომხმარებლის შეყვანისთვის იყენებენ შესაბამის მეთოდებს, როგორიცაა:

// prompt(): აჩვენებს დიალოგურ ფანჯარას, სადაც მომხმარებელი შეყავნის ტექსტს.

// confirm(): აჩვენებს დიალოგურ ფანჯარას OK და Cancel ღილაკებით.

// HTML input-ის გამოყენება



// 1. prompt() მეთოდი
let name = prompt("რა არის თქვენი სახელი?");
console.log("მომხმარებლის სახელი: " + name);

// 2. confirm() მეთოდი
let confirmation = confirm("დარწმუნებული ხართ?");
if (confirmation) {
  console.log("მომხმარებელმა დაადასტურა.");
} else {
  console.log("მომხმარებელმა უარყო.");
}

 
function getInput() {
  let inputValue = document.getElementById("userInput").value;
  console.log("მომხმარებლის შეყვანილი ტექსტი: " + inputValue);
}
