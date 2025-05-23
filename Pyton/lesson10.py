# გაკვეთილი 10
# # String indexing in Python is easy ✂️

# # პითონში სიმებიანი ინდექსირება (string indexing) ძალიან მარტივია და საშუალებას აძლევს პროგრამისტებს, სწრაფად და
# # ეფექტურად მიიღონ ან შეცვალონ კონკრეტული სიმბოლოს პოზიცია სტრინგში.

# # სიმებიანი ინდექსირება
# # პითონში, სტრინგი არის სიმბოლოების სერია, ანუ _sequence. თითოეული სიმბოლო წარმოდგენილია ინდექსით, რომელიც მიუთითებს
# # სიმბოლოს პოზიციას. ინდექსები იწყება 0-დან, ანუ პირველი სიმბოლო სტრინგში
# # აქვს ინდექსი 0, მეორე — 1, და ასე შემდეგ.

# ნორმალური ინდექსი
# python
# Copy code
# text = "Python"
# # ინდექსები:   0   1   2   3   4   5
# text[0] მოიძიებს პირველ სიმბოლოს, ანუ "P"
# text[1] მოიძიებს მეორე სიმბოლოს, ანუ "y"
# text[2] მოიძიებს მესამე სიმბოლოს, ანუ "t"
# უარყოფითი ინდექსები
# პითონში ინდექსი შეიძლება იყოს უარყოფითიც, რაც ნიშნავს რომ შეიძლება წაიკითხო სიმბოლოები სტრინგის ბოლოსგან. უარყოფითი ინდექსები იწყება -1-დან, რაც ნიშნავს, რომ -1 მიუთითებს ბოლო სიმბოლოს, -2 — წინაზე, და ასე შემდეგ.


# text = "Python"
# # ინდექსები:    0   1   2   3   4   5
# # უარყოფითი ინდექსები: -6  -5  -4  -3  -2  -1
# # text[-1] დაბრუნებს "n" (ბოლო სიმბოლო)
# # text[-2] დაბრუნებს "o" (ბოლო მეორე სიმბოლო)
# # text[-6] დაბრუნებს "P" (პირველი სიმბოლო)
# # სიმებიანი ინდექსირების მაგალითები

# text = "Python"

# # ნორმალური ინდექსები
# print(text[0])  # Output: P
# print(text[1])  # Output: y
# print(text[2])  # Output: t
# print(text[3])  # Output: h

# # უარყოფითი ინდექსები
# print(text[-1])  # Output: n
# print(text[-2])  # Output: o
# print(text[-3])  # Output: h
# # გამოყენება ინდექსირების დროს
# # 1. სიმბოლოების ამოკითხვა სტრინგში

# text = "Programming"
# print(text[0])  # P
# print(text[5])  # a
# print(text[-1]) # g
# # 2. ინდექსირების შეცვლა
# text = "Python"
# # შეცვლა არ მუშაობს პირდაპირ ინდექსირებით, რადგან სტრინგი არის Immutable ტიპი
# # text[0] = "J"  # TypeError

# # პითონში სტრინგები immutable (უხილავია) ტიპია, რაც ნიშნავს, რომ მათი ცვლის მცდელობა გამოიწვევს შეცდომას. 
# # მაგრამ შესაძლებელია შექმნათ ახალი სტრინგი ინდექსირების გამოყენებით.

# # 3. ინდექსირება და slicing

# text = "Python"

# # სინტაქსი: text[start:end:step]
# # ამოკითხავება პირველ 3 სიმბოლოს
# print(text[0:3])  # Output: Pyt

# # ამოკითხავება ყოველი მეორე სიმბოლოს
# # print(text[::2])  
# # start - დაწყების ინდექსი (დაახლოებით სად დაიწყება).
# # end - შეჩერების ინდექსი (სად შეჩერდება).
# # step - რამდენად ხშირად აირჩიოს სიმბოლოები (როგორც ჭამაში every nth).
# # მნიშვნელოვანი მომენტები
# # ინდექსირება სტრინგის სიმბოლოების წვდომისთვის, როგორც ციფრებთან (პოზიტიური და უარყოფითი ინდექსი).
# # slice საშუალებას იძლევა ამოკითხავების ნაწილი სტრინგიდან.
# # immutable სტრინგები (შეცვლა პირდაპირ არ ხდება).
# # start და end უნდა იყოს valid ინდექსები. end ყოველთვის არ მოიცავს ბოლო სიმბოლოს.