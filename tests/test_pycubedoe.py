
from pycubedoe import *


def test_pycubeDOE():
    nums = {"a":[1,5,2],"b":[5,10,1], "c":[3,4,3]}
    cats =  {"color": ["red", "white", "blue"],"temp": ["super-cold", "balmy"]}

    DOE_both = pycubeDOE(numeric=nums, categorical=cats)
    DOE_num  = pycubeDOE(numeric=nums, categorical=None)
    DOE_cat  = pycubeDOE(numeric=None, categorical=cats)
    
    return DOE_both, DOE_num, DOE_cat