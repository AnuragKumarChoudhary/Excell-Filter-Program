import numpy as np
import pandas as pd
import xlrd
import csv

data = pd.read_excel("Open Mic  (Responses) (2).xlsx")
#data

dt_pho = data[data["Category "].astype("str").str.contains("Singing")]

print(dt_pho)
name = 'Singing.csv'
f = open(name, "w", encoding='utf-8', errors='ignore')
writer = csv.writer(f)
writer.writerow(["Name", "Contact Number", "Whatsapp Number", "Gender", "Stream", "Year", "Events"])
writer.writerow(dt_pho['Name'])
writer.writerow(dt_pho['Email Address'])
writer.writerow(dt_pho['Contact Number '])
writer.writerow(dt_pho['Submit Your File Here '])
#writer.writerow(dt_pho['Gender'])
writer.writerow(dt_pho['Branch'])
writer.writerow(dt_pho['Year '])
writer.writerow(dt_pho['Roll'])
writer.writerow(dt_pho['Category '])
