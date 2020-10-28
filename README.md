# FE-595-HW3-Sentiment-Sorting
## How to run the code
### The required packages
To run the script, the following package are required:
1. [pandas](https://pandas.pydata.org)
2. [textblob](https://textblob.readthedocs.io/en/dev/)
3. [spacy](https://spacy.io)
4. [tabulate](https://pypi.org/project/tabulate/)
  
### The assumption about the data:
The script supports the .txt and .csv files. To run the script, the all text
data should be saved to a directory named **data_text**. The script has the
following assumption about the .csv and .txt file:
* .csv file:  
The dataframe should only contains three columns: **Index**, **Name** and
**Purpose**. The column names does not have to be exactly the same but the
order of columns should follows this structure.  

* .txt file:
The script assumes the data in the .txt file will have the following format:
```
Name: example name1---Purpose: example purpose1
Name: example name2---Purpose: example purpose2
```
The script may not be able to handle the other format in .txt.

### Run the scripts:
1. Run the **script1_merge_files.py**:
```
python script1_merge_files.py
```
The output of the first script is:
```
Head of the merged data:
                          Name                                            Purpose
0                  Eaton-Payne  Synergistic homogeneous moratorium for empower...
1                  Hayes Group  Front-line clear-thinking open architecture fo...
2  Compton, Zamora and Roberts  Open-source leadingedge solution for whiteboar...
3    Johnson, Dalton and Wells  Balanced neutral forecast for leverage extensi...
4                     Ward PLC  Future-proofed neutral approach for unleash se...


Tail of the merged data:
                          Name                                            Purpose
245   Banks, Sanchez and Smith   Function-based asymmetric installation for st...
246               Ali and Sons   Focused motivating Local Area Network for inc...
247                 Cooley Ltd   Profound reciprocal methodology for embrace b...
248               Kelly-Barnes   Re-engineered static workforce for enable int...
249                 Graham PLC   Quality-focused attitude-oriented Local Area ...

Process finished with exit code 0
```
and the script will save the merged file to **merged_data.csv** which is necessary for following scripts

2. Run the **script2_find.py**
```
python script2_find.py
```
The output of the second script is:
```
The best idea is [ Organic static instruction set for redefine distributed web services ]
The polarity of the idea is 0.5

The worst idea is [ Assimilated didactic parallelism for incubate bricks-and-clicks bandwidth ]
The polarity of the idea is -0.5

Process finished with exit code 0
```

3. Run the **script3_most_common.py**
```
python script3_most_common.py
```
The output of the third script is:
```
The 10 most common words and corresponding frequencies are:
Token            Frequency
-------------  -----------
e                       37
solution                21
enable                  17
orient                  16
info                    15
mediaries               15
system                  15
contextualize           14
time                    14
engineer                14

Process finished with exit code 0
```


### Usage of functions:
The functions are defined in the **HW3_functions.py**. To use a single function:
```
from HW3_function import *
```

#### Function to merge data:
The function is:
```
merge_data(save=False)
```
The function will merge all .csv and .txt file in **data_text** to a single
dataframe and the returned dataframe will have the structure:
```
                          Name                                            Purpose
0                  Eaton-Payne  Synergistic homogeneous moratorium for empower...
1                  Hayes Group  Front-line clear-thinking open architecture fo...
2  Compton, Zamora and Roberts  Open-source leadingedge solution for whiteboar...
3    Johnson, Dalton and Wells  Balanced neutral forecast for leverage extensi...
4                     Ward PLC  Future-proofed neutral approach for unleash se...
``` 
If **save** is set to true, the merged dataframe will be saved as
a single .csv file to the root directory.

#### Function to find the best and the worst idea:
The function is:
```
find_bestIdea(df)
```
The function will use the merged dataframe to find the best and worst
business idea based on sentiment analysis. The return of the function is
two tuples and will have following structure:
```
((highest_polarity, highest_polarity_corresponding_idea), 
(lowest_polarity, lowest_polarity_corresponding_idea))
```

#### Function to find the 10 most common token/words:
The function is:
```
find_most_common(df, process=True)
```
The function has two arguments:
+ df(pd.DataFrame): the text data, the structure should as same as the output
of the function *merge_data()*.
+ process(boolean): if the argument is set to *True*, the function will
remove the stop words and lemmatize the token to base form.

The function will return the 10 most common tokens and the corresponding
frequency.
