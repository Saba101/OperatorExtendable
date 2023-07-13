import operator
import re


def between_(a:int, _tuple):
    return _tuple[0] <= a <= _tuple[1]


def in_(a, _list):
    return a in _list


def empty_(a):
    if type(a) is str:
        return len(a) == 0 or a is None
    elif type(a) is int or type(a) is float:
        return a is None




def not_empty_(a):
    if type(a) is str:
        return len(a) > 0 and a is not None
    elif type(a) is int or type(a) is float:
        return a is not None


def contains_(a:str, value):
    if re.search(f"{value}", a):
        return True
    else:
        return False


def starts_with_(a:str, value):
    if re.search(f"^{value}", a):
        return True
    else:
        return False


def ends_with_(a:str, value):
    if re.search(f"{value}$", a):
        return True
    else:
        return False


# def lookup_(value, param_):
#     actions = {
#         'exists': Operators.eq,
#         'not_exists': Operators.ne,
#     }
#
#     _keys_list = param_[0]
#     _action = actions.get(param_[1])
#
#     db_connection = mariadb.connect(user=db_user, password=db_pass, database=db_name, host=db_hostname, port=db_port)
#     cursor = db_connection.cursor()
#     #     attribute_id = param_[0]
#     #     cursor.execute(f"SELECT `lookup_key` FROM `{db_name}`.`lookup` WHERE `product_attribute_id` = {attribute_id};")
#
#     result = False
#     for key_id in _keys_list:
#         cursor.execute(f"SELECT `lookup_key` FROM `{db_name}`.`lookup` WHERE `id` = {key_id};")
#         key = cursor.fetchone();
#         if key != None:
#             key = key[0]
#             # print(f"obtained key:{key} || provided value:{value}")
#             result = result or _action(str(value), str(key))
#         else:
#             print(f"No record found against key id:{key_id}")
#     return result