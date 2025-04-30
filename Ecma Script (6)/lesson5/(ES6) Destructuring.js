// GES6 Destructuring არის ფუნქციონალი, რომელიც საშუალებას გაძლევთ მარტივად "დაშალოთ" მასივები ან ობიექტები
//  ცვლადებში. ეს ამარტივებს კოდის წაკითხვასა და გამოყენებას.

// ობიექტის დაშლა
const person = {
    name: "ილია",
    age: 25,
    city: "თბილისი"
};

const { name, age } = person;
console.log(name); 
console.log(age); 

// Default მნიშვნელობები
const { ქვეყანა = "საქართველო" } = person;
console.log(ქვეყანა);
 
 
// მასივის დაშლა
const colors = ["წითელი", "მწვანე", "ლურჯი"];

const [first1, second1] = colors;
console.log(first); 
console.log(second); 

// Default მნიშვნელობები
const [a, b, c = "ყვითელი"] = ["თეთრი", "შავი"];
console.log(c); 
 


//Nested Destructuring (ჩადგმული დაშლა)

 
// ჩადგმული ობიექტის დაშლა
const user1 = {
    name: "მარიამი",
    address: {
        city: "ბათუმი",
        street: "რუსთაველის"
    }
};

const { address: { city, street } } = user;
console.log(city); 
console.log(street); 
 

 
// Rest ოპერატორი
const numbers = [1, 2, 3, 4, 5];
const [first, second, ...დანარჩენი] = numbers;
console.log(first);  
console.log(დანარჩენი);  
 


// ფუნქციაში ობიექტის დაშლა
function printUser({ name, age }) {
    console.log(`name: ${name}, age: ${age}`);
}

const user = { name: "გიორგი", age: 30 };
printUser(user);  
