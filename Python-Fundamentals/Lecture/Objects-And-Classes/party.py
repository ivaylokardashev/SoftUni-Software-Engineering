class Party:
    def __init__(self):
        self.people = []


party = Party()
command = input()
# Да проверя '>' в дебуга до парти дали ми изкарва всички атрибути в обекта и как те се променят
while command != "End":
    party.people.append(command)
    command = input()

# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")
