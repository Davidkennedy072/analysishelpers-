# -*- coding: utf-8 -*-
"""
Created on 9/26/2018
@author: David
Plotter class with useful plotting functions
"""
class plotter(object):
    '''Plotter class '''
    def __init__(self, X, Y):
        '''X = [x1, x2, x3...], Y = [y1, y2, y3...]'''
        self.X = X
        self.Y = Y
        return self 

    def inputlength(self):
        ''' Print out length of X and Y input'''
        print(len(self.X), len(self.Y))
        return None
        
