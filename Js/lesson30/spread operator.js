// The JavaScript spread operator (...) allows you to expand elements of an array, object, or iterable into individual elements. Here are some common use cases:

// 1. Copying Arrays
// 2. Merging Arrays
// 3. Copying Objects
// 4. Merging Objects
// 1 vulnerability
// 5. Function Arguments
// The spread operator can be used to pass array elements as arguments to a function:

// The spread operator is versatile and simplifies working with arrays and objects.


const array1 = [1, 2, 3];
const array4 = [...array1];

console.log(array2);  



const array2 = [1, 2];
const array3 = [3, 4];
const mergedArray = [...array1, ...array2];

console.log(mergedArray); 




const obj12 = { a: 1, b: 2 };
const obj32 = { ...obj1 };

console.log(obj2);


       
const obj31 = { a: 1, b: 2 };
const obj2 = { b: 3, c: 4 };
const mergedObj = { ...obj1, ...obj2 };

console.log(mergedObj);  