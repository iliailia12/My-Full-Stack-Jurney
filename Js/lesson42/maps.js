
// JavaScript maps

 
// A **Map** JavaScript– ში არის ძირითადი მნიშვნელობის წყვილების კოლექცია, სადაც
//  გასაღებები შეიძლება იყოს ნებისმიერი ტიპის მონაცემთა ტიპის. რუკები ინარჩუნებს მათი 
//  ჩნაწერების თანმიმდევრობას და უზრუნველყოფს მეთოდებით მანიპულირების შესახებ.



// Create a new Map
const myMap = new Map();

// Add key-value pairs
myMap.set('name', 'John');
myMap.set('age', 30);
myMap.set(true, 'isActive');

// Access values
console.log(myMap.get('name')); 
console.log(myMap.get(true));   

// Check if a key exists
console.log(myMap.has('age')); 

// Get the size of the Map
console.log(myMap.size); 

// Iterate over a Map
myMap.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// Delete a key-value pair
myMap.delete('age');

// Clear all entries
myMap.clear();
console.log(myMap.size); 

