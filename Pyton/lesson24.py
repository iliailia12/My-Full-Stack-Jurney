# lesson24
#  LIST COMPREHENSIONS 

# სიების გააზრება პითონში იძლევა სიების შექმნის მოკლე გზას. ისინი საშუალებას გაძლევთ შექმნათ ახალი სია 
# გამონათქვამების გამოყენებით არსებული იტერაბლის თითოეულ ელემენტზე (როგორიცაა სია ან დიაპაზონი), 
# სურვილისამებრ გაფილტროთ ელემენტები რომელიმე პირობის საფუძველზე.

# 1. Creating a list of squares:
squares = [x**2 for x in range(5)]
print(squares)


# 2. Converting a list of strings to uppercase:
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)


# 3. Filtering even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# 4. Flattening a list of lists:
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)


# 5. Creating a list of tuples:
numbers = [1, 2, 3, 4]
squared_tuples = [(x, x**2) for x in numbers]
print(squared_tuples)


# 6. Using multiple conditions in the filter:
numbers = range(1, 20)
result = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(result)


# 7. Using nested loops:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)


# Using a for-loop:
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)


