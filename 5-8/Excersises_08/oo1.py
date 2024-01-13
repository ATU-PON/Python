"""
Simple Class by JOR, by convention, use camel case to name classes
"""

# Create a class 
class JORzClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

class PONClass:
    def __init__(self, my_message):
        print("Running Constructor for PON Class")
        self.message = my_message
    
    def my_method(self):
        print(self.message)
        
# Create an instance of PONClass

my_class2 = PONClass("Hello There")

# Call the my_method of MyClass2
my_class2.my_method()

# Print the type of my_class2

print(type(my_class2))
