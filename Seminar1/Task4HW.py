# 4. Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

number_of_quarter = int(input('Print the number of quarter: '))

if number_of_quarter == 1:
    print('X range 0 to + infinity, Y range 0 to + infinity')
elif number_of_quarter == 2:
    print('X range 0 to - infinity, Y range 0 to + infinity')
elif number_of_quarter == 3:
    print('X range 0 to - infinity, Y range 0 to - infinity')
elif number_of_quarter == 4:
    print('X range 0 to + infinity, Y range 0 to - infinity')
else:
    print('You entered the wrong quarter number. Only 4 quarters')
