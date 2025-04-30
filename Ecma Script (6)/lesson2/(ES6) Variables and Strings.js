// ES6 ცვლადები და სტრინგები

// let და const - ცვლადების გამოცხადება
let name = "ილია";
const age = 25;

// ტემპლეიტ სტრინგები (Template Strings)
let greet = `გამარჯობა, ჩემი სახელი არის ${name} და მე ვარ ${age} წლის.`;

// სტრინგის მეთოდები
let txt = "ეს არის ES6-ის გაკვეთილი.";
let longtxt = txt.length;
let bigtxt = txt.toUpperCase(); 
let smalltxt = txt.toLowerCase(); 

console.log(greet);
console.log(`txtს სიგრძე: ${longtxt}`);
console.log(`დიდი ასოებით: ${bigtxt}`);
console.log(`პატარა ასოებით: ${smalltxt}`);