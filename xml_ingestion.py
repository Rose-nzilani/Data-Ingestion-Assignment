import pandas as pd

#Read xml file
data = pd.read_xml("students.xml")

print(data)