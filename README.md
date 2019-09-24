# Fama-French Decomposer
Fama-French Model used to analyse and decompose Berkshire Hathaway's returns. The program runs a Linear Regression of Berkshire Hathaway's returns against Fama-French 49 Industry Portfolios (Availiable at http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), and randomly drops unsignificant regressors until the F-Statistic and Adjusted R² values aren't inceasing significantly (Caped at a minimum of 3 explanatory variables)

TODO:
- Separate FF Factors and Berkshire Hathaway's returns & find a way to import more data (to be able to decompose any Hedge Fund's most significant investments / risk factors)



```python
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
from copy import deepcopy
```

# Functions

- Deepcopy to make sure the other functions works as intended (*e.g.:* if A=B, and A+=1, then A!=B)
- Looping through the regression in order to remove the most insignificant variables
- Importing the File Properly


```python
def dc(x):
    return deepcopy(x)

def remove_most_insignificant(df, results, results2):

    max_p_value = max(results.pvalues.iteritems(), key=operator.itemgetter(1))[0]
    max_p_value2 = max(results2.pvalues.iteritems(), key=operator.itemgetter(1))[0]
    
    if max_p_value == 'const':
        df.drop(columns = max_p_value2, inplace = True)
    else:
        df.drop(columns = max_p_value, inplace = True)
    return df


def importbuffet():
    
    file = [REDACTED]
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
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                RETURNS   R-squared:                       0.803
    Model:                            OLS   Adj. R-squared:                  0.326
    Method:                 Least Squares   F-statistic:                     1.685
    Date:                Tue, 24 Sep 2019   Prob (F-statistic):              0.171
    Time:                        16:42:54   Log-Likelihood:                -167.53
    No. Observations:                  42   AIC:                             395.1
    Df Residuals:                      12   BIC:                             447.2
    Df Model:                          29                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          5.3886      8.810      0.612      0.552     -13.807      24.584
    Cnstr         -0.1982      0.417     -0.475      0.643      -1.107       0.710
    Steel         -0.1311      0.498     -0.263      0.797      -1.217       0.955
    FabPr          0.0466      0.705      0.066      0.948      -1.489       1.582
    Mach           0.2264      0.727      0.312      0.761      -1.357       1.810
    ElcEq          0.4013      0.668      0.600      0.559      -1.055       1.857
    Autos         -0.5548      0.737     -0.752      0.466      -2.161       1.052
    Aero           0.0135      0.411      0.033      0.974      -0.882       0.909
    Ships         -0.5166      0.350     -1.476      0.166      -1.279       0.246
    Guns          -0.2214      0.276     -0.802      0.438      -0.823       0.380
    Gold           0.2245      0.183      1.229      0.243      -0.174       0.623
    Mines         -0.1192      0.359     -0.332      0.745      -0.901       0.662
    Coal           0.0663      0.244      0.272      0.790      -0.465       0.598
    Oil           -0.0303      0.270     -0.112      0.913      -0.619       0.558
    Util          -0.0396      0.590     -0.067      0.948      -1.326       1.247
    Telcm          0.2625      0.389      0.675      0.513      -0.585       1.110
    PerSv         -0.1033      0.698     -0.148      0.885      -1.624       1.417
    BusSv         -0.4692      1.059     -0.443      0.666      -2.777       1.838
    Hardw         -0.4124      0.636     -0.648      0.529      -1.799       0.974
    Softw          0.2944      0.515      0.572      0.578      -0.827       1.416
    Chips         -0.5554      0.910     -0.611      0.553      -2.537       1.427
    LabEq          0.7345      0.658      1.116      0.286      -0.700       2.169
    Paper          0.0266      0.469      0.057      0.956      -0.995       1.049
    Boxes          0.1444      0.421      0.343      0.738      -0.773       1.062
    Trans          1.2197      0.759      1.607      0.134      -0.434       2.873
    Whlsl         -0.9797      1.174     -0.834      0.420      -3.538       1.579
    Rtail          0.9850      0.726      1.357      0.200      -0.597       2.567
    Meals         -0.3198      0.622     -0.514      0.616      -1.675       1.035
    Banks          0.1257      0.432      0.291      0.776      -0.816       1.067
    Insur          0.9041      0.443      2.040      0.064      -0.062       1.870
    ==============================================================================
    Omnibus:                        4.603   Durbin-Watson:                   2.367
    Prob(Omnibus):                  0.100   Jarque-Bera (JB):                3.918
    Skew:                           0.748   Prob(JB):                        0.141
    Kurtosis:                       3.053   Cond. No.                         379.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Reducing The Regression Automatically

Using the function Coded above in order to automatically remove the most insignificant variables

- Regressing
- Removing the most insignificant variable
- If the F-Value or the adj.R² Value decrease too dramatically (5% decrease over one iteration), assume the model doesn't improve by removing insignificant variables, therefore stop the loop


```python
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
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                RETURNS   R-squared:                       0.700
    Model:                            OLS   Adj. R-squared:                  0.627
    Method:                 Least Squares   F-statistic:                     9.608
    Date:                Tue, 24 Sep 2019   Prob (F-statistic):           9.33e-07
    Time:                        16:42:59   Log-Likelihood:                -176.37
    No. Observations:                  42   AIC:                             370.7
    Df Residuals:                      33   BIC:                             386.4
    Df Model:                           8                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          8.3305      3.870      2.152      0.039       0.456      16.205
    FabPr          0.4661      0.202      2.302      0.028       0.054       0.878
    Autos         -0.5910      0.202     -2.919      0.006      -1.003      -0.179
    Ships         -0.3983      0.155     -2.576      0.015      -0.713      -0.084
    Gold           0.1704      0.063      2.713      0.011       0.043       0.298
    Trans          1.1121      0.341      3.263      0.003       0.419       1.806
    Whlsl         -1.6780      0.408     -4.116      0.000      -2.507      -0.848
    Rtail          0.8461      0.282      3.004      0.005       0.273       1.419
    Insur          1.0178      0.234      4.358      0.000       0.543       1.493
    ==============================================================================
    Omnibus:                        2.647   Durbin-Watson:                   2.342
    Prob(Omnibus):                  0.266   Jarque-Bera (JB):                2.346
    Skew:                           0.483   Prob(JB):                        0.309
    Kurtosis:                       2.362   Cond. No.                         117.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Conclusion

As we can see, Berkshire Hattaway most significant risk factors are the Wholesale market (Beta = -1.67), and Transportation (Beta = 1.11).
