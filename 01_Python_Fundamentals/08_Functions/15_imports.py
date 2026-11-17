# 8-15. Imports: Using a program you wrote that has functions in it, 
#                store that functions in a separate file. Import the fun-
#                -ctions into your main program file, and call the funct-
#                -ions using each of these approaches:
# * import module_name 
# * from module_name import function_name
# * from module_name import function_name as fn 
# * import module_name as mn
# * from module_name import *

# import module_name.
import z_imports_demo

z_imports_demo.convert_to_lower("HELLO, WORLD!")
z_imports_demo.covert_to_upper("hello, world!")

# from module_name import function_name.
from z_imports_demo import convert_to_lower,covert_to_upper

convert_to_lower("HELLO,WORLD!")
covert_to_upper("hello, world!")

# from module_name import function_name as fn.
from z_imports_demo import ( 
    convert_to_lower as lowercase,
    covert_to_upper as uppercase )

lowercase("HELLO, WORLD!")
uppercase("hello, world!")

# import module_name as mn.
import z_imports_demo as case_converter

case_converter.convert_to_lower("HELLO, WORLD!")
case_converter.covert_to_upper("hello, world!")

# from module_name import *.
from z_imports_demo import *

convert_to_lower("HELLO, WORLD!")
covert_to_upper("hello, world!")