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
transitions = [[] for i in range(len(df))]

# Sieving not useful data
for row in range(len(df)):
    for i in range(len(df.iloc[row])):
        if (type(df.iloc[row][i]) == type('F') or (not np.isnan(df.iloc[row][i]))):
            transitions[row].append(df.iloc[row][i])

pila = []
for row in range(len(df)):
    if (not (transitions[row][-1] in pila)):
        pila.append(transitions[row][-1])

states = []
for row in range(len(df)):
    if (not (transitions[row][0] in states)):
        states.append(transitions[row][0])
states += finales
initialState = states[0]

step1 = []
for f in finales:
    step1.append("S -> <" + initialState + ", " + "\\, " + f + ">")
step2 = []
for p in states:
    step2.append("<" + p + ", \\, " + p + "> -> \\")
step3 = []
for transition in transitions:
    if (transition[2] != '\\'):
        for r in states:
            step3.append("<" + transition[0] + ", " + transition[2] + ", " + r + "> -> "
                         + transition[1] + "<" + transition[3] + ", " + transition[-1] + ", " + r + ">")
step4 = []
for transition in transitions:
    if (transition[2] == '\\'):
        for w in pila:
            for k in states:
                for r in states:
                    step4.append("<" + transition[0] + ", " + w + ", " + r + "> -> " + transition[1] + "<" + transition[3] + ", "
                                 + transition[-1] + ", " + k + "><" + k + ", " + w + ", " + r + ">")
            

def printing(matrix):
    for a in matrix:
        print(a + "\n")

print("From step 1:\n")
#print(np.matrix(step1).reshape((-1,1)))
printing(step1)
print("\nFrom step 2:\n")
#print(np.matrix(step2).reshape((-1,1)))
printing(step2)
print("\nFrom step 3:\n")
#print(np.matrix(step3).reshape((-1,1)))
printing(step3)
print("\nFrom step 4:\n")
#print(np.matrix(step4).reshape((-1,1)))
printing(step4)

input("\nPress enter to exit")






