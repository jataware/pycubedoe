# pycubedoe

## Description

pycubedoe generates a design of experiements (DOE) by constructing a nearly orthogonal latin hypercube with user-defined factors and appropriate factor levels. The underling space-filling matrices are provided by the NOLHDesigns_v6.xls: Generating nearly orthogonal Latin Hypercube designs. More information on the NOLHDesigns can be found at: https://nps.edu/web/seed/software-downloads.


## Quick Start

1. Install the pycubedoe package to your environment: 

  `pip3 install pycubedoe`

2. Import the package:

  `import pycubedoe as pc`

3. Create a dictionary of your desired factors and their associated levels. pycubedoe can support both numeric and categorical factor-types. For each factor-type, build a dictionary as described below:

  **In general**:

   - For numeric factors:     {"factor name": [min Value, max Value, number of desired decimal places],...}
   
   - For categorical factors: {"factor name": ["list", "of", "categorical", "levels"],...}

  **Example Parameter Dictionaries**:

  - **Numeric Factors Only Dictionary**:

    `numeric = {"a":[1,5,2],...}`

     where `a` is the factor label and the list is: `[<min factor value = 1>, <max factor value = 5>, <number of significant digits = 2>]`


  - **Categorical Factors Only Dictionary**:

    `categorical = {"flag": ["red", "white", "blue"],...}`

    where `flag` is the factor label and the list is: ["a", list", "of", "all", categorical", "levels"]

  - **Both Numeric and Categorical Factors, as seen above**:

    `numeric = {"a":[1,5,2],...}`

    `categorical = {"flag": ["red", "white", "blue"],...}`


4. Build the Design of Experiments (DOE):

 - Default: `pc.pycubeDOE(numeric = None, categorical = None)`
   
 - Assign your pre-built factor-type dictionaries:
   
   `DOE = pc.pycubeDOE(numeric = numeric, categorical = categorical)`

 - This function returna a pandas dataframe with user-defined factors and factor-values within a user-defined range.

   - Each column is a user-defined factor; either numeric or categorical.
   - Each row is a design point.
   - In aggregate, all design points form a Nearly-Orthogonal Latin Hypercube that efficiently explores the parameter space while reducing the computational load.

   **NOTE**: for factor-types *not* used, you must assign it a value of `None`. 
   
      For example: `DOE = pc.pycubeDOE(numeric = None, categorical = categorical)`   

5. There is a helper function `pc.designPoints(DOE)` that iterates over each design point (row) of your DOE dataframe. First you will need to assign each design point value to a factor name. Below is an example using `exampleRun` as the model:

	    def exampleRun(designPT):
	      #Assign your variable values from the DOE design point
	      a = designPT[0]
	      flag = designPT[1]
	      
	      ### DO SOMETHING WITH YOUR DESIGN POINT, for example:
	      if flag == "red" and a <= 2.5:
	          return round(a*a,2)
	      else:
	          return 0


Then run the design points over `exampleRun` where we call pycubedoe's `pc.designPoints` function:
   
    modelResults = []
    for designPT in pc.designPoints(DOE):
        sim = exampleRun(designPT)
        modelResults.append(sim)
    print(modelResults) 

## License:

GNU Lesser General Public License v3 or later (LGPLv3+) 

## Development

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
