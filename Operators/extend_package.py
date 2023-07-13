import Operators
import pickle


def _extend(func_name, _func, path_to_save_extended_version):
    op = Operators.Operator()
    op._add_new_operation(f"{func_name}", _func)
    #
    # # Save the modified Operators instance to a file
    with open(path_to_save_extended_version + '\\' + 'extended.pickle', 'wb') as file:
        pickle.dump(op, file)

    # Load the modified Operators instance from the file
    with open(path_to_save_extended_version + '\\' + 'extended.pickle', 'rb') as file:
        op = pickle.load(file)

    return ("Saved to path: "+ path_to_save_extended_version + '\\' + 'extended.pickle')