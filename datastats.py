# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:31:01 2018
@author: David
Statistics on bracket data

Revisted on 9/25/2018. Adding in linear regression from sklearn
"""

import numpy as np
import pandas as pd
import scipy
from sklearn import linear_model

def linearregression(X, Y):
    ''' Takes dataframe or numpy array input
    
    Returns [coefficient, intercepts], R**2 score, predictions using X'''
    lm = linear_model.LinearRegression()
    
    try:
        model = lm.fit(X,Y)
    except ValueError:
        X = np.array(X).reshape(-1, 1)
        
    model = lm.fit(X,Y)
    predicts = lm.predict(X)
    return [lm.coef_, lm.intercept_], lm.score(X,Y), predicts

def tscore(mean, null, std, numoftrials):
    return (mean - null)/(std/np.sqrt(numoftrials))

def ttable(numoftrials, confidence, alpha = False):
    ''' onfidence number between 0 and 1. 95% confidence -> 0.95
    Degree of freedom = number of trials - 1'''
    if alpha == False:
        return scipy.stats.t.ppf(confidence, numoftrials - 1)
    else:
        return scipy.stats.t.ppf(1-confidence, numoftrials-1)

def onesamplettest(condition, parameter, null, fitdata, guassianfit, confidence = 0.95, 
                   alpha = False):
    '''One sample T-Test. Test if weight parameter is significantly different from zero'''
    conditiondata = fitdata.loc[guassianfit['condition'] == condition][parameter]
    mean = conditiondata.mean()
    std = conditiondata.std()
    ttestscore = tscore(mean, null, std, len(conditiondata))
    ttesttable = ttable(len(conditiondata), confidence, alpha = alpha)
    return [ttestscore, ttesttable]


