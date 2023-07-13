import pickle

def _load(path_to_saved_package_directory):
    # Load the modified Operators instance from the file
    with open(path_to_saved_package_directory + '\\' + 'extended.pickle', 'rb') as file:
        op = pickle.load(file)
    return op

##Whenever you use this function - you need to also import the function name from file where you created it.