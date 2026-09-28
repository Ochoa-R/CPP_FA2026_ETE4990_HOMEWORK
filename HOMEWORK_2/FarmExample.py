from FarmAnimals import Animal
from FarmAnimals import MilkProducer
from FarmAnimals import EggProducer
from FarmAnimals import Cow
from FarmAnimals import Chicken
from FarmAnimals import Pig
from FarmAnimals import Sheep
from FarmAnimals import Farm

bingus = Farm("Bingus")
animal_list = [
    Cow("Nessa", 7, 3),
    Cow("BooBoo", 5, 7),
    Chicken("Clara", 2, 4),
    Pig("Hog", 10, 8),
    Chicken("Loco", 8, 9),
    Pig("Greaser", 1, 7),
    Cow("Dancer",13, 4),
    Sheep("Dolly", 2, 4)
]

for animal in animal_list:
    bingus.add_animal(animal)
print(bingus)

for i in range(1, 10):
    bingus.next_day()
print(bingus)

for i in range(1, 10):
    bingus.feed_all()
print(bingus)

for chicken in bingus.animals_of_type(Chicken):
    print(chicken.name)

for milkers in bingus.produce(MilkProducer):
    print(milkers)

for layers in bingus.produce(EggProducer):
    print(layers)
