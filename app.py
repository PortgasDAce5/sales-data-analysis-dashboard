import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Data Analysis Dashboard")

# Load Data
df = pd.read_csv("sales.csv")

# Map dataset columns to match the dashboard's expected fields
df.rename(columns={
    'Date': 'Order Date',
    'City': 'Region',
    'Product line': 'Category',
    'Payment': 'Sub-Category',
    'Total': 'Sales'
}, inplace=True)

# Show Raw Data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Data Cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar Filters
st.sidebar.header("Filter Data")

region = st.sidebar.selectbox("Select Region", df['Region'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == region) & (df['Category'] == category)]

# Show Filtered Data
st.subheader("Filtered Data")
st.write(filtered_df)

# Total Sales
total_sales = filtered_df['Sales'].sum()
st.metric("Total Sales", f"${total_sales:,.2f}")

# Sales by Sub-Category
st.subheader("Sales by Sub-Category")
subcat_sales = filtered_df.groupby('Sub-Category')['Sales'].sum()

fig1, ax1 = plt.subplots()
subcat_sales.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Sales Over Time
st.subheader("Sales Over Time")
time_sales = filtered_df.groupby('Order Date')['Sales'].sum()

fig2, ax2 = plt.subplots()
time_sales.plot(ax=ax2)
st.pyplot(fig2)