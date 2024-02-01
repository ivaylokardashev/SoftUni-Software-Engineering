# stack = input().split()
#
# while len(stack) > 0:
#     print(stack.pop(), end=' ')

a = [
    [1,2,3,7,8,9,4,5,],
    [4,5,6,7,8,9,1,2,],
    [1,2,3,7,8,9,4,5,],
    [1,2,3,7,8,9,4,5,],
]

sum = 0

for row_index in range(3):
    sum += a[-row_index][-row_index]

print(sum)