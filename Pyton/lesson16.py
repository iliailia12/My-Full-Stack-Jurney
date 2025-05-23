 # lesson16.py
# პითონის 2D კოლექციები

# პითონში 2D კოლექციები ხშირად გამოიყენება, როდესაც საჭიროა მონაცემების ორგანიზება ორ
# განზომილებაში (მაგალითად, გრაფიკების ან ცხრილების წარმოქმნა, რაც აერთიანებს რამდენიმე 
# ცვლადს ერთში). ასეთი კოლექციები, ძირითადად, ლისტებსა
# და ნუმერირებულ დათვლადებში გამოიყენება, რათა შეგროვდეს მონაცემები ორ განზომილებაში.

# პითონში ყველაზე ხშირად გამოყენებული 2D კოლექციები არიან ლისტები და numpy-ს მასივები 
# (თუ მუშაობთ გრაფიკებითა და მათემატიკური ოპერაციებით).

# 1. 2D ლისტები (Lists of Lists)
# 2D ლისტი შეიძლება განვიხილოთ როგორც ლისტი, რომელიც შეიცავს სხვა ლისტებს. ეს 
# ნიშნავს, რომ ყოველი ელემენტი თავად წარმოადგენს ლისტს, და თითოეული ლისტი 
# შეიძლება შეიცავდეს სხვადასხვა რაოდენობის ელემენტებს.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 2D კოლექციები და მათი გამოყენების შემთხვევები
# მათემატიკური ოპერაციები: NumPy საშუალებას იძლევა მარტივად განახორციელოთ მათემატიკური
# ოპერაციები 2D მასივებზე, როგორიცაა მათ შორის დამატება, გამოკლენა,
# გამრავლება, ტრუნკირება და სხვა.
# გრაფიკული მონაცემები: 2D მასივები ხშირად გამოიყენება გრაფიკების და ხატულების 
# მონაცემების შესანახად, რათა შეძლოთ მათი ვიზუალიზაცია.
# ცხრილები: 2D კოლექციები გამოიყენება ცხრილების შესანახად, რომლებიც შეიცავს
# რიგებს და სვეტებს. ასეთ მონაცემებს ხშირად ინახავენ ცხრილების ფორმატში (მაგალითად, მონაცემთა ბაზებში).

