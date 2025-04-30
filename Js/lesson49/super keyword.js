// JavaScript super keyword

// JavaScript- ში "სუპერ" საკვანძო სიტყვა გამოიყენება კლასებში, რათა დარეკოს კონსტრუქტორი ან მშობლის კლასის მეთოდები. იგი
//  ჩვეულებრივ გამოიყენება მემკვიდრეობის კონტექსტში, როდესაც ქვეკლასს სჭირდება მშობლის კლასის ფუნქციონირება ან გაფართოება.


// JavaScript super keyword

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
        super.speak(); 
        console.log(`${this.name} barks.`);
    }
}

const genericAnimal = new Animal("Generic Animal");
genericAnimal.speak();

const dog = new Dog("Buddy", "Golden Retriever");
dog.speak(); 