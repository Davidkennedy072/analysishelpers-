# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:08:01 2018
@author: David
Save figures to pdf
"""


import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf 
import os

def savefiguretopdf(path, pdfname, closeall = True, figure1 = 1):
    os.chdir(path)
    pdf = matplotlib.backends.backend_pdf.PdfPages(path+'/'+pdfname+'.pdf')
    for fig in range(figure1, plt.gcf().number + 1):
        fig = plt.figure(fig)
        pdf.savefig(fig)
    pdf.close() 
    if closeall == True:
        plt.close('all')

def savefigureloop(path = os.getcwd(), pdfname = 'pdffile.pdf'): # Python Closure 
    pp = matplotlib.backends.backend_pdf.PdfPages(path+'/'+pdfname)
    def saveto(figure):
        pp.savefig(figure)
        return None
    return saveto, pp
        
if __name__ == '__main__':
    savefiguretopdf(path = 'C:/Users/zae/Documents/summer2018/replicationvariation/', 
                    pdfname = 'DY_RTgraphs', closeall = True)