'''
Assume df is a pandas dataframe object of the dataset given
'''

from math import log2
import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float


def get_entropy_of_dataset(df):
    # TODO
    entropy = 0
    count = 0
    tar = df.columns[-1]
    array_st = df[tar].value_counts()
    for i in array_st:
        count += i
    for med in array_st:
        entropy += -(med/count)*log2(med/count)
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float


def get_avg_info_of_attribute(df, attribute):
    # TODO
    # attrDict = {}
    # avg_info = 0
    # count = 0
    # for index, row in df.iterrows():
    #     attrDict[row[attribute]] = []
    #     count += 1

    # for index, row in df.iterrows():
    #     attrDict[row[attribute]].append(row[-1])

    # for values in attrDict.values():
    #     print(values)
    #     yes = values.count("yes")
    #     no = values.count("no")
    #     avg_info += ((yes+no)/count)*entropy_attr(yes, no)
    #     print(yes, no)
    #     print(attribute, avg_info)
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float


def get_information_gain(df, attribute):
    # TODO
    return information_gain


#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    pass


def entropy_attr(yes, no):
    if yes == 0 or no == 0:
        return 1
    ans = -(yes/(yes+no))*log2(yes/(yes+no)) - \
        (no/(yes+no))*log2(no/(yes+no))
    return (ans)
