
from pycubedoe import *


def test_pycubeDOE():
    params =  {"numeric": {"a":[1,5,2],
                           "b":[5,10,1],
                           "c":[3,4,3]
                          },
               "categorical": {"color": ["red", "white", "blue"],
                               "temp": ["super-cold", "balmy"], 
                               "ice":["lo", "med", "hi"]
                              }
              }
    DOE = pycubeDOE(params)
    
    return DOE