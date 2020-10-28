# script3_most_common.py
# find the 10 most common words in company descriptions

# module
import pandas as pd
from tabulate import tabulate
from HW3_functions import find_most_common

def main():
    # load the data
    df = pd.read_csv('merged_data.csv', index_col=0)

    # find most common
    # find the ten most common tokens
    # the stop words and punctuations are exclude and the token
    # the token is lemmatized to base form
    the_ten = find_most_common(df, process=True)
    # output result
    print('The 10 most common words and corresponding frequencies are:')
    print(tabulate(the_ten, headers=['Token', 'Frequency']))

    return


if __name__ == '__main__':
    main()