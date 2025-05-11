#  lesson32
# Python MULTIPLE INHERITANCE

# მრავალჯერადი მემკვიდრეობა პითონში არის ფუნქცია,
# რომლის დროსაც კლასს შეუძლია მემკვიდრეობა მიიღოს ერთზე მეტი
# მშობელი კლასისგან. ეს საშუალებას აძლევს ქვეკლასს მემკვიდრეობით 
# მიიღოს მეთოდები და ატრიბუტები მრავალი საბაზისო კლასებიდან. მიუხედავად 
# იმისა, რომ ეს შეიძლება იყოს ძლიერი კოდის ხელახლა გამოსაყენებლად და უფრო
# მოქნილი კლასის სტრუქტურების შესაქმნელად, მას ასევე შეუძლია სირთულეების 
# დანერგვა, განსაკუთრებით მეთოდის გადაწყვეტის წესრიგის (MRO) თვალსაზრისით,
# როდესაც მრავალ მშობელ კლასს აქვს იგივე სახელის 
# მეთოდები.

# Example of Multiple Inheritance:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Mammal:
    def __init__(self, has_hair=True):
        self.has_hair = has_hair

    def has_mammary_glands(self):
        return True

class Dog(Animal, Mammal):  
    def __init__(self, name, breed):
        Animal.__init__(self, name)  #
        Mammal.__init__(self)        
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  
print(dog.has_mammary_glands())  
print(dog.has_hair)  





# მეთოდის რეზოლუციის ორდერი (MRO)
# მრავალჯერადი მემკვიდრეობის შემთხვევაში, თუ ორ ან მეტ მშობელ კლასს აქვს 
# იგივე სახელის მეთოდები, Python იყენებს მეთოდის გადაწყვეტის ბრძანებას (MRO), 
# რათა გადაწყვიტოს რომელი მეთოდი გამოიძახოს. MRO განისაზღვრება C3 Lineariz
# ation ალგორითმით.

# შეგიძლიათ შეამოწმოთ მეთოდის გარჩევადობის თანმიმდევრობა mro() მეთოდის 
# ან __mro__ გამოყენებით


# Example of MRO in Action:

class A:
    def hello(self):
        print("Hello from class A")

class B(A):
    def hello(self):
        print("Hello from class B")

class C(A):
    def hello(self):
        print("Hello from class C")

class D(B, C):
    def hello(self):
        print("Hello from class D")


d = D()
d.hello()  


print(D.mro())  
