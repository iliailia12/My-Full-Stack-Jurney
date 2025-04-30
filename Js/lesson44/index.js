// JavaScript this keyword

// JavaScript– ის ეს საკვანძო სიტყვა ეხება მის კუთვნილ ობიექტს. 
// მისი მნიშვნელობა დამოკიდებულია იმ კონტექსტზე, რომელშიც ის 
// გამოიყენება. აქ მოცემულია ავარია, თუ როგორ იქცევა ეს სხვადასხვა 
// სცენარში:


// 1. გლობალური კონტექსტი
// გლობალურ სფეროში, ეს ეხება გლობალურ ობიექტს 
// (ფანჯარა ბრაუზერებში, გლობალური Node.js).

console.log(this); 

// 2. Inside a Function
// In a regular function, this refers to the global object 
// (in non-strict mode) or undefined (in strict mode).

function showThis() {
    console.log(this);
}
showThis();


// 3. მეთოდის შიგნით
// ობიექტის მეთოდის შიგნით გამოყენებისას, ეს
//  ეხება ობიექტს, რომელიც ფლობს მეთოდს.

const person = {
    name: "John",
    greet: function() {
        console.log(this.name);
    }
};
person.greet();


// 4. ისრის ფუნქციები
// ისრის ფუნქციებს არ აქვთ საკუთარი ეს. ამის ნაცვლად, ისინი 
// მემკვიდრეობით იღებენ 
// ამას მათი მიმდებარე ლექსიკური სფეროდან.

const person2 = {
    name: "John",
    greet: () => {
        console.log(this.name);
    }
};
person.greet();


// 5. კონსტრუქტორის ფუნქციაში
// კონსტრუქტორის ფუნქციაში ეს 
// ეხება ახლად შექმნილ ობიექტს.


function Person(name) {
    this.name = name;
}
const john = new Person("John");
console.log(john.name);


// 6. In a Class
// In a class, this refers to the instance of the class.

class Person {
    constructor(name) {
        this.name = name;
    }
    greet() {
        console.log(`Hello, ${this.name}`);
    }
}
const ilia = new Person("John");
john.greet();



// 7. Event Handlers
// In event handlers, this refers to the element that received the event.

document.querySelector("button").addEventListener("click", function() {
    console.log(this);
});