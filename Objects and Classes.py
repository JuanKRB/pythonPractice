class Circle(object):
    width = 20  # Class attribute is static
    def __init__(self, radius=3, color='blue'):
        self.radius = radius # Instance attribute
        self.color = color # Instance attribute

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)


RedCircle = Circle(10, 'red')

print(dir(RedCircle))

print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius = 3
RedCircle.color = "Red"

print(RedCircle.radius)
print(RedCircle.color)

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

print('///////////')

BlueCircle = Circle(radius=100)

print(BlueCircle.radius)


# Practice

class Car(object):

    def __init__(self, maximumSpeed, mileage, color = "white"):
        self.maximumSpeed = maximumSpeed
        self.mileage = mileage
        self.color = color
        # capacity = none // We can create an attribute in another method or set it none

    def setSeatingCapacity(self, capacity):
        self.capacity = capacity

    def printAll(self):
        print(self)
        print("maximumSpeed", self.maximumSpeed)
        print("mileage", self.mileage)
        print("color", self.color)
        print("capacity", self.capacity)

car1 = Car("200kmph", "20kmpl")
car1.setSeatingCapacity(5)

car2 = Car("180kmph", "25kmpl")
car2.setSeatingCapacity(4)

car1.printAll()
car2.printAll()











