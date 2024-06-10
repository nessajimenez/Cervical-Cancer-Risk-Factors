#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

def correct_columns(df, column):
    """
    Correct column type
    """
    df[column] = df[column].astype(float)
    return df[column]


def fill_na_with_mean(df, column):
    """
    Fill NaN values in a specified column with the mean of that column.
    """
    # Calculate the mean of the specified column
    mean_value = df[column].mean()
    
    # Fill NaN values in the specified column with the mean value
    df[column].fillna(mean_value, inplace=True)
    
    return df