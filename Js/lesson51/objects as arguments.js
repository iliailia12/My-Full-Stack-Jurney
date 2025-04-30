// JavaScript objects as arguments

// In JavaScript, objects can be passed as arguments to functions. This allows you to pass 
// multiple related values together and access them within the function. Using objects as 
// arguments is especially useful when dealing with functions that require many parameters, 
// as it improves readability and flexibility.
// ### Example: Passing Objects as Arguments

function displayPersonInfo(person) {
    console.log(`Name: ${person.name}`);
    console.log(`Age: ${person.age}`);
    console.log(`City: ${person.city}`);
}


const person = {
    name: "Ilia",
    age: 25,
    city: "Tbilisi"
};


displayPersonInfo(person);


 

// b ასევე შეგიძლიათ გამოიყენოთ ** ობიექტის დესტრუქტურირება ** კონკრეტული თვისებების პირდაპირ ამოსაღებად
// ფუნქციის პარამეტრებში.

function displayPersonInfo({ name, age, city }) {
    console.log(`Name: ${name}`);
    console.log(`Age: ${age}`);
    console.log(`City: ${city}`);
}

const person2 = {
    name: "Ilia",
    age: 25,
    city: "Tbilisi"
};

displayPersonInfo(person);
 
// ეს მიდგომა ხდის კოდს სუფთა და თავიდან აიცილებს განმეორებით წვდომას თვისებებზე
// "person.property".
// ## ძირითადი უპირატესობები:
//  1. **გაუმჯობესებული წაკითხვა **: ჯგუფთან დაკავშირებული მონაცემები ერთ ობიექტში.
// 2. **მოქნილობა **: მარტივად დაამატეთ ან ამოიღეთ თვისებები ფუნქციის ხელმოწერის შეცვლის გარეშე.
//  3. **განადგურება **: ამარტივებს კონკრეტულ თვისებებზე წვდომას.
// გსურთ ამის განხორციელება თქვენს ამჟამინდელ ფაილში ან შეისწავლოთ დაკავშირებული თემა?