from Operators import Operator


op = Operator()

str_a = "ABC"
str_b = "BB A"

int_a = 12
int_b = 4

list_L = [3, 'AB' ,5, 12, 'ABC', 'BBA']
tuple_T = (3,4)

empty_var1 = None
empty_var2 = ""


op.select_operation("equals")
print(op.apply_operation((str_a, str_b)))
print(op.apply_operation((int_a, int_b)))

op.select_operation("in")
print(op.apply_operation((str_b, list_L)))

op.select_operation("between")
print(op.apply_operation((int_a, tuple_T)))

op.select_operation("is_empty")
print(op.apply_operation((int_a, )))
print(op.apply_operation((str_a, )))
print(op.apply_operation((empty_var2, )))

op.select_operation("not_empty")
print(op.apply_operation((int_a, )))
print(op.apply_operation((str_a, )))
print(op.apply_operation((empty_var2, )))

op.select_operation("contains")
print(op.apply_operation((str_a, 'B')))
print(op.apply_operation((str_a, 'P')))
# print(op.apply_operation(int_a, 'P'))

op.select_operation("starts_with")
print(op.apply_operation((str_a, 'B')))
print(op.apply_operation((str_a, 'A')))

op.select_operation("ends_with")
print(op.apply_operation((str_a, 'B')))
print(op.apply_operation((str_a, 'C')))