# 5. Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
#     *Пример:*
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

point_x1 = float(input('Enter the coordinate X of the first point : '))
point_y1 = float(input('Enter the coordinate Y of the first point : '))

point_x2 = float(input('Enter the coordinate X of the second point : '))
point_y2 = float(input('Enter the coordinate Y of the second point : '))


A = (point_x2-point_x1)
B = (point_y2-point_y1)
length_of_points = ((point_x2-point_x1)**2+(point_y2-point_y1)**2)**(0.5)
length_of_points = round(length_of_points,3)
print(f'-> {length_of_points} - distance between two points ')

# length_of_points = (lambda x,y:(x+y)**(0.5), map(lambda points:(points[1]-points[0])**2))
# print(f'-> {length_of_points} - distance between two points ')
length_of_points = ( lambda x, y: ( x + y ) ** ( 0.5 ),( lambda points: ( points[ A ] - points[ B] ) ** 2 ))
print(f'-> {length_of_points} - distance between two points ')