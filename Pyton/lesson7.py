# Logical operators in Python 
# ლოგიკური ოპერატორები Python-ში გამოიყენება მრავალი პირობის გაერთიანებისთვის if, elif და while 
# განცხადებებში. ისინი საშუალებას გვაძლევს მივიღოთ გადაწყვეტილებები მრავალი პირობის საფუძველზე.

# პითონში სამი ძირითადი ლოგიკური ოპერატორია:

# and – აბრუნებს True-ს, თუ ორივე პირობა True არის.
# or– აბრუნებს True-ს, თუ ერთი პირობა მაინც არის True.
# not – აბრუნებს პირობას (აბრუნებს True-ს თუ პირობა False-ია და პირიქით).მაგ

# and
x = 10
y = 5

if x > 5 and y < 10:
    print("Both conditions are True!")
else:
    print("At least one condition is False.")


# or
x = 3
y = 7

if x > 5 or y < 10:
    print("At least one condition is True!")
else:
    print("Both conditions are False.")


# not
is_raining = False

if not is_raining:
    print("It's a sunny day!")
else:
    print("It's raining!")
