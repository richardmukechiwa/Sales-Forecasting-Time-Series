#### Project Title: Time Series Forecasting of Weekly Sales Using ARIMA and Prophet

Overview: In this project, I utilized historical sales data to forecast weekly sales for a retail store. The primary goal was to help the business make informed decisions regarding inventory management, staffing, and promotions. The project involved using two time series forecasting models: ARIMA and Prophet.

Dataset:

Weekly Sales: Target variable for predicting weekly sales trends.
Date: Time index used to build the time series.
Methodology:

Data Preprocessing:

The dataset was analyzed for stationarity using the Augmented Dickey-Fuller (ADF) test, which indicated the need for differencing to stabilize the time series.
After preprocessing, the dataset was split into training and test sets for model evaluation.
ARIMA Model:

Using pmdarima’s auto-ARIMA, the best (p, d, q) parameters were automatically selected for the ARIMA model.
ARIMA was particularly effective at modeling the linear trends and short-term dependencies in the data.
Prophet Model:

Prophet, developed by Facebook, was chosen for its ability to model non-linear trends, yearly seasonality, and holiday effects.
The model captured the sales spikes around holidays, which significantly improved the long-term forecasts.
Challenges Faced: A key challenge was handling the differences in RMSE between ARIMA and Prophet. While both models performed reasonably well, Prophet’s ability to handle complex seasonality resulted in a lower RMSE when predicting long-term trends. The key takeaway here was understanding how different models handle seasonality and how that impacts forecast accuracy.

Results:

ARIMA: Delivered robust short-term forecasts but struggled slightly with long-term seasonality.
Prophet: Outperformed ARIMA in capturing seasonal and holiday effects, leading to more accurate long-term forecasts.
Evaluation Metrics:

RMSE and MAE were used to assess model performance:
ARIMA RMSE: X
Prophet RMSE: Y
Prophet’s flexibility with seasonal effects allowed it to produce lower RMSE values compared to ARIMA.
Visualizations: I visualized both models' predictions using Prophet’s built-in tools and Matplotlib. The plots provided clear insights into the forecasted values, seasonal trends, and holiday effects.

Conclusion: Both ARIMA and Prophet are valuable tools for time series forecasting. ARIMA is excellent for short-term forecasting, while Prophet shines in long-term forecasting, particularly in data with holiday and seasonal trends. This project highlights the importance of model selection based on the specific characteristics of the time series data.

Future Work:

Incorporating additional features such as temperature, fuel price, and unemployment rates to improve model accuracy.
Exploring more advanced time series models such as LSTM for deeper insights into long-term patterns.
Tools Used:

Python Libraries: pmdarima (auto-ARIMA), statsmodels (ARIMA), Prophet
Data Visualization: Matplotlib, Prophet’s visualization utilities
Stationarity Testing: Augmented Dickey-Fuller (adfuller)
How to Run:

Clone the repository.
Install dependencies using pip install -r requirements.txt.
Run forecast.py to generate the sales forecast.
