from my_module import find_min_max


list_num = input("Введите уже что-нибудь -> ").split()

print(*find_min_max(list_num))