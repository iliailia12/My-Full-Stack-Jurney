# lesson29
# Python Object Oriented
# ობიექტზე ორიენტირებული პროგრამირება (OOP) პითონში არის პროგრამირების
#  პარადიგმა, რომელიც იყენებს "ობიექტებს" აპლიკაციების შესაქმნელად. ეს
#  ობიექტები არის კლასების ინსტანციები, რომლებიც 
# განსაზღვრავენ ობიექტების თვისებებს (ატრიბუტებს) და ქცევებს (მეთოდებს)
# . OOP პითონში ფოკუსირებულია შემდეგ ოთხ ძირითად კონცეფციაზე:

# 1. კლასები და ობიექტები
# კლასი: გეგმა ან შაბლონი ობიექტების შესაქმნელად. ის განსაზღვრავს 
# ატრიბუტებსა და მეთოდებს, რომლებიც ექნებათ ობიექტებს.
# ობიექტი: კლასის მაგალითი. როდესაც კლასი განისაზღვრება, მეხსიერება
#  არ არის გამოყოფილი, მაგრამ როდესაც ობიექტი იქმნება ამ კლასიდან,
#  მეხსიერება ენიჭება.
# 2. ინკაფსულაცია
# მონაცემების (ატრიბუტების) და მეთოდების (ფუნქციების) შეფუთვის იდეა, 
# რომლებიც მოქმედებენ მონაცემებზე ერთ ერთეულში (კლასში).
# ის ასევე მოიცავს ობიექტის ზოგიერთ კომპონენტზე წვდომის შეზღუდვას, 
# ობიექტის შიდა ფუნქციონირების კერძო და დაცულს გარე ჩარევისგან.
# 3. მემკვიდრეობა
# საშუალებას აძლევს კლასს (ე.წ. ბავშვი ან ქვეკლასი) მემკვიდრეობით 
# მიიღოს ატრიბუტები და მეთოდები სხვა კლასიდან (ე.წ. მშობელი ან 
# საბაზისო კლასი). ეს ხელს უწყობს კოდის ხელახლა გამოყენებას და
#  იძლევა იერარქიული კლასის სტრუქტურის საშუალებას.
# 4. პოლიმორფიზმი
# საშუალებას აძლევს სხვადასხვა კლასს განიხილებოდეს როგორც ერთი 
# და იმავე კლასის ეგზემპლარები საერთო ინტერფეისის საშუალებით. 
# ეს შეიძლება მოხდეს მეთოდის გადაფარვით (ქვეკლასებში) ან მეთოდის 
# გადატვირთვით.


# 1. Classes and Objects

# 2. Encapsulation

# 3. Inheritance

# 4. Polymorphism




# 1. Creating Classes and Objects:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine started.")


car1 = Car("Toyota", "Camry", 2020)
car1.start_engine()  



# 2. Encapsulation (Private and Public Attributes):


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  




# 3. Inheritance:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy", "Golden Retriever")
dog.speak()  



# 4. Polymorphism:


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()



# Method Overloading:

class Calculator:
    def add(self, *args):  
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         
print(calc.add(1, 2, 3, 4))   


