# გაკვეთილი 6
# Python are easy (if, elif, else) 🤔

# if განაცხადი საშუალებას გაძლევთ შეამოწმოთ არის თუ არა პირობა True და თუ ასეა, შეასრულოთ კოდის ბლოკი. მაგ

age = 18

if age >= 18:
    print("You are an adult.")

# The else Statement

# სხვა განცხადება გამოიყენება კოდის ბლოკის შესასრულებლად, როდესაც if განაცხადის მდგომარეობა არის False. ის არჩევითია, მაგრამ 
# შეიძლება გამოყენებულ იქნას ალტერნატიული 
# მოქმედების უზრუნველსაყოფად.მაგ

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a kid.")



# გაერთიანებული ვერსია

temperature = 75

if temperature > 85:
    print("It's too hot!")
elif temperature > 70:
    print("It's a nice day.")
elif temperature > 50:
    print("It's a bit chilly.")
else:
    print("It's cold!")
