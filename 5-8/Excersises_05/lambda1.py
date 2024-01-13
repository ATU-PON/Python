## Excersise 3 - Wire a lambda funciton to calculate the volume of a cylinder

cylinder_volume = lambda r, h: 3.14159265 * r**2 * h

radius = 3.0
height = 5.0
volume = cylinder_volume(radius, height)
print(f"The volume of the cylinder is {volume:.2f} cubic units")
