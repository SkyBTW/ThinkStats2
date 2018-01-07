#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:15:04 2018

@author: sky
"""

from __future__ import print_function

#import math
#import numpy as np

import nsfg
#import first
import thinkstats2
import thinkplot

# Q2 - Ex 1
resp = nsfg.ReadFemResp()

#n = resp['numkdhh'].Total()
pmf_tr = thinkstats2.Pmf(resp['numkdhh'], label='Actual')
#pmf_tr = pmf.Copy(label='Actual')

#thinkplot.PrePlot(2, cols=2)
#thinkplot.Hist(pmf_tr, align='left', width=.45)
#thinkplot.Hist(pmf_tr, align='right', width=.45)
#thinkplot.Config(xlabel='children per household', ylabel='probability')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf_tr, label='Biased - Predicted Survey')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_tr, biased_pmf])
thinkplot.Config(xlabel='Children per household', ylabel='PMF')

mn_rl = pmf_tr.Mean()
mn_obs = biased_pmf.Mean()