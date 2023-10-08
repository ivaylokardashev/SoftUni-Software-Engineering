orders = int(input())
total_price = 0
price_for_coffee = 0
for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000):
        continue
    price_for_coffee = price_per_capsule * days * capsules_per_day
    total_price += price_for_coffee
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")
print(f"Total: ${total_price:.2f}")

#test format
# a = 1.111111111
# b = 0.9
# '''Мястото пред : е за placeholder или индекс според аргумента във format() т.е. в този случай "0 е за a", a "1 е за b"'''
# '''Ако не поставим нищо пред : то си взима аргументите от format() под ред и си ги форматира'''
# s = '({:.2f}, {:.2f})'.format(a, b)
# print(s)