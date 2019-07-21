#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:09:55 2019

@author: vpfernandez
"""

#Linear reg buffet

import pandas as pd
import statsmodels.api as sm
import operator
import copy


def dc(x):
    return copy.deepcopy(x)

def remove_most_insignificant(df, results, results2):

    max_p_value = max(results.pvalues.iteritems(), key=operator.itemgetter(1))[0]
    max_p_value2 = max(results2.pvalues.iteritems(), key=operator.itemgetter(1))[0]
    
    if max_p_value == 'const':
        df.drop(columns = max_p_value2, inplace = True)
    else:
        df.drop(columns = max_p_value, inplace = True)
    return df


def importbuffet():
    
    file = r'/Data.xlsx'
    sheet = 'ALL'
    df = pd.read_excel(file,sheet) #for an earlier version of Excel, you may need to use the file extension of 'xls'
    #print (df)
    
    df = df.drop(df.index[[0]])
    Y = df['RETURNS']
    X = df[df.columns[4:]]
    
    st = 20-4
    
    X = X[X.columns[st:st+30]]
    
    model = sm.OLS(Y, sm.add_constant(X[X.columns[1:42]]), missing='drop').fit()
    model2 = sm.OLS(Y, X[X.columns[1:42]], missing='drop').fit()
    print(model.summary())
    
    return (X,Y,model,model2)
    
(X,Y,model,model2) = importbuffet()

fval = model.fvalue
adjR2 = model.rsquared_adj

fvalnew = 999
brek = 0

while brek < 10 and model.df_model > 2:
    X_old = dc(X)
     
    X = remove_most_insignificant(X, model, model2)

    model = sm.OLS(Y, sm.add_constant(X), missing='drop').fit()
    model2 = sm.OLS(Y, X, missing='drop').fit()
    #print(model.summary())

    fvalnew = model.fvalue
    adjR2new = model.rsquared_adj
    
    if ((fvalnew > fval*0.95) and (adjR2new > adjR2*0.95)) or (fvalnew == 0.0 and brek != 0):
        brek = 0
        fval = fvalnew
        adjR2 = adjR2new
        
    else:
        X = dc(X_old)
        brek += 1
            
            
model = sm.OLS(Y, sm.add_constant(X), missing='drop').fit()
model2 = sm.OLS(Y, X, missing='drop').fit()
print(model.summary())
