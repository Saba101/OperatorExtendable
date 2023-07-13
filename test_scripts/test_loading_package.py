import pickle
from directoryPaths import test_script_folder
from Operators import load_extended_package as loadext




##Import function you want to use
from functions import *

## Then use load function to load entire package
op = loadext._load(test_script_folder)
op.select_operation('increment')
print(op.apply_operation((12,)))

# op.select_operation('not_equals')
# print(op.apply_operation((12, 13)))