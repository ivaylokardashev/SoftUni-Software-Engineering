legendary_item = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_obtain = ""

while True:
    materials_and_quantity = input().split()
    materials = list(map(lambda x: x.lower(), materials_and_quantity[1::2]))
    quantities = list(map(lambda x: int(x), materials_and_quantity[::2]))

    # legendary_item.update({mater: quan for (mater, quan) in zip(material, quantity)})
    for material, quantity in zip(materials, quantities):
        if material not in legendary_item:
            legendary_item[f"{material}"] = 0
        legendary_item[f"{material}"] += quantity

        if legendary_item["shards"] >= 250:
            legendary_item["shards"] -= 250
            legendary_item_obtain = "Shadowmourne"
            break
        elif legendary_item["fragments"] >= 250:
            legendary_item["fragments"] -= 250
            legendary_item_obtain = "Valanyr"
            break
        elif legendary_item["motes"] >= 250:
            legendary_item["motes"] -= 250
            legendary_item_obtain = "Dragonwrath"
            break

    if legendary_item_obtain != "":
        break

print(f"{legendary_item_obtain} obtained!")
for (key, value) in legendary_item.items():
    print(f"{key}: {value}")
