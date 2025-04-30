// JavaScript rest parameters
 
// JavaScript-ის Rest Parameters საშუალებას გაძლევთ ფუნქციაში გადაცემული ყველა არგუმენტი ერთ მასივში მოაქციოთ. ეს გამოგადგებათ იმ შემთხვევაში, როცა ფუნქციას ჯერ ზუსტი რაოდენობის არგუმენტი არ იცით.
 
// აქ არის მოკლე ახსნა და მაგალითი Rest Parameters-ის შესახებ:

 
function sum(...numbers) {
  return numbers.reduce((total, number) => total + number, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
 

// ...numbers არის Rest Parameter, რომელიც ფუნქციის არგუმენტებს ერთ მასივად მოაქცევს.

// reduce მეთოდი გამოიყენება, რომ მასივის ყველა ელემენტი დავამუშავოთ და ჯამი დავთვალოთ.

// თუ მეტი კითხვები გაქვთ ან დამატებითი მაგალითი გჭირდებათ, გთხოვთ მითხრათ! 😊

 


//1
function sum(...numbers) {
    return numbers.reduce((total, number) => total + number, 0);
  }
  
  console.log(sum(1, 2, 3, 4));