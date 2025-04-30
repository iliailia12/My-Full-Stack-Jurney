// JavaScript format currency
// ფულის ფორმატირება JavaScript-ში
// JavaScript-ში ფულის ფორმატირება მარტივად შესაძლებელია Intl.NumberFormat კლასის გამოყენებით. ეს კლასი საშუალებას გაძლევთ აირჩიოთ ვალუტის ტიპი და ქვეყნის რეგიონის ფორმატირება.



let amount = 123456.789;
 
let formatted = new Intl.NumberFormat('ka-GE', { 
  style: 'currency', 
  currency: 'GEL' 
}).format(amount);

console.log(formatted); 
   

