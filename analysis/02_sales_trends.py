# 02_sales_trends.py

import pandas as pd

def sales_trends(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    trends = df.groupby('month')['total_revenue'].sum().reset_index()
    return trends

if __name__ == "__main__":
    from 01_load_and_clean import load_data, clean_data
    df = load_data("../data/cleaned_business_sales_data.xlsx")
    df = clean_data(df)
    trends = sales_trends(df)
    print(trends)
