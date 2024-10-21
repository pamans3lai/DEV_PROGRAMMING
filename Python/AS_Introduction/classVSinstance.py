class Pet:
    kind = 'mammal'
    n_pets = 0
    pet_names = []

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

tom = Pet('cat', 'Tom')
avocado = Pet('dog', 'Avocado')
ben = Pet('goldfish', 'Benjamin')

Pet.n_pets += 3
print(Pet.n_pets)
