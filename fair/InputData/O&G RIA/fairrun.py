# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import fair
import sys

file = str(sys.argv)
files = []
for x in file.split(',')[1:]:
    files.append(x[2:-2])

datas = [pd.read_csv(x).to_numpy() for x in files]
end_zeros = np.zeros((400, 40))

errorfixed = [np.array(list(x) + list(end_zeros)) for x in datas]

outs = []
for x in errorfixed:
    C, F, T = fair.forward.fair_scm(emissions=x)
    outs.append([C, F, T])
    
out_types = ['Concentration_', 'Forcing_', 'Temperature_']
for x in range(len(outs)):
    for y in range(len(out_types)):
        pd.DataFrame(outs[x][y]).to_csv("%s%s.csv"%(out_types[y], files[x].split('\\')[-1][:-4]))