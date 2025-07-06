import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Loading data
df = pd.read_csv("unemployment_data.csv")

# Cleaning column names
df.columns = df.columns.str.strip()

# Droping missing values
df.dropna(inplace=True)

# Converting 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Title for the Streamlit app
st.title("Indian Unemployment Rate Dashboard")
st.markdown("This dashboard provides an interactive analysis of unemployment data across Indian states before and during the COVID-19 period.")

# Sidebar filters (for choosing regions and area types)
st.sidebar.header("Filter the data")
regions = st.sidebar.multiselect("Select Region(s)", options=df['Region'].unique(), default=df['Region'].unique())
areas = st.sidebar.multiselect("Select Area Type", options=df['Area'].unique(), default=df['Area'].unique())

# Filtered Data(After applying the filters)
filtered_df = df[df['Region'].isin(regions) & df['Area'].isin(areas)]

# Key Metrics
st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Unemployment Rate (%)", round(filtered_df['Estimated Unemployment Rate (%)'].mean(), 2))
col2.metric("Max Unemployment Rate (%)", round(filtered_df['Estimated Unemployment Rate (%)'].max(), 2))
col3.metric("Min Unemployment Rate (%)", round(filtered_df['Estimated Unemployment Rate (%)'].min(), 2))

# Line Char
st.subheader("Unemployment Rate Over Time")
line_fig = px.line(filtered_df.sort_values('Date'), x='Date', y='Estimated Unemployment Rate (%)', color='Region')
st.plotly_chart(line_fig, use_container_width=True)

# Bar Chart
st.subheader("Average Unemployment Rate by Region")
bar_data = filtered_df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
bar_fig = px.bar(bar_data, orientation='h', title="Average Unemployment Rate by Region")
st.plotly_chart(bar_fig, use_container_width=True)

# Pie Chart
st.subheader("Area Distribution in Data")
pie_fig = px.pie(filtered_df, names='Area', title="Urban vs Rural Records")
st.plotly_chart(pie_fig, use_container_width=True)

# Correlation Heatmap
st.subheader("Correlation between Variables")
corr = filtered_df.select_dtypes(include='number').corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# Showing raw data 
with st.expander("Show Raw Data"):
    st.write(filtered_df)
 
