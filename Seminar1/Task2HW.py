# 2. Напишите программу для. проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ это not (не) 
# ⋁ - это OR (или)
# ⋀ - это AND (и)

# ¬X ⋀ ¬Y ⋀ ¬Z
# читается как не Х и не Y и не Z
# not

# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))

for x in [0,1]:
  for y in [0,1]:
    for z in [0,1]:
        print(not(x or y or z)) == (not (x) and not (y) and not(z))
        print(x,y,z)

# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#         print(not(x or y or z)) == (not (x) and not (y) and not(z))
#         print(x,y,z)
