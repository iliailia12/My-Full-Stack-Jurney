#  lesson34
# SUPER() in Python

# სუპერ() ფუნქცია პითონში
# Super() ფუნქცია Python-ში არის ჩაშენებული ფუნქცია, რომელიც 
# გამოიყენება მეთოდის გამოსაძახებლად სუპერკლასიდან (მშობელი კლასი) 
# ქვეკლასიდან (child class). ის უზრუნველყოფს მეთოდების გამოძახების 
# ხერხს მშობელი კლასიდან, რაც იძლევა კოდის ხელახლა გამოყენების საშუალებას
#  და პოლიმორფიზმის ჩართვას ობიექტზე ორიენტირებულ პროგრამირებაში 
# (OOP).

# სუპერ()-ის პირველადი გამოყენების შემთხვევებია:

# მეთოდების გამოძახება მშობელი კლასიდან ქვეკლასში.
# მრავალჯერადი მემკვიდრეობის ჩართვა, სადაც მოწოდებულია
#  შემდეგი კლასი მეთოდის რეზოლუციის ორდერში (MRO).
# გამოძახება მშობელი კლასის კონსტრუქტორის (__init__)
#  სათანადო ინიციალიზაციის უზრუნველსაყოფად


# 1: Calling Parent Class Methods

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  
        print("Dog barks")


dog = Dog()
dog.speak()


#  2: Calling the Parent Class's Constructor (__init__)

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed


dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   
print(dog.breed) 


# 3: super() with Multiple Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def speak(self):
        super().speak() 
        print("Mammal speaks")

class Dog(Mammal):
    def speak(self):
        super().speak()  
        print("Dog barks")


dog = Dog()
dog.speak()


# Key Points to Remember:
# super() calls the next class in the MRO:

# This is particularly useful in multiple inheritance scenarios, 
# ensuring that the correct class methods are invoked in the proper order.
# super() can be used to call parent class methods:

# You can use super() to call the parent class's methods, allowing 
# subclasses to extend the functionality of inherited methods.
# super() is essential in cooperative multiple inheritance:

# When multiple classes are involved, super() enables cooperative 
# multiple inheritance, where each class’s method is called in the o
# rder defined by the MRO.
# Avoid direct class references in super():

# Instead of calling ClassName.method(self), use super() to 
# ensure the method resolution respects the class hierarchy.



# Super() ფუნქცია არის Python-ის ძლიერი ინსტრუმენტი,
#  რომელიც საშუალებას გაძლევთ გამოიძახოთ მეთოდები 
# მშობელი კლასებიდან. განსაკუთრებით სასარგებლოა მრავა
# ლჯერადი მემკვიდრეობის დროს იმის უზრუნველსაყოფად,
#  რომ მემკვიდრეობის იერარქიაში კლასები გამოიძახონ სწორ
# ი თანმიმდევრობით. super()-ის გამოყენებით შეგიძლიათ 
# შექმნათ მოქნილი, მრავალჯერადი გამოყენებადი და შენარ
# ჩუნებული ობიექტზე ორიენტირებული კოდი