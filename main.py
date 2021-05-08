import csv
import pandas as pd 

df = pd.read_csv("P130/total_stars.csv")
# this didn't work :(
for row in df:
    row.replace(","," ")
    

df.dropna()

del df["Luminosity"]
del df["Star_name1"]
del df["distance_from_earth1"]
del df["Mass"]
del df["Radius"]

df.to_csv("P130/main.csv")