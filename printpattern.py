# a.i
number = []
for i in range(20):
    number.append(i)

print(*number)

print("-"*30)
print("-"*30)
# a.ii
n = int(input("your number ? "))
number = []
for i in range(n):
    number.append(i)

print(*number)

print("-"*30)
print("-"*30)

# b.i
number = []
x = 1
for _ in range(6):
    number.append(x)
    x -= 1
    number.append(x)
    x += 1
print(*number)

print("-"*30)
print("-"*30)
# b.ii

num = int(input("Enter your number of 1's 0's ? "))
x = 1
number = []


for _ in range((num//2)+1):
    number.append(x)
    x -= 1
    number.append(x)
    x += 1
if num % 2 != 0:
    number.pop()

print(*number)
