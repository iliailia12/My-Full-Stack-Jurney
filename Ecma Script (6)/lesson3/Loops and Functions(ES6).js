// ციკლები და ფუნქციები ES6-ში

// ქვემოთ მოცემულია ციკლებისა და ფუნქციების მაგალითები ES6-ში, რომლებიც შეგიძლიათ დაამატოთ თქვენს ფაილში
// For-of ციკლის მაგალითი
const fruits = ["ვაშლი", "ბანანი", "ატამი"];
for (const fruit of fruits) {
    console.log(fruit); 
}

// Arrow ფუნქციის მაგალითი
const square = (num) => num ** 2;
console.log(square(5)); 

// Default პარამეტრების მაგალითი
const greet = (name = "მეგობარო") => `გამარჯობა, ${name}!`;
console.log(greet()); 
console.log(greet("ილია")); 

// Rest ოპერატორის მაგალითი
const sum = (...numbers) => numbers.reduce((total, num) => total + num, 0);
console.log(sum(1, 2, 3, 4)); 

// Spread ოპერატორის მაგალითი
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2); 

// Map მეთოდის მაგალითი
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled); 

// Filter მეთოდის მაგალითი
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); 
