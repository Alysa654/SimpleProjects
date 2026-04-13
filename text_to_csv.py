# Made by Alysa Solomon
# Designed to help Illinois State University's Sociology and Anthropology Depatments
# takes text files from JSTOR to a CSV file
import pandas as pd

data = {"ISSN" : ["342, 4324"], "URL": ["efw"], "Abstract": ["fosme"], "Author": ["person"], "Journal": ["fjewio"], "Number": ["12"], "Pages":  ["pp 12"], "Publisher": ["Pluto"], "Title":["eiw"], "Volume": ["5"], "Year": ["4214"]}

print(len(data))

df = pd.DataFrame(data)
print(df)
