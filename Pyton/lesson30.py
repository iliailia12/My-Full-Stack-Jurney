# lesson30
# Python CLASS VARIABLES 

# პითონი, კლასის ცვლადები არის ცვლადები, რომლებიც
# იზიარებენ კლასის ყველა ინსტანციას (ობიექტს).
# ისინი განსაზღვრულია უშუალოდ კლასში, მაგრამ ნებისმიერი ინსტანციის 
# მეთოდის მიღმა (ანუ მეთოდები, რომლებიც მოითხოვს თვითმმართველობას,
#                 როგორც პირველ პარამეტრს).

# კლასის ცვლადების ძირითადი მახასიათებლები:
# გაზიარებული ყველა ინსტანციას შორის: კლასის ცვლადი არ არის სპეციფიკური
# კლასის რომელიმე ინსტანციისთვის. ამის ნაცვლად, ის იზიარებს ამ კლასის ყველა
# ინსტანციას.
# წვდომა კლასის მეშვეობით: თქვენ შეგიძლიათ წვდომა კლასის ცვლადზე პირდაპირ 
# კლასიდან ან კლასის ინსტანციიდან.
# მოდიფიცირებადი კლასის მეშვეობით: კლასის ცვლადში შეტანილი ნებისმიერი 
# ცვლილება გავლენას ახდენს კლასის ყველა ინსტანციაზე.





# Key Characteristics of Class Variables:
# Shared among all instances: A class variable is not specific to any 
# single instance of the class. Instead, it is shared by all instances 
# of that class.
# Accessed via the class: You can access a class variable directly from 
# the class or from an instance of the class.
# Modifiable via the class: Any changes made to the class variable affect
#  all instances of the class.




# Class Variables:





class Dog:

    species = "Canis familiaris" 
    def __init__(self, name, age):
        self.name = name  
        self.age = age     

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)


print(Dog.species)  
print(dog1.species)  
print(dog2.species)  
Dog.species = "Canis lupus familiaris"
print(dog1.species)  
print(dog2.species)  


#  Modifying Class Variables:
class Car:

    wheels = 4 

    def __init__(self, make, model):
        self.make = make
        self.model = model


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  
print(car2.wheels)  


Car.wheels = 6
print(car1.wheels)  
print(car2.wheels)  

car1.wheels = 3
print(car1.wheels)  
print(car2.wheels)  
