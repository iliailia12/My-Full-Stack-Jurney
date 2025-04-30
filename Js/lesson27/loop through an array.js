// o loop through an array in JavaScript, you can use several methods. Here are some common ones:

// 1. Using a for Loop
// 2. Using a for...of Loop
// 3. Using forEach
// 4. Using map (if you want to transform the array)
// Each method has its use case depending on the situation. For simple iteration, for or for...of is sufficient. For functional programming, forEach or map is often preferred.



//1
const array = [1, 2, 3, 4, 5];

for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}



//2
const array4 = [1, 2, 3, 4, 5];

for (const element of array) {
  console.log(element);
}



//3
const array3 = [1, 2, 3, 4, 5];

array.forEach(element => {
  console.log(element);
});


//4
const array1= [1, 2, 3, 4, 5];

array.map(element => {
  console.log(element);
});