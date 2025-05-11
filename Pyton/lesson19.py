# lesson19
# Python default arguments
# პითონის ნაგულისხმევი არგუმენტები

# ითონში ნაგულისხმევი არგუმენტები (Default Arguments)
# არის არგუმენტები, რომლებსაც სვადასხვა ფუნქციაში გადაცემა არ
# დასჭირდება, თუ მათთვის დადგენილი არარაობა (default) უკვე არსებობს.
# თუ ფუნქციაში არ გადაეცემა კონკრეტული მნიშვნელობა, მაშინ 
# გამოიყენება ნაგულისხმევი მნიშვნელობა.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# 1. მარტივი ნაგულისხმევი არგუმენტი:

def power(base, exponent=2):
    return base ** exponent

print(power(5))    
print(power(5, 3)) 

# 2. რამდენიმე ნაგულისხმევი არგუმენტი:

def create_full_name(first_name, last_name="Doe"):
    return f"{first_name} {last_name}"

print(create_full_name("John"))          
print(create_full_name("John", "Smith")) 

# 3. ნაგულისხმევი არგუმენტები შეცვლისას:

def calculate_total(price, discount=0.1):
    return price - (price * discount)

print(calculate_total(100)) 
print(calculate_total(100, 0.2))  


# ნაგულისხმევი არგუმენტები ხელს უწყობს ფუნქციების 
# გამარტივებას და მათთვის შემოთავაზებულ პარამეტრებს, როცა
# პროგრამაში მხოლოდ ზოგადი მახასიათებლები გინდა.
