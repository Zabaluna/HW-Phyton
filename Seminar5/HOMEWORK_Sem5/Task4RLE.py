# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# С помощью алгоритма сжатия данных кодирования длин серий (RLE),
#  примененного к приведенной выше гипотетической строке сканирования,
#  ее можно представить как 12W1B12W3B24W1B14W

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compress_text(my_text):
    count = 1
    result_compress_text = ''


    for i in range(len(my_text) - 1):
        if my_text[i] == my_text[i + 1]:
            count +=1
        else:
            result_compress_text += str(count) + my_text[i]
            count = 1
            
    result_compress_text += str(count) + my_text[len(my_text) - 1]
    return result_compress_text

def unpacking_text(result_compress_text):
    result_unpucking_text = ''
    temp = ''
    for i in result_compress_text:
        for element in i:
            if element.isdigit():
                temp += element
            else:
                result_unpucking_text += element * int(temp)
                temp = ''
        result_unpucking_text += '\n'
    return result_unpucking_text

def main():
    # записываем наш текст, который будем использовать для сжатия
    my_text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    comp_data = open("D:\GB\PYTHON\Seminar5\HOMEWORK_Sem5\\my_text", "a", encoding='UTF-8')
    comp_data.writelines(my_text)
    comp_data.close
    # with open("D:\GB\PYTHON\Seminar5\HOMEWORK_Sem5\\my_text", "w") as filek:
    #         filek.write(my_text)

    data = open("D:\GB\PYTHON\Seminar5\HOMEWORK_Sem5\\my_text", "r", encoding='UTF-8')
    result_compress_text = data.readlines()
    data.close()

    compress_text(my_text)
    unpacking_text(result_compress_text)

    unpack_data = open("D:\GB\PYTHON\Seminar5\HOMEWORK_Sem5\\my_text", "w", encoding='UTF-8')
    for el in compress_text:
        unpack_data.writelines(el)
    unpack_data.close()



if __name__ == "__main__":
    main()    
