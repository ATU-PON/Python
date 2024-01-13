"""
Class template by JOR

Revision History
06OCT22: Alpha
11OCT23: Beta
"""

class MyTemplate:
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        # Initialize the instance attributes
        self.attr1 = attribute1
        self.attr2 = attribute2
        print("Constructor ran")

    # Define a class object attribute, it will be the same for any instance of the class
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752

    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

# Instantiate the class
my_object = MyTemplate("Paul", True)

# Check the class object attributes
print(MyTemplate.class_object_attribute1, MyTemplate.class_object_attribute2)

# Call the method on the object
my_object.my_method1()

