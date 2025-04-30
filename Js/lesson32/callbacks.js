// JavaScript callbacks


// JavaScript-ში callback ფუნქცია არის ფუნქცია, რომელიც გადაეცემა სხვა ფუნქციას როგორც არგუმენტი და შემდეგ მუშავდება ან გამოძახება მეორე ფუნქციის მიერ.

// აქ არის მოკლე ახსნა და მაგალითი callback-ის შესახებ:

 
function processUserInput(callback) {
  const name = prompt("შეიყვანეთ თქვენი სახელი:");
  callback(name);
}

function greetUser(name) {
  console.log(`გამარჯობა, ${name}!`);
}

 
processUserInput(greetUser);
 

// processUserInput ფუნქცია იღებს callback ფუნქციას როგორც არგუმენტი.

// callback ფუნქცია (ამ შემთხვევაში greetUser) გადაეცემა და მის დახმარებით ხდება მომხმარებლის სახელით მუშაობა.

// ეს მიდგომა განსაკუთრებით გამოსადეგია ასინქრონულ ოპერაციებში, როგორიცაა მონაცემების წამოღება სერვერიდან.