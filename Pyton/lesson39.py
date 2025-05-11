#  lesson39
#  Python NESTED CLASSES



# პითონის Nested Classes (გამოყენება შიდა კლასების)
# Nested Class არის კლასის კლასში განსაზღვრული
#  კლასი, ანუ როდესაც ერთი კლასი არის სხვა
#  კლასის შიგნით. პითონში კლასი შეიძლება განსაზღვროს სხვა კლასის შიგნით, 
# და ეს შიდა კლასები, როგორც წესი, გამოიყენება გარკვეულ ფუნქციონალთან
#  დაკავშირებულ შიდა სტრუქტურების განსაზღვრაში.

# Nested Classes შეიძლება იყოს სასარგებლო, როცა გვსურს, რომ შინაგანი 
# (შიდა) კლასის ტიპი იყოს დამოკიდებული მისი გარე (მშობელი) კლასის
#  კონტექსტზე.

# როგორ მუშაობს Nested Class?
# შიდა კლასი არის გარე კლასის ნაწილი, ამიტომ ის შეიძლება გამოიყენოს
#  გარე კლასის ატრიბუტები და მეთოდები, თუმცა არ ექნება წვდომა გარე 
# კლასის წევრებთან პირდაპირი გზით.
# შიდა კლასების გამოყენება ხშირად გამოიყენება, როდესაც ერთი კლასი 
# უნდა განახორციელოს ძალიან სპეციფიკური ფუნქციონალი, რომელიც 
# მხოლოდ მისი მშობლიური კლასის კონტექსტშია საჭირო.
# Nested Class-ის მაგალითი:

class OuterClass:
    def __init__(self, name):
        self.name = name
    
    def outer_method(self):
        print(f"Outer method called from {self.name}")
    
    class InnerClass:
        def __init__(self, inner_name):
            self.inner_name = inner_name
        
        def inner_method(self):
            print(f"Inner method called from {self.inner_name}")
    

outer_object = OuterClass("Outer Object")
inner_object = OuterClass.InnerClass("Inner Object")

outer_object.outer_method()  
inner_object.inner_method()   




# Nested Class და მეთოდები:
# შიდა კლასი შეიძლება შექმნას გარე კლასის მეთოდებში, და მისი შექმნა 
# პირდაპირაც შეიძლება.


class OuterClass:
    def __init__(self, name):
        self.name = name
    
    class InnerClass:
        def __init__(self, inner_name):
            self.inner_name = inner_name

        def inner_method(self):
            print(f"Inner method called from {self.inner_name}")
    
    def create_inner(self, inner_name):
        return self.InnerClass(inner_name)


outer_object = OuterClass("Outer Object")
inner_object = outer_object.create_inner("Inner Object")

inner_object.inner_method()  
