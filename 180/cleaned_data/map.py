import pandas as pd
import os
from matrix_gen import combine_districts
from h_gen import combine

combine('AP.txt')
os.remove('fixedAP.txt')

elementary = ["E09.txt", "E10.txt", "E11.txt", "E12.txt", "E13.txt", "E14.txt"]

for i in elementary:
    combine_districts(i)
for i in elementary:
    os.remove('fixed'+i)
ap = pd.read_csv('finalAP.txt')
el = pd.read_csv('meanE09.txt')

overlap = list(set(ap['District Code']) & set(el['District Code']))

for i in elementary:
    e = pd.read_csv('mean'+i)
    for j in list(e['District Code']):
        if j not in overlap:
            e = e[e['District Code'] != j]
    e.to_csv("final"+i)
for i in elementary:
    os.remove("mean"+i)
