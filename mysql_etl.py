import pandas as pd
import mysql.connector
#Connect to mysql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rose@079256",
    database="student_db"
)

#Extract database
query = "SELECT * FROM students"
df = pd.read_sql(query, conn)

print("Extracted Data:")
print(df)

# transform: add grade column
df['grade'] = df['marks'].apply(lambda x: 'Pass' if x >= 75 else 'Fail')

# load: save to CSV
df.to_csv("students_cleaned.csv", index=False)

print("\nTransformed data saved to students_cleaned.csv")
