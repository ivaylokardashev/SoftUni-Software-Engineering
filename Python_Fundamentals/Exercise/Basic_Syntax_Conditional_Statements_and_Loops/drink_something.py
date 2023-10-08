# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif age <= 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")
'''Ако нещо се повтаря повече от един път помисли дали има как да го подобриш'''
age = int(input())
drinks = ""
if age <= 14:
    drinks = "toddy"
elif age <= 18:
    drinks = "coke"
elif age <= 21:
    drinks = "beer"
else:
    drinks = "whisky"
print(f"drink {drinks}")