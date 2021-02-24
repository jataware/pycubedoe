# pycubedoe

pycubedoe generates a design of experiments (DOE) by constructing a Nearly Orthogonal Latin Hypercube (NOLH) with user-defined factors and appropriate factor levels. The underling space-filling matrices are provided by the NOLHDesigns_v6.xls spreadsheet: Generating nearly orthogonal Latin Hypercube designs. More information on the NOLHDesigns can be found at: https://nps.edu/web/seed/software-downloads.

Each row of the DOE is a design point that is a point value inclusive to the user-assigned parameter ranges. In turn, instantiating a model run over each design point constitutes a metamodel. This approach allows for the simple and quick exploration of the effects of varying parameter values on your model of choice through analysis of the metamodel results.

A note on design points:

The number of design points is dictated by the number of factors chosen. Below is table detailing the number of design points that will be generated for your DOE:


| Number of Factors           | Number of Design Points (rows)  |
| --------------------------- | ------------------------------- |
|        [1, 7]               |          17                     |
|        [8, 11]              |          33                     |
|        [12, 16]             |          56                     |
|        [17, 22]             |          129                    |
|        [23, 29]             |          257                    |
|        [30, inf]            | None, too many factors!         |

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

     where `a` is the factor label and the list is: 
     
     `[<min factor value = 1>, <max factor value = 5>, <number of significant digits = 2>]`


   - **Categorical Factors Only Dictionary**:

     `categorical = {"flag": ["red", "white", "blue"],...}`

      where `flag` is the factor label and the list is: 
    
     `["a", list", "of", "all", categorical", "levels"]`


   - **Both Numeric and Categorical Factors, as seen above**:

     `numeric = {"a":[1,5,2],...}`

     `categorical = {"flag": ["red", "white", "blue"],...}`


4. Build the Design of Experiments (DOE):

   - Default: `pc.pycubeDOE(numeric = None, categorical = None)`
   
   - Assign your pre-built factor-type dictionaries:
   
      `DOE = pc.pycubeDOE(numeric = numeric, categorical = categorical)`

   - `pc.pycubeDOE()` returns a dataframe with user-defined factors and factor-values for user-defined ranges.

     - Each column is a user-defined factor; either numeric or categorical.
     - Each row is a design point.
     - In aggregate, all design points form a Nearly-Orthogonal Latin Hypercube that efficiently explores the parameter space while reducing the computational load.

     **NOTE**: for factor-types *not* used, you must assign it a value of `None`. 
   
       For example: `DOE = pc.pycubeDOE(numeric = None, categorical = categorical)`   

5. There is a helper function `pc.designPoints(DOE)` that iterates over each design point (row) of your DOE dataframe. First you will need to assign each design point value to a factor name. Below is an example using `exampleRun` as the model:


```
def exampleRun(designPT):
    #Assign your variable values from the DOE design point
    a = designPT[0]
    flag = designPT[1]
    ### DO SOMETHING WITH YOUR DESIGN POINT, for example:
    if flag == "red" and a <= 2.5:
        return round(a*a,2)
    else:
        return "Fly Navy"
```

  Then run the design points over `exampleRun` where we call pycubedoe's `pc.designPoints` function:

```
modelResults = []
for designPT in pc.designPoints(DOE):
    sim = exampleRun(designPT)
    modelResults.append(sim)
print(modelResults) 
```

## Acknowledgments

The full designs for up to 22 factors are from Tom Cioppa's 2002 PhD dissertation (2002).  For ease of application, we use a slightly different column order for designs with fewer factors.  The 29-factor design was provided by Andy Hernandez.  For more details about the properties or application of these designs, see 

  Cioppa, T. M. and T. W. Lucas.  2007.  Efficient nearly orthogonal and space-filling Latin hypercubes.
  Technometrics 49(1):  45-55.

  Kleijnen, J. P. C., S. M. Sanchez, T. W. Lucas, and T. M. Cioppa.  A user's guide to the brave new world of
  designing simulation experiments.  INFORMS Journal on Computing 17(3): 263-289.

For more information:
Links to handouts, papers, presentations, and examples that you may find useful will be maintained at http://harvest.nps.edu, along with future updates of this worksheet.  You can also contact the author at ssanchez@nps.edu developed by Susan M. Sanchez, January 2004. Version 6: March 2015.

## License:

GNU Lesser General Public License v3 or later (LGPLv3+)

Copyright (c)  2021  Travis Hartman

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".
