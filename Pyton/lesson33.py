#  lesson33
# Python ABSTRACT CLASSES



# აბსტრაქტული კლასები პითონში
# პითონში, აბსტრაქტული კლასები არის კლასები, რომლებიც 
# არ შეიძლება იყოს უშუალოდ ინსტანციირებული და გამიზნულია სხვა კლასების
# მიერ ქვეკლასებად. აბსტრაქტული კლასი შეიძლება შეიცავდეს აბსტრაქტულ 
# მეთოდებს (მეთოდები განხორციელების გარეშე), რომლებიც უნდა განხორციელდეს
# ქვეკლასების მიერ. ეს უზრუნველყოფს გზას განსაზღვროს საერთო ინტერფეისი
# დაკავშირებული კლასების ჯგუფისთვის.

# აბსტრაქტული კლასები განისაზღვრება Python-ში abc (აბსტრაქტული საბაზისო 
# კლასი) მოდულის გამოყენებით. abc მოდული საშუალებას გაძლევთ 
# განსაზღვროთ აბსტრაქტული მეთოდები კლასში, რაც უზრუნველყოფს, რომ
# ნებისმიერი ქვეკლასი უზრუნველყოფს ამ მეთოდების განხორციელებას.

# ძირითადი ცნებები:
# აბსტრაქტული კლასი: კლასი, რომელიც არ შეიძლება იყოს უშუალოდ 
# ინსტანციირებული და ჩვეულებრივ შეიცავს ერთ ან მეტ აბსტრაქტულ მეთოდს.
# აბსტრაქტული მეთოდი: მეთოდი გამოცხადებულია აბსტრაქტულ კლასში, მაგრამ 
# ყოველგვარი განხორციელების გარეშე. ამ მეთოდების განსახორციელებლად საჭიროა
# ქვეკლასები.
# კონკრეტული მეთოდი: მეთოდი, რომელსაც აქვს სრული იმპლემენტაცია
# აბსტრაქტულ კლასში, რომელიც შეიძლება მემკვიდრეობით მიიღონ ქვეკლასებმა
# ცვლილებების გარეშე.
# როგორ შევქმნათ აბსტრაქტული კლასები პითონში
# პითონში აბსტრაქტული კლასის შესაქმნელად საჭიროა:

# ABC და აბსტრაქტული მეთოდის იმპორტი abc მოდულიდან.
# გამოიყენეთ @abstractmethod დეკორატორი აბსტრაქტული მეთოდების
# დასადგენად.
# კლასის განსაზღვრა ABC-ის ქვეკლასად.






#  of Abstract Classes in Python:

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"

    def move(self):
        return "Dog runs"


class Fish(Animal):
    def speak(self):
        return "Blub"

    def move(self):
        return "Fish swims"


dog = Dog()
fish = Fish()

print(dog.speak())  
print(dog.move())   

print(fish.speak()) 
print(fish.move())  







# Abstract Class with Concrete Methods:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("This is a shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(10, 4)

circle.display()  
print(circle.area()) 

rectangle.display()  
print(rectangle.area())  


