import random

class Animal():
    """Animal parent class to contain name, age, and hunger attributes.
    Has methods to reduce and increase hunger. All attributes are private"""
    def __init__(self, name, age, hunger):
        self.__name = name
        self.__age = abs(age)
        self.__hunger = abs(hunger % 10)

    def __str__(self):
        return f"Name: {self.name} - Age: {self.age} - Hunger: {self.hunger}"

    def feed(self):
        """Reduces the hunger of the animal to a minimum of 0"""
        if self.__hunger - 2 <= 0:
            self.__hunger = 0
        else:
            self.__hunger -= 2

    def pass_day(self):
        """Increase the hunger of the animal by random number from 1-5
        to a maximum of 10"""
        hunger_to_add = random.randint(1, 5)
        if (self.__hunger + hunger_to_add) >= 10:
            self.__hunger = 10
        else:
            self.__hunger += hunger_to_add

    def die(self):
        return True if self.__hunger >= 10 else False

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def hunger(self):
        return self.__hunger

class MilkProducer():
    """Parent class that gives children a milk producing function"""
    def produce(self):
        return "milk"

class EggProducer():
    """Parent class that gives children an eggs producing function"""
    def produce(self):
        return "eggs"

class Cow(Animal, MilkProducer):
    def __init__(self, name, age, hunger = random.randint(1, 5)):
        super().__init__(name, age, hunger)

    def __str__(self):
        return super().__str__() + " - Animal: Cow"

    def moo(self):
        print(f"{self.name} says moo")

class Chicken(Animal, EggProducer):
    def __init__(self, name, age, hunger = random.randint(1, 5)):
        super().__init__(name, age, hunger)

    def __str__(self):
        return super().__str__() + " - Animal: Chicken"

    def cluck(self):
        print(f"{self.name} says cluck")

class Pig(Animal):
    def __init__(self, name, age, hunger = random.randint(1, 5)):
        super().__init__(name, age, hunger)

    def __str__(self):
        return super().__str__() + " - Animal: Pig"

    def oink(self):
        print(f"{self.name} says oink")

class Sheep(Animal, MilkProducer):
    def __init__(self, name, age, hunger = random.randint(1, 5)):
        super().__init__(name, age, hunger)

    def __str__(self):
        return super().__str__() + " - Animal: Sheep"

    def baa(self):
        print(f"{self.name} says baa")

class Farm():
    """Farm Class to contain animals and provide methods
    to change all animals within farm"""
    def __init__(self, name, animals = None):
        print(animals)
        self.__name = name
        self.__animals = [] if animals is None else animals
    def __str__(self):
        farm_list = f"{self.__name}'s Animals:\n"
        for animal in self.__animals:
            farm_list += (str(animal) + '\n')
        return farm_list

    @property
    def name(self):
        return self.__name

    def add_animal(self, animal):
        """Adds a new animal object to the animals list of the class"""
        print("We have a new family member!")
        self.__animals.append(animal)

    def feed_all(self):
        """Uses the feed() method for all animals in the farm"""
        print("I wonder what's for dinner...")
        for animal in self.__animals:
            animal.feed()

    def next_day(self):
        """Uses the pass_day() method for all animals in the farm"""
        print("Tomorrow is another day...")
        for animal in self.__animals.copy():
            animal.pass_day()
            '''
            if animal.die():
                print(f"{animal.name} forget where the trough was...")
                self.__animals.remove(animal)
            ''' 
    def produce(self, produce_type):
        """Generator that yields the animal's produce only if
        it is of the specified producer type"""
        print("The free market beckons!")
        for animal in self.__animals:
            if isinstance(animal, produce_type):
                yield f"{animal.name}'s {animal.produce()}"

    def animals_of_type(self, animal_type):
        """Generator that yields an animal only if it is of the 
        specified type"""
        print("Looking for something?")
        for animal in self.__animals:
            if isinstance(animal, animal_type):
                yield animal
