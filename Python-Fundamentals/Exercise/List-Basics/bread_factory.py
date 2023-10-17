INITIAL_ENERGY = 100
ENERGY_FOR_ORDER = 30
ENERGY_FOR_REST = 50


events = input().split('|')
total_energy = 100
total_coins = 100
closed_day = False

for event in events:
    event_items = event.split('-')
    event_or_ingredient = event_items[0]
    event_value = int(event_items[1])

    if event_or_ingredient == "rest":
        current_energy = total_energy
        total_energy += event_value

        if total_energy > INITIAL_ENERGY:
            total_energy = 100

        gained_energy = total_energy - current_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_or_ingredient == "order":
        if total_energy >= ENERGY_FOR_ORDER:
            total_coins += event_value
            total_energy -= ENERGY_FOR_ORDER

            print(f"You earned {event_value} coins.")

        else:
            total_energy += ENERGY_FOR_REST

            print("You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value

            print(f"You bought {event_or_ingredient}.")

        else:
            closed_day = True

            print(f"Closed! Cannot afford {event_or_ingredient}.")

            break

if not closed_day:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")



