divisor = int(input())
boundary = int(input())
'''До divisor - 1 е защото всички числа, които са по-малки от делитела няма смисъл да се проверяват тъй като
немогат да се разделят с точност'''
for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number) # Няма проблем да се запише принта извън цикъла тъй като по условие е гарантирано, че ще се намери поне едно число
