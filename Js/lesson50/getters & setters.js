// JavaScript getters & setters

class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }


    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }


    set fullName(name) {
        const parts = name.split(" ");
        if (parts.length === 2) {
            this.firstName = parts[0];
            this.lastName = parts[1];
        } else {
            console.error("Invalid full name format. Please provide both first and last names.");
        }
    }
}


const person = new Person("ilo", "kvico");
console.log(person.fullName); 

person.fullName = "ilia kviciani"; 
console.log(person.fullName);  

person.fullName = "InvalidName";  




// Getters და setters in JavaScript არის სპეციალური მეთოდები,
//  რომლებიც საშუალებას გაძლევთ განსაზღვროთ, თუ როგორ უნდა
//   შეხვიდეთ და განაახლოთ ობიექტის თვისებები. ისინი
//    უზრუნველყოფენ ლოგიკის დასაშიფრად ქონების მიღების ან 
//    დასადგენად, რაც 
// მას უფრო მოქნილს და სეკუს ხდის


// Getters და setters in JavaScript არის სპეციალური მეთოდები,
//  რომლებიც საშუალებას გაძლევთ განსაზღვროთ, თუ როგორ უნდა 
//  შეხვიდეთ და განაახლოთ ობიექტის თვისებები. ისინი უზრუნველყოფენ
//   ლოგიკის დასაშიფრად ქონების 
// მიღების ან დასადგენად, რაც მას უფრო მოქნილს და უსაფრთხოს ხ
// დის.