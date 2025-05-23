# User input in Python is easy + exercises 

# input() ფუნქცია გამოიყენება მომხმარებლისგან მონაცემების მისაღებად. ეს ფუნქცია მონაცემებს სტრინგის (ტექსტის) სახით აბრუნებს. შეგიძლიათ მონაცემები სხვა ტიპებად გარდაქმნათ, მაგალითად, რიცხვებად ან მცურავ რიცხვებად.

# 1
# input() ფუნქციის გამოყენების მაგალითი:
name = input("შეიყვანეთ თქვენი სახელი: ")
print("გამარჯობა, " + name + "!")

# 2
# input() ფუნქციის გამოყენება რიცხვების შესატყვისად:
age = input("შეიყვანეთ თქვენი ასაკი: ")
print("თქვენი ასაკი არის: " + age)

# 3
# input() ფუნქციის გამოყენება რიცხვების შესატყვისად:
number = input("შეიყვანეთ რიცხვი: ")
number = int(number)  # გარდაქმნა მთელი რიცხვის ტიპში
print("თქვენი რიცხვი არის: " + str(number))

# 4
# input() ფუნქციის გამოყენება მცურავი რიცხვების შესატყვისად:
decimal_number = input("შეიყვანეთ მცურავი რიცხვი: ")
decimal_number = float(decimal_number)  # გარდაქმნა მცურავი რიცხვის  
print("თქვენი მცურავი რიცხვი არის: " + str(decimal_number))

# 5
# input() ფუნქციის გამოყენება სიის შესატყვისად:
fruits = input("შეიყვანეთ ხილი (გამიჯნეთ კომას): ")
fruits = fruits.split(",")  
print("თქვენი ხილები არიან: " + str(fruits))

# 6
# input() ფუნქციის გამოყენება ლოგიკური მნიშვნელობების შესატყვისად:
is_student = input("ხართ სტუდენტი? (True/False): ")
is_student = is_student.lower() == "true"  
print("თქვენი სტატუსი არის: " + str(is_student))

# 7
# მომხმარებლისგან მონაცემების მიღება
სახელი = input("შეიყვანეთ თქვენი სახელი: ")
ასაკი = int(input("შეიყვანეთ თქვენი ასაკი: "))
 
print("გამარჯობა,", სახელი + "!")
print("თქვენი ასაკია:", ასაკი)

# 8
# მომხმარებლისგან ორი რიცხვის მიღება და მათი ჯამის გამოთვლა.
რიცხვი1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
რიცხვი2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
print("ჯამი არის:", რიცხვი1 + რიცხვი2)

# 9
# მომხმარებლისგან მისი საყვარელი ფერის მიღება და შეტყობინების ჩვენება.
ფერი = input("რა არის თქვენი საყვარელი ფერი? ")
print("ვაუ! მეც ძალიან მიყვარს", ფერი, "!")

# 10
# სამი მონაცემის მიღება ერთ ხაზში და მათი ჩვენება.
მონაცემები = input("შეიყვანეთ სამი მნიშვნელობა სივრცეებით გამოყოფილი: ").split()
print("თქვენ შეიყვანეთ:", მონაცემები)
