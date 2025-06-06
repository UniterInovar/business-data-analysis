# 06_visual_dashboard.py

import pandas as pd
import matplotlib.pyplot as plt

def dashboard(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    df.groupby('month')['total_revenue'].sum().plot(ax=axs[0, 0], title="Monthly Sales Trend")
    df.groupby('region')['total_revenue'].sum().plot(kind='bar', ax=axs[0, 1], title="Sales by Region")
    df.groupby('product_category')['total_revenue'].sum().nlargest(5).plot(kind='bar', ax=axs[1, 0], title="Top Products")
    df['payment_method'].value_counts().plot(kind='pie', ax=axs[1, 1], title="Payment Methods", autopct='%1.1f%%')

    plt.tight_layout()
    plt.savefig("../exports/dashboard.png")

if __name__ == "__main__":
    from 01_load_and_clean import load_data, clean_data
    df = load_data("../data/cleaned_business_sales_data.xlsx")
    df = clean_data(df)
    dashboard(df)
