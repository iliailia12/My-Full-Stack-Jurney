// JavaScript inheritance

class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name); 
        this.breed = breed;
    }

    speak() {
        console.log(`${this.name} barks.`);
    }
}

const genericAnimal = new Animal("Generic Animal");
genericAnimal.speak(); 

const dog = new Dog("Buddy", "Golden Retriever");
dog.speak();                