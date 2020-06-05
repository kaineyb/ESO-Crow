# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def __init__(self, name, color, value):
        self.name = name
        self.colour = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str
# # your code goes here
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
#  and car2 to be a blue van named Jump worth $10,000.00.


# car1 = Vehicle("Fer", "Red", 60000)
# car2 = Vehicle("Jump", "Blue", 10000)


# # test code
# print(car1.name)
# print(car2.description())


class People:
    instances = []

    potatoes = []

    def __init__(self, name, age, potato):
        self.name = name
        self.age = age
        self.__class__.instances.append([name, age])
        self.__class__.potatoes.append(potato)

    @classmethod
    def printInstances(cls):
        for instance in cls.instances:
            print(instance)

    @classmethod
    def printPotatoes(cls):
        for potato in cls.potatoes:
            print(potato)


Kaine = People("Kaine", 33, 1)
Lucy = People("Lucy", 28, 5)

People.printInstances()
People.printPotatoes()
