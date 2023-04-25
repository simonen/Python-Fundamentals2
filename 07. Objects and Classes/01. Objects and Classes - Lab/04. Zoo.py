class Zoo:
    __animals = 0

    def __init__(self, zooname):
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.zooname = zooname

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        names = ''
        if species == 'mammal':
            names = self.mammals
            species = 'Mammals'
        elif species == 'fish':
            names = self.fishes
            species = 'Fishes'
        elif species == 'bird':
            names = self.birds
            species = 'Birds'

        return f"{species} in {self.zooname}: {', '.join(names)}\n" \
               f"Total animals: {Zoo.__animals}"


zname = input()
numbers = int(input())
zoo = Zoo(zname)
for n in range(numbers):
    line = input().split()
    specie, name = line[0], line[1]
    zoo.add_animal(specie, name)

print(zoo.get_info(input()))
