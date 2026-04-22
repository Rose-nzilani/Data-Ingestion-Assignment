import pandas as pd

# Load CSV data
df = pd.read_csv("employees.csv")

print(df)

#Convert data to apache parquet
# Save as parquet
df.to_parquet("employees.parquet")

print("Parquet file created!")

# Read parquet file
parquet_df = pd.read_parquet("employees.parquet")

print(parquet_df)