# load libraries
import streamlit as st
import matplotlib.pyplot
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

# Load data
df= pd.read_csv("C:/Users/RICH-FILES/Downloads/MachineLearning/10 portfolioprojects/Walmart_Sales.csv", dayfirst=True, parse_dates=True)

# extract date and weekly sales columns
sales_df = df[['Date', 'Weekly_Sales']]
# correct Date data type from str to datetime
sales_df.loc[:, 'Date'] = pd.to_datetime(sales_df['Date'], dayfirst=True)
# change column names
sales_df.columns = ['ds', 'y']
# Train Prophet model
model = Prophet()
model.fit(sales_df)
# Streamlit Interface
st.title('Time Series Forecasting with Prophet')
periods = st.number_input('Enter number of future weeks to predict', min_value=1, max_value=52)

future = model.make_future_dataframe(periods= periods ,  freq= 'W')
forecast = model.predict(future)

st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

# Plot the forecast
fig = model.plot(forecast)

st.pyplot(fig)
# visualize components

st.subheader('Forecast Components')
fig_components = plot_components_plotly(model, forecast)
st.plotly_chart(fig_components)
