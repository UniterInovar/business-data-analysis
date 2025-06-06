# 04_regional_analysis.py

import pandas as pd

def regional_sales(df):
    return df.groupby('region')['total_revenue'].sum().reset_index()

if __name__ == "__main__":
    from 01_load_and_clean import load_data, clean_data
    df = load_data("../data/cleaned_business_sales_data.xlsx")
    df = clean_data(df)
    print(regional_sales(df))
