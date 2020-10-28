# script2_find.py
# find the best and worst idea based on sentiment analysis

# modules
import pandas as pd
from HW3_functions import find_Ideas

def main():
    # load the data
    df = pd.read_csv('merged_data.csv', index_col=0)

    # find ideas
    the_best, the_worst = find_Ideas(df)
    print('The best idea is [', the_best[1], ']')
    print('The polarity of the idea is', the_best[0])
    print()
    print('The worst idea is [', the_worst[1], ']')
    print('The polarity of the idea is', the_worst[0])

    return


if __name__ == '__main__':
    main()
