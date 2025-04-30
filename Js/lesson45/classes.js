// JavaScript classes

// JavaScript კლასები არის გეგმა ობიექტების
//  შესაქმნელად. ისინი უზრუნველყოფენ უფრო სუფთა 
//  და უფრო სტრუქტურულ გზას ობიექტის კ
//  ონსტრუქტორების, მეთოდებისა და მემკვიდრეობის 
//  განსაზღვრისთვის ტრადიციულ კონსტრუქტორულ
//   ფუნქციებთან და პროტოტიპებთან შედარებით.
// მსგავსი კოდი ნაპოვნია 1 ლიცენზიის ტიპით

// Basic Syntax
// A class is defined using the class keyword. Here's an example:

class Person {
    constructor(name, age) {
        this.name = name;  
        this.age = age;
    }

    // Method
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

 
const john = new Person("John", 30);
john.greet(); 






// კონსტრუქტორის მეთოდი
// კონსტრუქტორი არის სპეციალური მეთოდი, რომელიც გამოიყენება ობიექტების ინიციალიზაციისთვის.
//  მას ავტომატურად უწოდებენ, როდესაც იქმნება კლასის ახალი შემთხვევა.

// ინსტანციის მეთოდები
// კლასში განსაზღვრული მეთოდები ემატება კლასის პროტოტიპს და მისი წვდომა შესაძლებელია ყველა 
// შემთხვევით.

// სტატიკური მეთოდები
// სტატიკური მეთოდები განისაზღვრება სტატიკური საკვანძო სიტყვის გამოყენებით. ისინი თავად კლასს
//  მიეკუთვნებიან და არა შემთხვევებს.

class MathUtils {
    static add(a, b) {
        return a + b;
    }
}
console.log(MathUtils.add(5, 3));


// მემკვიდრეობა
// კლასებს შეუძლიათ მემკვიდრეობით მიიღონ სხვა კლასებიდან გაფართოებული 
// საკვანძო სიტყვის გამოყენებით. სუპერ საკვანძო სიტყვა გამოიყენება 
// მშობლის კლასის კონსტრუქტორის ან მეთოდების დასარეკად.


class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

const dog = new Dog("Rex");
dog.speak();



// გეტერები და სეტერები
// კლასებს შეიძლება ჰქონდეთ getter და setter მეთოდები, რათა 
// გააკონტროლონ წვდომა თვისებებზე.



class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    get area() {
        return this.width * this.height;
    }

    set dimensions({ width, height }) {
        this.width = width;
        this.height = height;
    }
}

const rect = new Rectangle(10, 5);
console.log(rect.area); // Output: 50
rect.dimensions = { width: 20, height: 10 };
console.log(rect.area);



// JavaScript კლასები გთავაზობთ თანამედროვე და ინტუიციურ გზას 
// ობიექტებთან და მემკვიდრეობასთან მუშაობისთვის. ისინი სინტაქსური შაქარია J
// avaScript- ის პროტოტიპზე დაფუძნებული 
// მემკვიდრეობის მოდელზე, მაგრამ კოდს უფრო იკითხება და ინარჩუნებს.




 