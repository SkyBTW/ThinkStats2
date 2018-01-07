#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:49:32 2018

@author: sky
"""

import pandas as pd
import numpy as np

import sys
import nsfg
import thinkstats2
import math


df = nsfg.ReadFemPreg()

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

df.agepreg /= 100.0
na_vals = [97, 98, 99]
df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0

wt_frst = df[df['birthord'] == 1]['totalwgt_lb']
wt_other = df[df['birthord'] > 1]['totalwgt_lb']

wt_mn_1st = wt_frst.mean()
wt_var1 = wt_frst.var()
wt_mn_other = wt_other.mean()
wt_var2 = wt_other.var()
wt_pooled_var = (len(wt_frst) * wt_var1 + len(wt_other) 
    * wt_var2) / (len(wt_frst) + len(wt_other))
wt_cd = CohenEffectSize(wt_frst, wt_other)

###

pl_frst = df[df['birthord'] == 1]['prglngth']
pl_other = df[df['birthord'] > 1]['prglngth']

pl_mn_1st = pl_frst.mean()
pl_var1 = pl_frst.var()
pl_mn_other = pl_other.mean()
pl_var2 = pl_other.var()
pl_pooled_var = (len(pl_frst) * pl_var1 + len(pl_other) 
    * pl_var2) / (len(pl_frst) + len(pl_other))
pl_cd = CohenEffectSize(pl_frst, pl_other)


import thinkplot

#thinkplot.PrePlot(2, cols=2)
#thinkplot.Hist(first_pmf, align='right', width=width)
#thinkplot.Hist(other_pmf, align='left', width=width)
#thinkplot.Config(xlabel='weeks',
#                 ylabel='probability',
#                 axis=[27, 46, 0, 0.6])
#thinkplot.PrePlot(2)
#thinkplot.SubPlot(2)
#thinkplot.Pmfs([first_pmf, other_pmf])
#thinkplot.Show(xlabel='weeks',
#               axis=[27, 46, 0, 0.6])

d = { 7: 8, 12: 8, 17: 14, 22: 4,
          27: 6, 32: 12, 37: 8, 42: 3, 47: 2 }
pmf = thinkstats2.Pmf(d, label='actual')
print('mean', pmf.Mean())

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='class size', ylabel='PMF')

df[]