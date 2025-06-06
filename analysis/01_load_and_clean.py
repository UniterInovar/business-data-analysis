# 01_load_and_clean.py

import pandas as pd

def load_data(filepath):
    df = pd.read_excel(filepath)
    return df

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

if __name__ == "__main__":
    path = "../data/cleaned_business_sales_data.xlsx"
    df = load_data(path)
    df = clean_data(df)
    print(df.info())
