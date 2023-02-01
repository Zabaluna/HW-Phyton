from statistics import mode
import  model_sub as initial
import view
import initial

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    initial.init(value_a, value_b)
    result = initial.do_it()
    view.view_data(result, "resul")
