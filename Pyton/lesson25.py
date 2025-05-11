# lesson25
# Python MATCH-CASE STATEMENTS

# Python-ში მატჩის შემთხვევის განცხადებები დაინერგა Python 3.10-ში, 
# როგორც შაბლონების შესატყვისი ძლიერი ინსტრუმენტი. ეს სინტაქსი
# საშუალებას გაძლევთ დააკავშიროთ და გაანადგუროთ მნიშვნელობები
# უფრო იკითხებადი და მოქნილი გზით ტრადიციულ
# if-elif-else ჯაჭვებთან შედარებით.

# Literal Patterns: Match specific values.

# Variable Patterns: Capture the value and assign it to a variable.

# Sequence Patterns: Match sequences (like lists, tuples).

# Mapping Patterns: Match dictionaries or key-value pairs.

# Class Patterns: Match class instances and their attributes.






 # Literal Patterns: ემთხვევა კონკრეტული მნიშვნელობები.

# Variable Patterns: დააფიქსირეთ მნიშვნელობა და მივანიჭეთ იგი ცვლადს.

# თანმიმდევრობის ნიმუშები: თანმიმდევრობების შესატყვისი (როგორიცაა სიები, ტოპები).

# რუკების ნიმუშები: ემთხვევა ლექსიკონებს ან გასაღები-მნიშვნელობის წყვილებს.

# კლასის შაბლონები: ემთხვევა კლასის მაგალითებს და მათ ატრიბუტებს.




# 1. მარტივი
def match_number(n):
    match n:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Unknown"

print(match_number(2))  
print(match_number(5))  




# 2. Using Wildcard (_):
# ნიმუში ემთხვევა ყველაფერს და ის გამოიყენება "ნაგულისხმევი" შემთხვევისთვის.

def match_color(color):
    match color:
        case 'red':
            return "Stop"
        case 'green':
            return "Go"
        case 'yellow':
            return "Slow down"
        case _:
            return "Unknown color"

print(match_color('green'))  
print(match_color('blue')) 

# 3. Variable Pattern:
# თქვენ შეგიძლიათ გამოიყენოთ ცვლადები შაბლონში მნიშვნელობების აღსაწერად და მათი მოგვიანებით გამოყენება ქეისის ბლოკში.
def match_person(person):
    match person:
        case ('John', age):
            return f"John is {age} years old"
        case ('Alice', age):
            return f"Alice is {age} years old"
        case (_, age):
            return f"Some person is {age} years old"
        
print(match_person(('John', 30)))  
print(match_person(('Bob', 25)))   

# 4. Sequence Patterns:
# შეგიძლიათ დაამთხვიოთ თანმიმდევრობები, როგორიცაა სიები ან ტოპები.

def match_sequence(seq):
    match seq:
        case [1, 2, 3]:
            return 
        case [1, 2, *rest]:  
            return f"Starts with [1, 2], and the rest are {rest}"
        case _:
            return "No match"

print(match_sequence([1, 2, 3]))         
print(match_sequence([1, 2, 4, 5, 6]))  

# 5. Mapping Patterns:
#შეგიძლიათ ლექსიკონების შედარება გასაღებებისა და მნიშვნელობების მიხედვით.

def match_dict(d):
    match d:
        case {'name': name, 'age': age}:  
            return f"Name: {name}, Age: {age}"
        case {'name': name}: 
            return f"Name: {name}"
        case _:
            return "No match"

print(match_dict({'name': 'John', 'age': 30}))  
print(match_dict({'name': 'Alice'}))    

# 6. Class Patterns:
# ეგიძლიათ დაამთხვიოთ კლასის ინსტანციები და ამოიღოთ ატრიბუტები.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def match_class(obj):
    match obj:
        case Person(name=name, age=age):  
            return f"Person: {name}, Age: {age}"
        case _:
            return "Not a Person"

p = Person("Alice", 30)
print(match_class(p)) 


# Complex Patterns:
# თქვენ ასევე შეგიძლიათ დააკავშიროთ მრავალი ნიმუში, გამოიყენოთ | ალტერნატიული შაბლონებისთვის და გამოიყენეთ როგორც მნიშვნელობების ამოსაღებად.


def match_complex(data):
    match data:
        case [x, y] if x == y:
            return f"Matched a pair of equal values: {x} and {y}"
        case (x, y) | (y, x):  
            return f"Matched a pair: {x} and {y}"
        case _:
            return "No match"

print(match_complex([5, 5])) 
print(match_complex([3, 2]))   








# Key Features:
# Wildcards (_) for default matching.
# Sequence Matching with * to match parts of sequences.
# Class Patterns for matching specific attributes of objects.
# Guards (if clauses) can be used for more refined matching.
# Logical OR (|) to combine multiple patterns.
# When to Use match-case:
# Complex conditionals: When you need to check multiple conditions 
# on an object and want cleaner, more readable code.
# Pattern Matching: When you need to destructure objects (lists, tuples,
#  dictionaries, etc.) directly in the match statement.
# Replacing long if-elif-else chains: If you have 
# several conditions
#  based on distinct values or structures.



# ძირითადი მახასიათებლები:
# Wildcards (_) ნაგულისხმევი შესატყვისისთვის.
# თანმიმდევრობის შესატყვისი *-ით მიმდევრობის ნაწილების შესატყვისად.
# კლასის შაბლონები ობიექტების კონკრეტული ატრიბუტების შესატყვისი.
# მცველები (თუ პუნქტები) შეიძლება გამოყენებულ იქნას უფრო დახვეწილი შესატყვისისთვის.
# ლოგიკური ან (|) მრავალი შაბლონის გაერთიანებისთვის.
# როდის გამოვიყენოთ მატჩის შემთხვევა:
# რთული პირობითობა: როდესაც საჭიროა მრავალი პირობის შემოწმება
# ობიექტზე და მინდა უფრო სუფთა, უფრო წასაკითხი კოდი.
# შაბლონის შესატყვისი: როდესაც გჭირდებათ ობიექტების განადგურება (სიები, ტოპები,
# ლექსიკონი და ა.შ.) პირდაპირ მატჩის განცხადებაში.
# გრძელი if-elif-else ჯაჭვების გამოცვლა: თუ გაქვთ
# რამდენიმე პირობა
# ეფუძნება განსხვავებულ ღირებულებებს ან სტრუქტურებს.