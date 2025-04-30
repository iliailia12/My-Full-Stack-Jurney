// JavaScript static
// JavaScript static

// JavaScript- ში "სტატიკური" საკვანძო სიტყვა გამოიყენება იმ მეთოდების ან თვისებების 
// დასადგენად, რომლებიც ეკუთვნის თავად კლასს, ვიდრე კლასის შემთხვევებს. მათ უწოდებენ *
// * სტატიკური მეთოდები ** ან ** სტატიკური თვისებები **.

// #### 1. ** სტატიკური მეთოდები **
// სტატიკური მეთოდები პირდაპირ კლასშია და არ შეიძლება ეწოდოს კლასის შემთხვევებს.

class Calculator {
    static add(a, b) {
        return a + b;
    }

    static multiply(a, b) {
        return a * b;
    }
}


console.log(Calculator.add(5, 3));      
console.log(Calculator.multiply(4, 7));


const calc = new Calculator();

 
// #### 2. ** სტატიკური თვისებები **
// სტატიკური თვისებები პირდაპირ კლასშია და არ შეიძლება ეწოდოს კლასის შემთხვევებს.

class AppConfig {
    static appName = "My Application";
    static version = "1.0.0";

    static getInfo() {
        return `${this.appName} - Version: ${this.version}`;
    }
}


console.log(AppConfig.appName);  
console.log(AppConfig.version); 
console.log(AppConfig.getInfo()); 