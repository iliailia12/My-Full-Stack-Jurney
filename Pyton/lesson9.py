# გაკვეთილი 9
# String methods in Python


# პითონში სიმებიანი მეთოდები (string methods) მნიშვნელოვნად გამარტივებენ სიმბოლოების (string) სამუშაოდ გამოყენებას. 
# მათ შორის ზოგიერთი მეთოდი ეხმარება სიმბოლოების შეყვანას, შტრიხების შეცვლასა და სხვა ოპერაციებში. ქვემოთ მოცემულია სიმებიანი 
# მეთოდების ზოგადი აღწერა და მაგალითები.

# 1. lower()
# lower() მეთოდი ცვლის სიმბოლოების ყველა ასო ერთწეროვან ქვედა რეგისტრში.

text = "HELLO WORLD"
print(text.lower())  


# 2. upper()
# upper() მეთოდი ცვლის სიმბოლოების ყველა ასო დიდ რეგისტრში.

text = "hello world"
print(text.upper())  


# 3. capitalize()
# capitalize() მეთოდი ცვლის პირველ ასოს დიდზე და ყველა სხვა ასოს მცირე რეგისტრში.

text = "hello world"
print(text.capitalize()) 

# 4. title()
# title() მეთოდი ცვლის ყველა სიტყვის პირველ ასოს დიდზე.

text = "hello world"
print(text.title())  

# 5. strip()
# strip() მეთოდი აცილებს ყველა ზედმეტ ადგილს, რომელიც მდებარეობს სიმბოლოს დასაწყისსა და ბოლოს.

text = "   hello world   "
print(text.strip())  # output: hello world


# 6. lstrip()
# lstrip() მეთოდი აცილებს მხოლოდ მარცხენა მხარეს ზედმეტ ადგილებს.

text = "  hello world   "
print(text.lstrip())  


# 7. rstrip()
# rstrip() მეთოდი აცილებს მხოლოდ მარჯვენა მხარეს ზედმეტ ადგილებს.

text = "   hello world   "
print(text.rstrip())  


# 8. replace(old, new)
# replace() მეთოდი შეცვლის ყველა old ქვეკარგულ substring-ს new-ით.

text = "hello world"
print(text.replace("world", "Python"))

# 9. split()
# split() მეთოდი ყოფს სტრინგს სიად (list) და შემოაქვს ყველა სიტყვა ცალკე ელემენტად. დეფოლტად იყენებს ცარიელ სივრცეს (space) როგორც გამყოფს.

text = "hello world"
print(text.split())  

text = "apple,banana,orange"
print(text.split(','))  

# 10. join(iterable)
# join() მეთოდი აერთიანებს სტრინგის ელემენტებს და ქმნის ერთი სტრინგისგან სიიდან. გამოიყენება ცარიელი
#  სტრინგი ან სხვა სტრინგი როგორც გამყოფი.

words = ["hello", "world"]
print(" ".join(words)) 


# 11. find(substring)
# find() მეთოდი მოძებნის მაცივის substring-ს და აბრუნებს მის პირველი გამოჩენის ინდექსს. თუ substring არ მოიძებნა, აბრუნებს -1.
text = "hello world"
print(text.find("world"))  
print(text.find("Python"))

# 12. index(substring)
# index() მეთოდი მუშაობს როგორც find(), მაგრამ თუ substring არ მოიძებნა, ის გამოიმუშავებს შეცდომას ValueError.

text = "hello world"
print(text.index("world"))

# 13. count(substring)
# count() მეთოდი დაათვლიდა substring-ის რაოდენობას სტრინგში.

text = "hello hello hello"
print(text.count("hello")) 


# 14. startswith(prefix)
# startswith() მეთოდი შეამოწმებს, თუ სტრინგი იწყება მოცემული prefix-ით.

text = "hello world"
print(text.startswith("hello"))  
print(text.startswith("world"))  

# 15. endswith(suffix)
# endswith() მეთოდი შეამოწმებს, თუ სტრინგი მთავრდება მოცემული suffix-ით.

text = "hello world"
print(text.endswith("world"))  
print(text.endswith("hello"))  

# 16. isalpha()
# isalpha() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ ასოებს (არ შეიცავს ციფრებს, მითითებებს ან სივრცეებს).


text = "hello"
print(text.isalpha()) 

text = "hello123"
print(text.isalpha())  

# 7. isdigit()
# isdigit() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ ციფრებს.


text = "12345"
print(text.isdigit())  

text = "123a45"
print(text.isdigit()) 

# 18. isalnum()
# isalnum() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ ასოებს და ციფრებს.

text = "hello123"
print(text.isalnum()) 

text = "hello 123"
print(text.isalnum()) 

# 19. isspace()
# isspace() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ ცარიელ სივრცეებს.

text = "   "
print(text.isspace())  

text = "hello"
print(text.isspace())


# 20. isupper()
# isupper() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ დიდ ასოებს.


text = "HELLO"
print(text.isupper()) 

text = "Hello"
print(text.isupper())  

# 21. islower()
# islower() მეთოდი შეამოწმებს, თუ სტრინგი შეიცავს მხოლოდ მცირე ასოებს.

text = "hello"
print(text.islower())  

text = "Hello"
print(text.islower())  

# 22. zfill(width)
# zfill() მეთოდი სტრინგის წინ ჩასვამს საჭირო რაოდენობის ციფრებს (ზეროებს), რომ სტრინგის სიგრძე მიაღწიოს მოცემულ width-ს.


text = "42"
print(text.zfill(5)) 
# 23. format()
# format() მეთოდი გამოგიყენებთ კონკრეტული სტრინგის ადგილებში ცვლადების ჩასმისთვის.

name = "John"
age = 25
print("My name is {}, and I am {} years old.".format(name, age))

# 24. f-strings (formatted string literals)
# f-strings გამოიყენება პითონის 3.6 ვერსიიდან და საშუალებას გაძლევთ გაერთიანოთ ცვლადები სტრინგში უფრო დასამახსოვრებლად და მარტივად.

name = "Alice"
age = 30
print(f"My name is {name}, and I am {age} years old.")
