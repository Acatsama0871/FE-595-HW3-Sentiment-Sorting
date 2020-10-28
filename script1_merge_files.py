# script1_merge_files.py
# merge the data

# modules
from HW3_functions import merge_data

def main():
    # merge various data
    df = merge_data(save=True)  # save the merged data to a .csv file

    # print the head and tail to confirm result
    print('\nHead of the merged data:')
    print(df.head())
    print('\n\nTail of the merged data:')
    print(df.tail())

    return


if __name__ == '__main__':
    main()
