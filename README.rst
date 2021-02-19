========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.com/jataware/pycubedoe.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/jataware/pycubedoe

.. |version| image:: https://img.shields.io/pypi/v/pycubedoe.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pycubedoe

.. |wheel| image:: https://img.shields.io/pypi/wheel/pycubedoe.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pycubedoe

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycubedoe.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pycubedoe

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pycubedoe.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pycubedoe

.. |commits-since| image:: https://img.shields.io/github/commits-since/jataware/pycubedoe/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/jataware/pycubedoe/compare/v0.0.1...main



.. end-badges

Generates design of experiements by constructing a nearly orthogonal latin hypercube with user-defined factors and
appropriate factor levels.

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Overview
========

`pycubedoe` generates a design of experiements (DOE) by constructing a nearly orthogonal latin hypercube with user-defined factors and
appropriate factor levels. The underling space-filling matrices are provided by the NOLHDesigns_v6.xls: Generating nearly orthogonal Latin Hypercube designs. More information on the NOLHDesigns can be found at: https://nps.edu/web/seed/software-downloads.

Installation
============

::

    pip3 install pycubedoe

You can also install the in-development version with::

    pip3 install https://github.com/jataware/pycubedoe/archive/main.zip


Documentation
=============


To use the project:


1. import the package:

.. code-block:: python
    
    import pycubedoe as pc

2. Create a dictionary of your desired factors and their associated levels. pycubedoe can support both numeric and categorical factors. For each factor, build a dictionary as described below:

   For numeric factors:     "factor name": [min Value, max Value, number of desired decimal places]
   For categorical factors: "factor name": ["list", "of", "categorical", "levels"]

For each factor-type, build a dictionary of all your factors under the appropriate dictionary key as shown below:

Numeric Factors Only:

.. code-block:: python

    params = {"numeric": {"a":[1,5,2],
                          "b":[5,10,1],
                          "c":[3,4,3]
                          }
             }

Categorical Factors Only:

.. code-block:: python

    params = {"categorical": {"color": ["red", "white", "blue"],
                              "temperature": ["super-cold", "balmy"], 
                              "ice":["lo", "med", "hi"]
                              }
             }

Both Numeric and Categorical Factors:

.. code-block:: python
    
    num = {"a":[1,5,2], "b":[5,10,1], "c":[3,4,3]}
    cat = {"color": ["red", "white", "blue"],
           "temp": ["super-cold", "balmy"], 
           "ice":["lo", "med", "hi"]
          }
    params =  {"numeric": num,
               "categorical": cat
               }

3. Build the Design of Experiments (DOE)

.. code-block:: python

    DOE = pc.pycubeDOE(params)

4. There is a helper function ['designPoints(DOE)'] that iterates over each row of your DOE. First you will need to assign each design point value to a factor name. Below is an example using `YOUR_MODEL` as a model:

.. code-block:: python

  def YOUR_MODEL(designPT):
      '''  
      Example on how to parse the design point from the DOE and implement some logic
      '''

      #Assign your variable values from the DOE design point
      a = designPT[0]
      b = designPT[1]
      c = designPT[2]
      color = designPT[3]
      temp = designPT[4]
      ice = designPT[5]
      
      ### DO SOMETHING WITH YOUR DESIGN POINT, for example:
      if ice == "hi" and temp == "super-cold":
          return round(a*b*c,2)
      else:
          return 0


Then run the design points over `YOUR_MODEL` where we call pycubedoe's `designPoints` function:

.. code-block:: python

    modelResults = []
    for designPT in pc.designPoints(DOE):
        sim = YOUR_MODEL(designPT)
        modelResults.append(sim)
    print(modelResults) 

