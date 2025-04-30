// JavaScript closures
 
// ### რა არის JavaScript დახურვა?
// A **დახურვა ** არის ფუნქცია, რომელსაც აქვს წვდომა საკუთარ მასშტაბებზე, 
// გარე ფუნქციის ფარგლებსა და გლობალურ მასშტაბებზე. დახურვა იქმნება ყოველ ჯერზე, 
// როდესაც ფუნქცია განისაზღვრება, რაც საშუალებას აძლევს ფუნქციას "დაიმახსოვროს"
//  გარემო, რომელშიც იგი შეიქმნა.


function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log(`Outer Variable: ${outerVariable}`);
        console.log(`Inner Variable: ${innerVariable}`);
    };
}

const newFunction = outerFunction("outside");
newFunction("inside");
  
 