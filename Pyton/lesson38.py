# lesson38
#  Python COMPOSITION




# პითონის კომპოზიცია (Composition)
# კომპოზიცია არის ობიექტების ურთიერთობა, სადაც ერთი ობიექტი არის 
# სხვა ობიექტის ნაწარმოების ნაწილი, და ამ ობიექტის ცხოვრება მთლიანად
#  დამოკიდებულია მშობელ ობიექტზე. ეს არის "part-of" ურთიერთობა,
#  სადაც მშობელი ობიექტი აკონტროლებს შვილობილი ობიექტის სიცოცხლეს.
#  კომპოზიციის შემთხვევაში, თუ მშობელი ობიექტი განადგურდება, შვილობილი 
# ობიექტი ავტომატურად განადგურებულია.

# კომპოზიციის განმარტება:
# "part-of" ურთიერთობა: კომპოზიცია ნიშნავს, რომ ერთი ობიექტი
#  წარმოადგენს მეორეს ნაწილს.
# დამოკიდებულება: შვილობილი ობიექტები მთლიანად დამოკიდებულია 
# მშობელზე. თუ მშობელი ობიექტი განადგურებულია, მისი შვილობილი 
# ობიექტებიც განადგურებულია.
# მტკიცე კავშირი: სხვა სიტყვებით რომ ვთქვათ, შვილობილი ობიექტები არ არსებობს დამოუკიდებლად მშობელ ობიექტის გარეშე.
# კომპოზიციის მაგალითი:
# მოდით, განვიხილოთ House და Room კლასები. სახლში ოთახები 
# კომპოზიციის სახით "შეიცავს" ოთახებს. თუ House განადგურებულია,
#  მისი Room-ები აღარ არსებობს.


class Room:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class House:
    def __init__(self, house_name):
        self.house_name = house_name
        self.rooms = []  # House has rooms as part of its composition

    def add_room(self, room):
        self.rooms.append(room)

    def get_rooms(self):
        return [room.get_name() for room in self.rooms]


room1 = Room("Living Room")
room2 = Room("Bedroom")


house = House("My House")
house.add_room(room1)
house.add_room(room2)






# კომპოზიციის მაგალითი უფრო გამარტივებული:

class Engine:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"Starting engine {self.model}")

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine("V8")  # Car has an engine as a part of it

    def start(self):
        print(f"Starting car {self.model}")
        self.engine.start()  # Starting the car's engine

# Create a Car object
car = Car("Mustang")

# Start the car, which will also start the engine as part of its composition
car.start()
