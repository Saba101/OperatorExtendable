# #### Test Cases for class Operators
# import Operators
# op = Operators.Operator()
#
# from functions import increment_, decrement_
# op._add_new_operation("increment", increment_)
# op._add_new_operation("decrement", decrement_)
# #
# # # Save the modified Operators instance to a file
# import pickle
# from directoryPaths import test_script_folder
# with open(test_script_folder + '\\' + 'extended.pickle', 'wb') as file:
#     pickle.dump(op, file)
#
# # Load the modified Operators instance from the file
# with open(test_script_folder + '\\' +'extended.pickle', 'rb') as file:
#     op = pickle.load(file)


# str_a = "ABC"
# str_b = "BB A"
#
# int_a = 12
# int_b = 4
#
# list_L = [3, 'AB' ,5, 12, 'ABC', 'BBA']
# tuple_T = (3,4)
#
# empty_var1 = None
# empty_var2 = ""
#
#
# op.select_operation("equals")
# print(op.apply_operation(str_a, str_b))
# print(op.apply_operation(int_a, int_b))
#
# op.select_operation("in")
# print(op.apply_operation(str_b, list_L))
#
# op.select_operation("between")
# print(op.apply_operation(int_a, tuple_T))
#
# op.select_operation("is_empty")
# print(op.apply_operation(int_a))
# print(op.apply_operation(str_a))
# print(op.apply_operation(empty_var2))
#
# op.select_operation("not_empty")
# print(op.apply_operation(int_a))
# print(op.apply_operation(str_a))
# print(op.apply_operation(empty_var2))
#
# op.select_operation("contains")
# print(op.apply_operation(str_a, 'B'))
# print(op.apply_operation(str_a, 'P'))
# # print(op.apply_operation(int_a, 'P'))
#
# op.select_operation("starts_with")
# print(op.apply_operation(str_a, 'B'))
# print(op.apply_operation(str_a, 'A'))
#
# op.select_operation("ends_with")
# print(op.apply_operation(str_a, 'B'))
# print(op.apply_operation(str_a, 'C'))

# # Load the modified Operators instance from the file
# with open('Operators.pickle', 'rb') as file:
#     op = pickle.load(file)
from functions import *
from Operators import extend_package as ext
from directoryPaths import test_script_folder


ext._extend("increment", increment_, test_script_folder)
