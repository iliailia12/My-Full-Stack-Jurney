# Type casting in Python 

# Python-ში ტიპების გარდაქმნა (Type Casting) საშუალებას გაძლევთ შეცვალოთ მონაცემთა ტიპი ერთი ტიპიდან მეორეზე. ეს ხშირად საჭიროა, როდესაც გსურთ მონაცემების გამოყენება კონკრეტული ფორმატით.



# Python-ში არსებობს სამი ძირითადი ტიპი, რომლებსაც ხშირად იყენებენ: int (integer), float (floating point number) და str (string).
# 1. int (integer) - მთელი რიცხვი, მაგალითად: 5, -3, 42
# 2. float (floating point number) - ათწილადი რიცხვი, მაგალითად: 3.14, -0.5, 2.0
# 3. str (string) - ტექსტური მონაცემები, მაგალითად: "Hello", "123", "Python"
# Python-ში ტიპების გარდაქმნა (Type Casting) საშუალებას გაძლევთ შეცვალოთ მონაცემთა ტიპი ერთი ტიპიდან მეორეზე. ეს ხშირად საჭიროა, როდესაც გსურთ მონაცემების გამოყენება კონკრეტული ფორმატით.


# 1
# int() - გამოიყენება ტექსტური მონაცემების (string) მთელი რიცხვის (integer) ტიპში გარდასახვისთვის.
number_as_string = "123"
number = int(number_as_string)   

print(number + 10)   


# 2
# float() - გამოიყენება მთელი რიცხვის (integer) ათწილადი რიცხვის (floating point number) ტიპში გარდასახვისთვის.
integer_number = 10
floating_number = float(integer_number)    

print(floating_number)   

# 3
# str() - გამოიყენება მთელი რიცხვის (integer) ან ათწილადი რიცხვის (floating point number) ტექსტური მონაცემების (string) ტიპში გარდასახვისთვის.
number = 456
number_as_string = str(number)  

print("The number is: " + number_as_string)  



# 4
# boolian() - გამოიყენება ნებისმიერი ტიპის მონაცემების (integer, float, string) ბულეან ტიპში გარდასახვისთვის.

0 - False, 1 - True
0.0 - False, 1.0 - True
"" - False, "Hello" - True
 