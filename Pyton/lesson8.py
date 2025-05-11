# გაკვეთილი 8
#  Python CONDITIONAL EXPRESSIONS პითონის პირობითი გამონათქვამები 

# პითონში პირობითი გამონათქვამები (conditional statements) გამოიყენება იმისთვის, რომ პროგრამა მიიღოს განსხვავებული
# გადაწყვეტილებები განსაზღვრული პირობების მიხედვით. პითონის მთავარ პირობითი გამონათქვამებია: if, elif, და else.

# 1. if - პირობა
# if გამოიყენება, როდესაც გსურთ შეამოწმოთ გარკვეული პირობა და, თუ ის ჭეშმარიტია, შეასრულოთ გარკვეული მოქმედება.

age = 20

if age >= 18:
    print("You are an adult.")

# else - წინააღმდეგ შემთხვევაში
# else გამოიყენება, როდესაც პირობა არ შესრულდა და გსურთ შეასრულოთ სხვა მოქმედება.

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# elif - დამატებითი პირობა
# elif (else if) გამოიყენება, როდესაც გსურთ გამორიცხოთ რამდენიმე პირობა. თუ პირველი პირობა არ
#  შესრულდა, შეიძლება შეამოწმოთ დამატებითი პირობა.

age = 20

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")


# მრავალჯერადი პირობა (Nested Conditions)

# შეძლებთ გამოყენება if/else ნესტედ (შიდაპირობითი პირობები), როდესაც ერთი პირობა იყენებს სხვა პირობას.

age = 25
is_student = True

if age >= 18:
    if is_student:
        print("You are an adult and a student.")
    else:
        print("You are an adult but not a student.")
else:
    print("You are a აუუუ მოკლედ რაა dumb.")



# ლოგიკური ოპერატორები პირობის გამონათქვამებში
# if-ში შეგიძლიათ გამოიყენოთ ლოგიკური ოპერატორები, როგორიცაა and, or, not, რომ შეამოწმოთ უფრო რთული პირობები.

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert.")
else:
    print("You cannot enter the concert.")

# 6. in და not in ოპერატორები
# შეიძლება გამოიყენოთ in და not in, როდესაც გსურთ შეამოწმოთ, თუ ელემენტი არსებობენ გარკვეულ სიაში.

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# if მარტივი ფორმა (Ternary Operator)
# შეიძლება გამოიყენოთ მარტივი ფორმა, რომელსაც უწოდებენ Ternary Operator (მცირე პირობის სტრუქტურა).

age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)
