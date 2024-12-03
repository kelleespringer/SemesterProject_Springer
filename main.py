import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df_non_farm = pd.read_csv('data/non_farm_data.csv')
df_unemployment = pd.read_csv('data/unemployment_data.csv')

# Streamlit header
st.title("Labor Statistics Dashboard")

# Display data for non-farm payrolls
st.subheader("Non-Farm Payroll Employment")
st.line_chart(df_non_farm.set_index('date')['value'])

# Display data for unemployment rate
st.subheader("Unemployment Rate")
st.line_chart(df_unemployment.set_index('date')['value'])


