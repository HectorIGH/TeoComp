import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *

# Reading file removing extra notation
root = Tk()
root.withdraw()
root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select .fda file to extract RegEx", filetypes = ((".fda files", "*.afd"),("all files", "*.*")))
data = pd.read_csv(root.filename, sep = "\t|,| |=|\)|\(|\{|\}|F.", header = None, engine = 'python')
df = pd.DataFrame(data)

# Auxiliar array
states = [[] for i in range(len(df))]

# Sieving garbage data
for row in range(len(df)):
    for i in range(len(df.iloc[row])):
        if (type(df.iloc[row][i]) == type('F') or (not np.isnan(df.iloc[row][i]))):
            states[row].append(df.iloc[row][i])

# Casting number of states into ints
max = -1 # Variable to store the bigger node
for i in range(len(states) - 1):
    states[i][0] = int(states[i][0])
    states[i][2] = int(states[i][2])
    if (max < int(states[i][0])):
        max = int(states[i][0])
    if (max < int(states[i][2])):
        max = int(states[i][2])

for i in range(len(states[-1])):
    states[-1][i] = int(states[-1][i])

# Adding epsilon transitions
states = [[0, 'E', 1]] + states
finales = states.pop(-1) # Retrieve the list of final nodes in the original FDA
for i in range(len(finales)):
    states += [[finales[i], 'E', max + 1]] # Add epsilon transition for each final state
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

#TO TEST WE SKIP FILE READING
#max = 3
#qs = [[0, 'E', 1], [1, 'a', 2], [1, 'b', 3], [2, 'a', 1], [2, 'b', 2], [2, 'E', 4], [3, 'b', 1], [3, 'a', 2], [3, 'E', 4]]
print("Initial transitions states, after adding epsilon (E) transitions:")
print(np.matrix(qs))

istates = [i for i in range(0, max + 1)]
jstates = [i for i in range(1, max + 2)]
statesQrip = [i for i in range(1, max + 1)]
print("States to rip:", statesQrip)
#print("States to be i", istates)
#print("States to be j", jstates)

while len(statesQrip):
    qrip = statesQrip.pop(0)
    print("Ripping node:", qrip)
    istates.remove(qrip)
    print("i-states:", istates)
    jstates.remove(qrip)
    print("j-states:", jstates)
    print("Current states transitions:")
    print(np.matrix(qs))
    maux = []
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
                        if (r1 != 'E'):
                            if (r3 != 'E'):
                                regex = "("+r1 + r3 + "|" + r4+")"
                            else:
                                regex = "("+r1 + "|" + r4+")"
                        else:
                            if (r3 != 'E'):
                                regex = "("+r3 + "|" + r4+")"
                            else:
                                regex = r4 #Tal vez innecesario
                    else:
                        if (r1 != 'E'):
                            if (r3 != 'E'):
                                regex = "("+r1 + "(" + r2 + ")*" + r3 + "|" + r4+")"
                            else:
                                regex = "("+r1 + "(" + r2 + ")*" + "|" + r4+")"
                        else:
                            if (r3 != 'E'):
                                regex = "("+"(" + r2 + ")*" + r3 + "|" + r4+")"
                            else:
                                regex = "("+"(" + r2 + ")*" + "|" + r4+")"
                else:
                    if (r2 == ""):
                        if (r1 != 'E'):
                            if (r3 != 'E'):
                                regex = r1 + r3
                            else:
                                regex = r1
                        else:
                            if (r3 != 'E'):
                                regex = "("+r3+")"
                    else:
                        if (r1 != 'E'):
                            if (r3 != 'E'):
                                regex = r1 + "(" + r2 + ")*" + r3
                            else:
                                regex = r1 + "(" + r2 + ")*"
                        else:
                            if (r3 != 'E'):
                                regex = "(" + r2 + ")*" + r3
                            else:
                                regex = "(" + r2 + ")*"
            else:
                regex = r4

            if (regex != ""):
               maux.append([i, regex, j])
               
    qs = maux

print("Final state transitions")
print(qs)
print("RegEx in standar form:")
print(qs[-1][1])
print("RegEx in \"web\" form:")
print(qs[-1][1].replace("|", "+"))
input("Press enter to exit")

















