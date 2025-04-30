// JavaScript nested functions

// JavaScript-ში Nested Functions არის ფუნქციები, რომლებიც შიგნით ფუნქციაშია განსაზღვრული. შიდა ფუნქციას შეუძლია გამოიყენოს გარე ფუნქციის მონაცემები და კონტექსტი. ეს მიდგომა განსაკუთრებით გამოსადეგია, როცა კოდი უნდა დავახარისხოთ ან ლოგიკა დავაკომპაქტოთ.

 
function outerFunction(name) {
  function innerFunction() {
    console.log(`გამარჯობა, ${name}!`);
  }
  innerFunction(); 
}

outerFunction("მარიამი");
 

// outerFunction განსაზღვრავს innerFunction-ს.

// შიდა ფუნქცია (inner) იღებს წვდომას გარე ფუნქციის (outer) ცვლადებზე.

// innerFunction მხოლოდ იმ შემთხვევაში შეიძლება გამოიძახოთ, თუ outerFunction შიგნით ხართ.

// Nested Functions კარგია ფუნქციურ პროგრამირებაში