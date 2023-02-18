# def my_sum(num_1, num_2):
#     return num_1 + num_2


# def my_dif(num_1, num_2):
#     return num_1 - num_2


# def my_mult(num_1, num_2):
#     return num_1 * num_2


# def my_div(num_1, num_2):
#     return num_1 / num_2


import view

def calcul():
    num_1, num_2, oper = view.get_value()
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)

def calcul2(num_1, num_2, oper):
    match oper:
        case '+': return(num_1 + num_2)
        case '-': return(num_1 - num_2)
        case '*': return(num_1 * num_2)
        case '/': return(num_1 / num_2)    