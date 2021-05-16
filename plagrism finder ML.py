#Plagrism finder with difflib
import os
import re
import pandas as pd
import numpy as np
from difflib import SequenceMatcher
#The only thing that is needed here is
#the path of files in your computer
path = "C:\\programs\\..."
files = [code for code in os.listdir(path) if code.endswith('.c')] # you can change it for other programming softwares like *.py 
notes =[open(File).read() for File in  files]
#Removing the first two rows of files (mostly similar) for c programming
new_notes = []
for k in notes:
    cleaned_notes = re.sub("#include <stdio.h>" , "", k)
    cleaned_notes = re.sub("#include <stdlib.h>" , "", cleaned_notes)
    new_notes.append(cleaned_notes)

#Converting results in the form of a dataframe 
df = pd.DataFrame(columns = ["StudentA","StudentB","Similarity"])
student_A = []
student_B = []
match_list = []


for m in files:
    for n in files:
        student_A.append(m)
        student_B.append(n)

#Calculating similarity
for i in new_notes:
    for j in new_notes:
        studentA = i
        studentB = j
        Similarity = SequenceMatcher(None, studentA , studentB).ratio()
        Similarity = round(Similarity *100, 2)
        match_list.append(Similarity)


#Importing calculated data into the dataframe
df["StudentA"] = student_A
df["StudentB"] = student_B
df["Similarity"] = match_list


#Sorting rows and removing duplicated and permuted rows 
df = df[df['StudentA'] < df['StudentB']]
df_sorted = df.sort_values("Similarity",ascending=False)
df_sorted = df_sorted.reset_index(inplace=False)
df_sorted = df_sorted.drop(['index'],  axis=1)


#Printing the final result
print(df_sorted)