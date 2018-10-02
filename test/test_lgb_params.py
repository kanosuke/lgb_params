import os
os.getcwd()
os.chdir("..")

import lgb_params

dir(lgb_params)
lgb_params.__path__

lgb_params.get_simple_space()
lgb_params.get_standard_space()
