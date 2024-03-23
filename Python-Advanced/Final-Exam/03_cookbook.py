from pprint import pp
def cookbook(*args):
    recipts = dict()

    for index in range(len(args)):
        if not recipts.get(args[index][1]):
            recipts[args[index][1]] = {}
        if not recipts[args[index][1]].get(args[index][0]):
            recipts[args[index][1]][args[index][0]] = list()

        ingredients = ', '.join(args[index][2])
        recipts[args[index][1]][args[index][0]].append(ingredients)

    # shoud see x[0] if judge give me incorect output
    sorted_by_cuisine = sorted(recipts.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for cuisine, receipt in sorted_by_cuisine:
        result += f"{cuisine} cuisine contains {len(receipt)} recipes:\n"
        sorted_by_receipt_name = sorted(receipt.items(), key=lambda x: x[0])

        for receipt_name, ingredients in sorted_by_receipt_name:
            result += f"  * {receipt_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
