class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, spices, name):
        if spices == 'mammal':
            self.mammals.append(name)
        elif spices == "fish":
            self.fishes.append(name)
        elif spices == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, spices):
        result = ""

        if spices == 'mammal':
            result += f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\n"
        elif spices == "fish":
            result += f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\n"
        elif spices == "bird":
            result += f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


name = input()
animals = int(input())
zoo = Zoo(name)

for current_animal in range(animals):
    command = input().split()
    species, animal = command[0], command[1]
    zoo.add_animal(species, animal)

species = input()
print(zoo.get_info(species))
