#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:55:10 2020

@author: ing
"""

import pandas as pd
import numpy as np
from datetime import date

def countEachProductStock():
    today = date.today().strftime('%Y-%m-%d')
    data_file = "DATAFACTORY1.xlsx"
    data = pd.read_excel(data_file)
    preprocessed_data = data.iloc[:, [18, 10, 1]]
    preprocessed_data.columns = ["product", "entry_date", "release_date"]
    return(preprocessed_data.loc[(preprocessed_data.entry_date<today)
    & (preprocessed_data.release_date.isna()), 'product'].value_counts().to_json())

countEachProductStock()
