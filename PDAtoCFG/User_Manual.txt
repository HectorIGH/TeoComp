@ Author: Hector Ivan Garcia-Hernandez

In order to use this script you will need to have installed 'numpy' and 'pandas'. Pandas is used to read the file and format it accordingly. Numpy is used to present the results as a matrix; it is also used to validate if the character read is NaN or a number.


The script will take a pushdown automaton in .ap file as input and will give the corresponding context free grammar as output. It will output the results of every and each of the four steps in order.

The .ap file MUST have the following structure: 
- A list of the transitions between states in the form (nameOfOriginState, symbolReadFromString, symbolToPopFromStack; nameOfTargetState, symbolToPushToStack).
- A set named F that contains all of the accept states in the form F = {nameOfState, nameOfState, ...}.
- The lambda symbol is represented by '\', without the quotes.

A valid .ap file is, for example:
(i,c,\;g,c)
(g,b,\;g,\)
(g,c,c;h,\)
F = {h}

For the user convenience, the script comes along with a pushdown automaton already translated in this file format.

Once the script is executed it will show a GUI to select the .ap file. If the selected file is formated correctly the script will start to perform the four steps in order to obtain the CFG.

The script performs the four steps completely before presenting results. In other words, the results are printed only after the whole computation is done.

The script will print "From step i:", with i matching the step performed, and then it will print the list of production rules that were generated.

Finally, it will ask you to press enter to exit.

