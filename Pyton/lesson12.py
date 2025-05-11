# # გაკვეთილი 12
# While loops in Python 

# Python-ში while loop გამოიყენება კოდის ბლოკის შესასრულებლად, სანამ მითითებული პირობა არის True. 
# ის არაერთხელ ახორციელებს კოდს მარყუჟის შიგნით, სანამ მდგომარეობა არ გახდება False.

# როგორ მუშაობს:
# მდგომარეობა ფასდება ყოველი გამეორების წინ.
# თუ პირობა არის True, ციკლის შიგნით კოდის ბლოკი გადის.
# თუ პირობა გახდება False, მარყუჟი წყდება და პროგრამა აგრძელებს შემდეგი დებულებით მარყუჟის შემდეგ.

#მაგალითი 1: ძირითადი while ციკლი
count = 0
while count < 5:
    print(count)
    count += 1  

# მაგალითი 2: გამოყენება while იმ პირობით, რომელიც საბოლოოდ ხდება False

while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
        print("Exiting loop.")
        break 
    else:
        print(f"You typed: {user_input}")

# მაგალითი 4: while loop else ერთად

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop has finished.")

# მაგალითი 5: nested while loops

i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
