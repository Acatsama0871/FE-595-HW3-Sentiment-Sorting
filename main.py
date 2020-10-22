# main.py
# merge data, find best idea find most common tokens


# modules
from HW3_functions import *
from tabulate import tabulate


def main():

    # merge various data
    df = merge_data(save=True)  # save the merged data to a .csv file
    # print the head and tail to confirm result
    print('\nHead of the merged data:')
    print(df.head())
    print('\n\nTail of the merged data:')
    print(df.tail())
    print('\n' * 3)

    # find the best business idea
    the_best, the_worst = find_bestIdea(df)
    print('The best idea is [', the_best[1], ']')
    print('The polarity of the idea is', the_best[0])
    print()
    print('The worst idea is [', the_worst[1], ']')
    print('The polarity of the idea is', the_worst[0])
    print("\n" * 3)

    # find the ten most common tokens
    # the stop words and punctuations are exclude and the token
    # the token is lemmatized to base form
    the_ten = find_most_common(df, process=True)
    # output result
    print('The 10 most common words and corresponding frequency are:')
    print(tabulate(the_ten, headers=['Token', 'Frequency']))

    return


if __name__ == '__main__':
    main()
