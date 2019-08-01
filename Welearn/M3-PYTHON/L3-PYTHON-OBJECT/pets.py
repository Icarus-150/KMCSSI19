class Pet(object):
    def __init__(self, name, age,species):
     self.name = name
     self.age = age
     self.species = species
     self.is_moving = False
     self.mood = "happy"
     
    def move(self):
        print("> %s is moving..." % self.name)
        if self.moving:
            self.moving = False
        else:
            print("> is still" % self.name)
            self.mood = "lethargic"

my_pet = Pet("Fido",3, "dog")

my_pet.moving = True  # manually set to True
print("Is my pet moving? %s" % my_pet.moving)
my_pet.move()  # calls the move method defined above
print("How about now? %s" % my_pet.moving)
print("My pet is feeling %s" % my_pet.mood)
