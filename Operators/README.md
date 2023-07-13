## Extendable Operator Module

Package Description: A Python package for creating operations as per need of operations.


Install package:
Copy code: #private repository
_pip install git+https://github.com/Saba101/OperatorExtendable.git

Usage:
1. To use Operator class - 
create instance of Operator() class
```
from Operators import Operator
op = Operator()
op.select_operation("<condition>")
print(op.apply_operation(<tuple_object_of_values>))
```
Please check test_scripts > test_extending_package for more details.

2. To extend the already available module. Use _extend_package_
For this create the functions you want to add to another file - such that 'functions' in test_scripts.\
Then write script to extend the exitinf Operator module 
```
from functions import *
from Operators import extend_package as ext
ext._extend("<function-name>", <function>, <test_script_folder_path>)
```
This will save the extended operator class as _.pickle_ file inside your working folder. \

3. To load the extended package created - use load_extended_package function
**Please Note:** We can use functionality of previously made Operator class as well by loading this.
 ```
from Operators import load_extended_package as loadext

##You have to import functions from function file to use this package
from functions import *

## Then use load function to load entire package
op = loadext._load(test_script_folder)
op.select_operation('<function_name')
print(op.apply_operation(<tuple>))
```



Please check "test_scripts" folder to learn about usage in more detail.
