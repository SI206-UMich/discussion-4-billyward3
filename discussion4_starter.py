class Rectangle():
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    def __init__(self, width, height):
        self.width = width
        self.height = height


    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)


    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    def verify_input(self):
        if (self.width > 0 and self.height > 0):
            return True
        return False 


    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    def area(self):
        if not self.verify_input():
            return "Invalid input"
        return self.width * self.height


    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    def perimeter(self):
        if not self.verify_input():
            return "Invalid input"
        return 2 * self.width + 2 * self.height
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()