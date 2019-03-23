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
root.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select .fda file to extract RegEx", filetypes = ((".fda files", "*.afd"),("all files", "*.*")))
data = pd.read_csv(root.filename, skipfooter = 1, sep = "\t|,| |=|\)|\(|\{|\}|F.", header = None, engine = 'python')
df = pd.DataFrame(data)
# Get the row count
with open(root.filename, "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    row_count = len(data)
# Read only the final line for the accept states
dataN = pd.read_csv(root.filename, skiprows = row_count - 1, sep = "\t|,| |=|\)|\(|\{|\}|F.", header = None, engine = 'python')
dfN = pd.DataFrame(dataN)
finales = []
for i in range(len(dfN.iloc[0])):
    if(not np.isnan(dfN.iloc[0][i])):
        finales.append(dfN.iloc[0][i])

print("@Author: Hector Ivan Garcia-Hernandez\n")
e = input("Input the symbol to be used as 'epsilon': ")

# Auxiliar array
states = [[] for i in range(len(df))]

# Sieving garbage data
for row in range(len(df)):
    for i in range(len(df.iloc[row])):
        if (type(df.iloc[row][i]) == type('F') or (not np.isnan(df.iloc[row][i]))):
            states[row].append(df.iloc[row][i])

# Casting number of states into ints
max = -1 # Variable to store the bigger numbered state
for i in range(len(states) - 1):
    states[i][0] = int(states[i][0])
    states[i][2] = int(states[i][2])
    if (max < int(states[i][0])):
        max = int(states[i][0])
    if (max < int(states[i][2])):
        max = int(states[i][2])

for i in range(len(finales)):
    finales[i] = int(finales[i])

# Adding epsilon transitions
states = [[0, e, 1]] + states
#finales = states.pop(-1) # Retrieve the list of final nodes in the original FDA
for i in range(len(finales)):
    states += [[finales[i], e, max + 1]] # Add epsilon transition for each final state
finales = [max + 1] # Update the list of final states

# Transform python 2d array to numpy array for sorting by two columns
states = np.array(states)
# Get the sorted indexes
ind = np.lexsort((states[:,2], states[:,0]))
# Create the ordered qs as a python array
qs = [states[i] for i in ind]
# Transform qs to numpy array
qs = np.array(qs)
#Return qs as regular python array
qs = qs.tolist()
# Transform again to int
for i in range(len(qs)):
    qs[i][0] = int(qs[i][0])
    qs[i][2] = int(qs[i][2])

# Start the process
print("Initial transitions states, after adding epsilon ",e," transitions:")
print(np.matrix(qs))

istates = [i for i in range(0, max + 1)]
jstates = [i for i in range(1, max + 2)]
statesQrip = [i for i in range(1, max + 1)]

while len(statesQrip):
    print("\nStates to rip:", statesQrip)
    qrip = statesQrip.pop(0)
    print("Ripping node:", qrip)
    istates.remove(qrip)
    print("i-states:", istates)
    jstates.remove(qrip)
    print("j-states:", jstates)

    maux = [] # Auxiliar matrix to store the temporarly regular expressions
    for i in istates:
        for j in jstates:
            regex = ""
            r1, r2, r3, r4 = "","","",""
            for k in range(0, len(qs), 1):
                if (qs[k][0] == i and qs[k][2] == qrip):
                    r1 = qs[k][1]
            #for k in range(0, len(qs), 1):
                if (qs[k][0] == qrip and qs[k][2] == qrip):
                    r2 = qs[k][1]
            #for k in range(0, len(qs), 1):
                if (qs[k][0] == qrip and qs[k][2] == j):
                    r3 = qs[k][1]
            #for k in range(0, len(qs), 1):
                if (qs[k][0] == i and qs[k][2] == j):
                    r4 = qs[k][1]

            if (r1 != "" and r3 != ""):
                if (r4 != ""):
                    if (r2 == ""):
                        regex = "("+r1 + r3 + "|" + r4+")"
                    else:
                        regex = "("+r1 + "(" + r2 + ")*" + r3 + "|" + r4+")"
                else:
                    if (r2 == ""):
                        regex = r1 + r3
                    else:
                        regex = r1 + "(" + r2 + ")*" + r3
            else:
                regex = r4

            if (regex != ""):
               maux.append([i, regex, j])
               
    qs = maux
    print("Current states transitions:")
    print(np.matrix(qs))

print("\nFinal state transitions")
print(qs)
print("\nRegEx in standard form:")
print(qs[-1][1])
print("\nRegEx in \"web\" form:")
print(qs[-1][1].replace("|", "+"))
input("Press enter to exit")

















