import pandas as pd
import numpy as np
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.info())
print(df.describe())
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
df['TotalCharges'] = df['TotalCharges'].astype(float)
df['TotalCharges'] = df['TotalCharges'].fillna(0)
df.replace('No internet service', 'No', inplace=True)
df.replace('No phone service', 'No', inplace=True)
print(df.info())
df.to_csv("Telco-Customer-Churn-Cleaned.csv", index=False)