// Rest & Sp read

// Rest & Spread ოპერატორები ES6-ში საშუალებას გაძლევთ მარტივად იმუშაოთ მასივებთან, ობიექტებთან და ფუნქციებთან.

// Rest ოპერატორი (...)
// Rest ოპერატორი გამოიყენება, როდესაც გვინდა ფუნქციაში ან მასივში დარჩენილი ელემენტები ერთ ცვლადში მოვაქციოთ.
//  Rest ოპერატორი საშუალებას გაძლევთ "დარჩენილი" მნიშვნელობები ერთ ცვლადში

// ფუნქციაში Rest ოპერატორი
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); 

// მასივის დაშლა Rest ოპერატორით
const [first, second, ...rest] = [10, 20, 30, 40, 50];
console.log(first); 
console.log(second); 
console.log(rest); 



// Spread ოპერატორი (...)
// Spread ოპერატორი გამოიყენება, როდესაც გვინდა მასივი ან ობიექტი "გავშალოთ" ცალკეულ ელემენტებად.

// ქართულად: Spread ოპერატორი საშუალებას გაძლევთ მასივი ან ობიექტი ცალკეულ ელემენტებად "გაშალოთ".

// მასივის გაშლა
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(combined);

// ობიექტის გაშლა
const obj1 = { name: "ილია", age: 25 };
const obj2 = { city: "თბილისი", country: "საქართველო" };
const combinedObj = { ...obj1, ...obj2 };
console.log(combinedObj); 
 