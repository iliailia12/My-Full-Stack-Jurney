# lesson23
# Python MEMBERSHIP OPERATORS 

# Python-ში წევრობის ოპერატორები გამოიყენება 
# იმის შესამოწმებლად, არის თუ არა მნიშვნელობა 
# ან ცვლადი ნაპოვნი თანმიმდევრობაში (როგორიცაა სტრიქონები, სიები, 
# ტოპები, კომპლექტები ან ლექსიკონები). არსებობს ორი წევრობის ოპერატორი:

# in: აბრუნებს True-ს, თუ მითითებული მ
# ნიშვნელობა ნაპოვნია თანმიმდევრობაში.
# not in: აბრუნებს True-ს, თუ მითითებული მნიშვნელობა არ არის 
# ნაპოვნი თანმიმდევრობაში.
# წევრობის ოპერატორების გამოყენება
# 1. ოპერატორი
# ოპერატორი in ამოწმებს არის თუ არა მნიშვნელობა მიმდევრობაში
# . თუ მნიშვნელობა ნაპოვნია, ის აბრუნებს True; 
# წინააღმდეგ შემთხვევაში, ის აბრუნებს False-ს.

# With a List:

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  
print(6 in my_list)  

# With a String:

my_string = "Hello, World!"
print("Hello" in my_string)  
print("Python" in my_string)  

# With a Set:

my_set = {1, 2, 3, 4, 5}
print(2 in my_set)  # Output: True
print(6 in my_set)  # Output: False



# With a List:

my_list = [1, 2, 3, 4, 5]
print(6 not in my_list) 
print(3 not in my_list)  

# With a String:

my_string = "Hello, World!"
print("Python" not in my_string)  
print("Hello" not in my_string)    

# With a Set:

my_set = {1, 2, 3, 4, 5}
print(6 not in my_set) 
print(2 not in my_set) 

# With a Dictionary:

my_dict = {"name": "Alice", "age": 30}
print("Alice" not in my_dict)
print("age" not in my_dict)     
