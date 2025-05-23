# გაკვეთილი 15
# Python lists, sets, and tuples explained 

# პითონში სიები, კომპლექტები და ტოპები არის სამი ჩაშენებული მონაცემთა სტრუქტურა, რომლებიც ფართოდ გამოიყენება 
# ნივთების კოლექციების შესანახად და სამართავად. თითოეულ ამ მონაცემთა სტრუქტურას აქვს საკუთარი მახასიათებლები და გამოყენების შემთხვევები. 
# განვიხილოთ თითოეული დეტალურად.

# 1. სიები
# სია Python-ში არის ნივთების მოწესრიგებული, ცვალებადი (მოდიფიცირებადი) კოლექცია. სიებს შეუძლიათ შეინახონ სხვადასხვა ტიპის მონაცემთა ელემენტები
# (მაგ., მთელი რიცხვები, სტრიქონები, სხვა სიები) და დაუშვან ელემენტების დუბლიკატი.

# სიების მახასიათებლები:
# შეკვეთილი: სიის ელემენტებს აქვთ განსაზღვრული თანმიმდევრობა. ეს ნიშნავს, რომ სიაში ელემენტების თანმიმდევრობა შენარჩუნებულია.
# ცვალებადი: სიების შეცვლა შესაძლებელია (ერთეულების დამატება, წაშლა ან შეცვლა).
# ნებას რთავს დუბლიკატებს: სიებს შეიძლება ჰქონდეთ რამდენიმე ელემენტი იგივე მნიშვნელობით.







# ელემენტების წვდომა: შეგიძლიათ ელემენტებზე წვდომა მათი ინდექსით.
my_list = [1, 2, 3, "apple", 5.5]
print(my_list[0]) 

# ელემენტების დამატება: ელემენტების დასამატებლად გამოიყენეთ append(), insert(), ან extend().

my_list.append(6)  
my_list.insert(1, "banana")  

# ელემენტების წაშლა: გამოიყენეთ remove(), pop() ან del ნივთების ამოსაშლელად.

my_list.remove("apple")  
my_list.pop(1)  
del my_list[0] 

# დაჭრა: შეგიძლიათ ქვესიის ამონაწერი დაჭრის გამოყენებით

# ამის გამოყენება კარგად არ ვიცი