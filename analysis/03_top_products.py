# 03_top_products.py

import pandas as pd

def top_products(df, top_n=10):
    return df.groupby('product_category')['total_revenue'].sum().sort_values(ascending=False).head(top_n)

if __name__ == "__main__":
    from 01_load_and_clean import load_data, clean_data
    df = load_data("../data/cleaned_business_sales_data.xlsx")
    df = clean_data(df)
    print(top_products(df))
