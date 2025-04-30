// JavaScript objects

// JavaScript– ში ობიექტი არის თვისებების კრებული, სადაც თითოეული ქონება 
// არის ძირითადი მნიშვნელობის წყვილი. ობიექტები გამოიყენება მონაცემთა შესანახად 
// და ორგანიზებისთვის და ასევე 
// შეიძლება შეიცავდეს მეთოდებს (ფუნქციებს).


 
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    isEmployed: true,
    hobbies: ["reading", "traveling", "sports"],
    
    
    getFullName: function() {
        return `${this.firstName} ${this.lastName}`;
    }
};

// Access properties
console.log(person.firstName);
console.log(person["age"]);    

// Call a method
console.log(person.getFullName());  

// Add a new property
person.country = "USA";
console.log(person.country); 

// Modify a property
person.age = 31;
console.log(person.age); 

// Delete a property
delete person.isEmployed;
console.log(person.isEmployed); 