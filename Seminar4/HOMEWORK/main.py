from Task4HW import create_dictionary
from Task4HW import polynomial
from Task5HW import backdictinary
from Task5HW import addition


# equation = create_equation()
# print(equation)
# new_equation =decode(equation)
# print(new_equation)

if __name__ == "__main__":
    my_dict1 = create_dictionary()
    my_dict2 = create_dictionary()
    print(polynomial(my_dict1))
    print(polynomial(my_dict2))
    print(polynomial(addition(my_dict1, my_dict2)))
 



    # my_dict = create_dictionary()
    # print(my_dict)

    # str_equation=polynomial(my_dict)
    # print(str_equation)

    # dict_equation = encode(str_equation)
    # print(dict_equation)