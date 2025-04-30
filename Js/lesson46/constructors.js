// JavaScript constructors

// ## # JavaScript კონსტრუქტორები

// JavaScript-ში, **კონსტრუქტორი ** არის სპეციალური ფუნქცია, რომელიც გამოიყენება 
// ობიექტების შესაქმნელად და ინიციალიზაციისთვის. იგი ჩვეულებრივ გამოიყენება კლასებში 
// ან როგორც დამოუკიდებელი ფუნქცია ობიექტის თვისებებისა და მეთოდების დასაყენებლად.

// ---

// #### 1. ** კონსტრუქტორი კლასებში**
// ES6 კლასების გამოყენებისას, "კონსტრუქტორის" მეთოდი გამოიყენება ობიექტის თვისებების
//  ინიციალიზაციისთვის. მას ავტომატურად უწოდებენ, როდესაც იქმნება კლასის ახალი შემთხვევა.
// n სხვა თემასთან?


class Person {
    constructor(name, age) {
        this.name = name;  
        this.age = age;   
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

 
const john = new Person("John", 30);
john.greet(); 


// 2. დამოუკიდებელი კონსტრუქტორის ფუნქციები
// ES6-მდე კონსტრუქტორის ფუნქციები გამოიყენებოდა ობიექტების შესაქმნელად. კონგრესის მიხედვით, ფუნქციის სახელი იწყება დიდი ასოებით


function Car(make, model) {
    this.make = make;    
    this.model = model;  
    this.drive = function () {
        console.log(`Driving a ${this.make} ${this.model}`);
    };
}

 
const car = new Car("Toyota", "Corolla");
car.drive();  

//2

class Animal {
    constructor(name = "Unknown", type = "Unknown") {
        this.name = name;
        this.type = type;
    }

    describe() {
        console.log(`${this.name} is a ${this.type}.`);
    }
}

const dog001 = new Animal("Buddy", "Dog");
dog001.describe(); 

const unknownAnimal = new Animal();
unknownAnimal.describe(); 


//3


class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);  
        this.breed = breed;
    }

    describe() {
        console.log(`${this.name} is a ${this.breed}.`);
    }
}

const dog = new Dog("Rex", "German Shepherd");
dog.describe();