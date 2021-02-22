========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - | |version| |wheel| |supported-versions|
        | |commits-since|

.. |travis| image:: https://github/jataware/pycubedoe.svg?branch=main
    :alt: Travis-CI Build Status
    :target: https://github/jataware/pycubedoe

.. |version| image:: https://img.shields.io/pypi/v/pycubedoe.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pycubedoe

.. |wheel| image:: https://img.shields.io/pypi/wheel/pycubedoe.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pycubedoe

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycubedoe.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pycubedoe

.. |commits-since| image:: https://img.shields.io/github/commits-since/jataware/pycubedoe/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/jataware/pycubedoe/compare/v0.0.1...main



.. end-badges

Generates design of experiments by constructing a nearly orthogonal latin hypercube with user-defined factors and appropriate factor levels.

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Overview
========

`pycubedoe` generates a design of experiments (DOE) by constructing a nearly orthogonal latin hypercube with user-defined factors and appropriate factor levels. The underling space-filling matrices are provided by the "Generating nearly orthogonal Latin Hypercube designs" spreadsheet NOLHDesigns_v6.xls. More information on the NOLHDesigns can be found at: https://nps.edu/web/seed/software-downloads.

Background
==========




Installation
============

.. code-block:: python

    pip3 install pycubedoe

You can also install the in-development version with::

    pip3 install https://github.com/jataware/pycubedoe/archive/main.zip


Quick Start
=============


To use the project:


1. import the package:

  .. code-block:: python

    import pycubedoe as pc

2. Create a dictionary of your desired factors and their associated levels. pycubedoe can support both numeric and categorical factors. For each factor-type, build a dictionary of all your factors under the appropriate dictionary key as shown below::

   For numeric factors: "factor name": [min Value, max Value, number of desired decimal places]
   
    For example: If you are interested in exploring the effects of various temperatures from 10 to 15 degrees Celsius on your model, and wish to have two decimals (two significant digits) then your temperature key/value would be: `"temperature":[10,15,2]`
   
   For categorical factors: "factor name": ["list", "of", "categorical", "factor", "levels"]
   
    For example: If you are interested in exploring the effects of various levels of ice accumulation on your model that are categorized as "lo", "medium", and "high", then your "ice" factor key/value would be: `"ice:["low", "medium", "high"]`

   **Numeric Factors Only**:

    .. code-block:: python

    nums = {"rainfall":[1,5,2],"temperature":[10,15,2]}
    
    cats = None

   **Categorical Factors Only**:

    .. code-block:: python

    nums = None
    
    cats = {"flag": ["red", "white", "blue"],"ice:["low", "medium", "high"]}

   **Both Numeric and Categorical Factors**:

    .. code-block:: python

    nums = {"rainfall":[1,5,2],"temperature":[10,15,2]}
    
    cats = {"flag": ["red", "white", "blue"],"ice:["low", "medium", "high"]}

  **Note: Assigning *None* to a factor-type not utilized is required.**

3. Build the Design of Experiments (DOE)

  .. code-block:: python

    DOE = pc.pycubeDOE(numeric=nums, categorical=cats)

4. There is a helper function 'pc.designPoints(DOE)' that iterates over each row of your DOE. First you will need to assign each design point value to a factor name. Below is an example using `Example_Function` as a generic model:

.. code-block:: python

  def Example_Function(designPT):
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
      if ice == "hi" and temp <= 17.0:
          return round(a*b*c,2)
      else:
          return 0


Then run the design points over `Eaxmple_Function` where we call pycubedoe's designPoints function:

.. code-block:: python

    modelResults = []
    for designPT in designPoints(DOE):
        tempResult = Example_Function(designPT)
        modelResults.append(tempResult)
    print(modelResults) 

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
