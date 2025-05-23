# While loops in Python 

# Python-ში while ციკლი გამოიყენება კოდის ბლოკის განმეორებით შესასრულებლად, სანამ მოცემული პირობა მართალია. ეს ციკლი განსაკუთრებით სასარგებლოა, როდესაც წინასწარ არ იცით, რამდენჯერ უნდა შესრულდეს კოდი.

# რიცხვების დაბეჭდვა 1-დან 5-მდე
i = 1
while i <= 5:
    print(i)
    i += 1  




# 2
# break ოპერატორი: გამოიყენება ციკლის ნაადრევად შესაწყვეტად.

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1


# 3
# continue ოპერატორი: ციკლის მიმდინარე გამეორების გამოტოვება და შემდეგზე გადასვლა.

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)



# 4
# else ბლოკი: შეგიძლიათ გამოიყენოთ else ციკლთან ერთად, რათა კოდი შესრულდეს, როცა პირობა მცდარი ხდება.

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("ციკლი დასრულდა!")
