// JavaScript shuffle an array

// JavaScript-ში მასივის შერევის (shuffle) ფუნქციის შექმნა შეგიძლიათ sort() მეთოდით და Math.
// random() ფუნქციის გამოყენებით.

 
const shuffleArray = (array) => {
  return array.sort(() => Math.random() - 0.5);
};

const numbers = [1, 2, 3, 4, 5];
console.log(shuffleArray(numbers));
 

// Math.random() ქმნის შემთხვევით რიცხვს 0-დან 1-მდე.
// sort()-ის კომპარატორი ფუნქცია (Math.random() - 0.5) განსაზღვრავს ელემენტების შერევის შემთხვევითობას.
// ყოველი გავებისას მასივი განსხვავებულად იერევა.
// გთხოვთ გაითვალისწინოთ, რომ ეს მეთოდი არ არის სრულად შემთხვევითი დიდი მასივებისთვის. 
// სრულად შემთხვევითი შერევისთვის შეგიძლიათ გამოიყენოთ Fisher-Yates ალგორითმი.  
 