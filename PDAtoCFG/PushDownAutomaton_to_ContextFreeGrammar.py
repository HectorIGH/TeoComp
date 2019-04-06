import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *
import os
import csv

# Reading file removing extra notation
root = Tk()
root.withdraw()
root.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select .fda file to extract RegEx", filetypes = ((".ap files", "*.ap"),("all files", "*.*")))
data = pd.read_csv(root.filename, skipfooter = 1, sep = "\t|;|,| |=|\)|\(|\{|\}|F.", header = None, engine = 'python')
df = pd.DataFrame(data)
# Get the row count
with open(root.filename, "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    row_count = len(data)
# Read only the final line for the accept states
dataN = pd.read_csv(root.filename, skiprows = row_count - 1, sep = "\t|;|,| |=|\)|\(|\{|\}|F.", header = None, engine = 'python')
dfN = pd.DataFrame(dataN)
finales = []
for i in range(len(dfN.iloc[0])):
    if(type(dfN.iloc[0][i]) == type('F') or (not np.isnan(dfN.iloc[0][i]))):
        finales.append(dfN.iloc[0][i])

print("@Author: Hector Ivan Garcia-Hernandez\n")

# Auxiliar array
states = [[] for i in range(len(df))]

# Sieving not useful data
for row in range(len(df)):
    for i in range(len(df.iloc[row])):
        if (type(df.iloc[row][i]) == type('F') or (not np.isnan(df.iloc[row][i]))):
            states[row].append(df.iloc[row][i])

pila = []
for row in range(len(df)):
    if (not (states[row][-1] in pila)):
        pila.append(states[row][-1])

nodos = []
for row in range(len(df)):
    if (not (states[row][0] in nodos)):
        nodos.append(states[row][0])
nodos += finales



print(states)
print(finales)
print(pila)
print(nodos)











