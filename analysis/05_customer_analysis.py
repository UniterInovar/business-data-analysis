# 05_customer_analysis.py

import pandas as pd

def customer_behavior(df):
    return df['customer__name'].value_counts().head(10)

if __name__ == "__main__":
    from 01_load_and_clean import load_data, clean_data
    df = load_data("../data/cleaned_business_sales_data.xlsx")
    df = clean_data(df)
    print(customer_behavior(df))
