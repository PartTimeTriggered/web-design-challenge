import pandas as pd
 
# to read csv file named "samplee"
a = pd.read_csv("C:\Bootcamp-Folder\Web-Design-challenge\Resources\cities.csv")
 
# to save as html file
# named as "Table"
a.to_html("CityData.html")
 
# assign it to a
# variable (string)
html_file = a.to_html()