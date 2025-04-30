// ობიექტის შექმნა
const person = {
    name: "ილია",
    age: 12,
    greet() {
        return `გამარჯობა, მე ვარ ${this.name} და მე ${this.age} წლის ვარ.`;
    }
};
console.log(person.მისალმება()); // გამარჯობა, მე ვარ ილია და მე 25 წლის ვარ.

// Object Destructuring (ობიექტის დაშლა)
const { name, age } = person;
console.log(name); 
console.log(age);  

// Computed Property Names (გამოთვლადი თვისებების სახელები)
const key = "mark";
const student = {
    name: "mari",
    [key]: 95
};
console.log(student);  
 