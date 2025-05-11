# lesson31
# Python INHERITANCE

# მემკვიდრეობა არის ობიექტზე ორიენტირებული პროგრამირების (OOP)
#  ერთ-ერთი ძირითადი პრინციპი, რომელიც საშუალებას აძლევს ახალ 
# კლასს (ე.წ. ბავშვის კლასს ან ქვეკლასს) მემკვიდრეობით მიიღოს ატრიბუტები 
# და მეთოდები არსებული კლასიდან (ე.წ. მშობელი კლასი ან საბაზო კლასი). 
# პითონში მემკვიდრეობა საშუალებას აძლევს კოდის ხელახლა გამოყენებას და
#  ქმნის ურთიერთობას კლასებს შორის, რაც ხელს უწყობს არსებული კლასების
#  უფრო სპეციალიზებული ვერსიების შექმნას.






# მემკვიდრეობის სარგებელი:
# კოდის მრავალჯერადი გამოყენება: ბავშვის კლასს შეუძლია ხელახლა გამოიყენოს მეთოდები და ატრიბუტები
# მშობლის კლასის #.
# გაფართოება: ბავშვის კლასს შეუძლია გააფართოვოს ან გადალახოს ფუნქცია
# მშობლის კლასის #.
# იერარქიული კლასიფიკაცია: შეგიძლიათ წარმოადგინოთ იერარქიული
# ურთიერთობა კლასებს შორის.
# მემკვიდრეობის სახეები პითონში:
# Single Inheritance: ქვეკლასი მემკვიდრეობით იღებს ერთი მშობლის კლასიდან.
# მრავალჯერადი მემკვიდრეობა: ქვეკლასი მემკვიდრეობით იღებს ერთზე მეტ მშობელს
# კლასი.
# მრავალდონიანი მემკვიდრეობა: ქვეკლასი მემკვიდრეობით იღებს სხვა ქვეკლასს
# (მრავალდონიანი იერარქიის შექმნა).
# იერარქიული მემკვიდრეობა: მრავალი ქვეკლასი მემკვიდრეობით იღებს იმავეს
# მშობლის კლასი.
# ჰიბრიდული მემკვიდრეობა: ორი ან მეტი ტიპის მემკვიდრეობის კომბინაცია.







# Benefits of Inheritance:
# Code Reusability: The child class can reuse the methods and attributes 
# of the parent class.
# Extensibility: The child class can extend or override the functionality 
# of the parent class.
# Hierarchical Classification: You can represent hierarchical 
# relationships between classes.
# Types of Inheritance in Python:
# Single Inheritance: A subclass inherits from one parent class.
# Multiple Inheritance: A subclass inherits from more than one parent 
# class.
# Multilevel Inheritance: A subclass inherits from another subclass
#  (creating a multi-level hierarchy).
# Hierarchical Inheritance: Multiple subclasses inherit from the same
#  parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.


# 1. Single Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  




# 2. Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Mammal:
    def has_hair(self):
        return True

class Dog(Animal, Mammal):  
    def __init__(self, name, breed):
        Animal.__init__(self, name)  
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())       
print(dog.has_hair())    



#  Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Mammal(Animal):
    def __init__(self, name, has_hair=True):
        super().__init__(name)
        self.has_hair = has_hair

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  
print(dog.has_hair)



# 4. Hierarchical Inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):  
    def speak(self):
        return f"{self.name} meows."

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  
print(cat.speak()) 



# 5. Hybrid Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Mammal:
    def has_hair(self):
        return True

class Dog(Animal, Mammal): 
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())     
print(dog.has_hair())   
