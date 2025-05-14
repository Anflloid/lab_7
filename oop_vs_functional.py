# Процедурний підхід
def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = 5
height = 3
print("Protsedurnyy pidhid:")
print("Ploshcha:", calculate_area(width, height))
print("Perymetr:", calculate_perimeter(width, height))



# ООП підхід
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print("\nOOP pidhid:")
print("Ploshcha:", rect.area())
print("Perymetr:", rect.perimeter())
