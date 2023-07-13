from Operators.operations import *


class Operator:

    def __init__(self):
        self.__operation = None
        self.operations = {
            'not_equals': operator.ne,
            'equals': operator.eq,
            'is': operator.eq,
            'greater_than': operator.gt,
            'less_than': operator.lt,
            'greater_than_or_equal': operator.ge,
            'less_than_or_equal': operator.le,

            'between': between_,
            'in': in_,

            'is_empty': empty_,
            'not_empty': not_empty_,

            'contains': contains_,
            'starts_with': starts_with_,
            'ends_with': ends_with_
        }

    # def _add_new_operation(self, function_name, function_parameters, function_body):
    #     _func, params_info = create_new(function_name, function_parameters, function_body)
    #     self.operations[function_name] = _func
    #     self.list_all_operations()
    #     # return _func, params_info


    def list_all_operations(self):
        print(list(self.operations.keys()))

    def _add_new_operation(self, function_name, _func):
        self.operations[function_name] = _func
        self.list_all_operations()


    def select_operation(self, condition):
        self.__operation = self.operations.get(str(condition).lower())
        # print(self.__operation)

    def apply_operation(self, _params: tuple):
        if len(_params) == 0:
            return "No parameters are provided. Cannot perform any operation!"

        import inspect
        req_params = dict(inspect.signature(self.__operation).parameters)
        # given_params = dict(inspect.signature(self.apply_operation).parameters)
        # print("Required:" , req_params, "\nGiven:", given_params)

        if len(req_params) == len(_params):
            return self.__operation(*_params)

        else:
            print("Error: One required argument missing!")
            return "Operation not performed!"

        # if b == None:
        #     if self.__operation == empty_ or self.__operation == not_empty_:
        #         return self.__operation(a)
        #
        #     else:
        #         print("Error: One required argument missing!")
        #         return "Operation not performed!"
        #
        # else:
        #     return self.__operation(a, b) if a != None and b != None else "Error.."

