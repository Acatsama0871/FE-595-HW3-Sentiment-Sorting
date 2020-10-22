# HW3_functions.py
# merge data function, find best idea function, find most common tokens


# modules
import os
import re
import string
from collections import Counter
import pandas as pd
import spacy
from textblob import TextBlob


# merge data function
def merge_data(save=False):
    # get cwd and file names
    cwd = os.getcwd()
    data_path = os.path.join(cwd, 'data_text')
    file_names = os.listdir(data_path)


    # load data
    file_list = []
    col_names = ['Name', 'Purpose']
    for cur_file_name in file_names:
        suffix = cur_file_name.split('.')[1]

        # if the file is a csv
        if suffix == 'csv':
            cur_file = pd.read_csv(os.path.join(data_path, cur_file_name))
            if cur_file.shape[1] > 2:  # if it contains a index column, drop it
                cur_file = cur_file.iloc[:, [1, 2]]
            cur_file.columns = col_names
            file_list.append(cur_file)
        # if the file is a txt
        elif suffix == 'txt':
            # load file
            cur_file = pd.read_csv(os.path.join(data_path, cur_file_name), sep='\n', header=None)
            # convert to dataframe format
            company_names = []
            company_purpose = []
            for i in range(cur_file.shape[0]):
                cur_text = cur_file.iloc[i, 0]
                cur_name, cur_purpose = cur_text.split('---', 1)  # split by '---'
                cur_name = re.sub(pattern=r'Name: ', repl='', string=cur_name)  # remove 'Name: ' prefix
                cur_purpose = re.sub(pattern=r'Purpose: ', repl='', string=cur_purpose)  # remove 'Purpose: ' prefix
                company_names.append(cur_name)
                company_purpose.append(cur_purpose)
            # build new pandas dataframe
            cur_file = pd.DataFrame({'Name': company_names, 'Purpose': company_purpose})
            file_list.append(cur_file)

    # concatenate dataframes
    result = pd.DataFrame({'Name': [], 'Purpose': []})
    for cur_df in file_list:
        result = result.append(cur_df)
    result.reset_index(drop=True, inplace=True)

    # if need save the data
    if save:
        result.to_csv('merged_data.csv')
        return result
    else:
        return result


# find best idea function
def find_bestIdea(df):
    # initialize
    data_length = df.shape[0]
    highest_polarity = -2 # default value
    highest_index = -1  # default value
    lowest_polarity = 2 # default value
    lowest_index = -1 # default value

    # iterate to find the best idea and worst idea
    for i in range(data_length):
        cur_purpose = df.iloc[i, 1]
        cur_polarity = TextBlob(cur_purpose).sentiment.polarity

        if cur_polarity > highest_polarity:
            highest_polarity = cur_polarity
            highest_index = i
        elif cur_polarity < lowest_polarity:
            lowest_polarity = cur_polarity
            lowest_index = i

    # return result
    return (highest_polarity, df.iloc[highest_index, 1]), (lowest_polarity, df.iloc[lowest_index, 1])


# find most common tokens
def find_most_common(df, process=True):
    # initialize
    df_copy = df.copy()
    length = df_copy.shape[0]
    punctuations = string.punctuation
    nlp = spacy.load('en_core_web_lg', disable=['parser', 'tagger', 'ner'])

    # append text to a single string
    string_result = []
    for i in range(length):
        cur_text = df_copy.iloc[i, 1]
        cur_nlp_result = nlp(cur_text)
        # if process is needed
        if process:
            for token in cur_nlp_result:
                if token.text not in punctuations and token.text != ' ':  # remove punctuation and space
                    if not token.is_stop:  # remove stop words
                        token_lemma = token.lemma_  # lemmatization
                        string_result.append(token_lemma)
        # if process is not needed
        else:
            for token in cur_nlp_result:
                if token.text not in punctuations and token.text != ' ':  # remove punctuation and space
                    string_result.append(token)

    # find the 10 most common words
    ten_most_common = Counter(string_result).most_common(10)  # retrieved from: https://stackoverflow.com/questions/16375404/how-do-i-find-the-most-common-words-in-multiple-separate-texts


    return ten_most_common
