from pokemon import Pokemon
from trainer import Trainer


first_pokemon = Pokemon("Chalizar", 500)
second_pokemon = Pokemon("Zecrom", 1500)
third_pokemon = Pokemon("Reshiram", 1500)

first_trainer = Trainer("Ivaylo")

print(first_trainer.add_pokemon(first_pokemon))
print(first_trainer.add_pokemon(second_pokemon))
print(first_trainer.add_pokemon(third_pokemon))

print(first_trainer.release_pokemon("Chalizar"))

print(first_trainer.trainer_data())

