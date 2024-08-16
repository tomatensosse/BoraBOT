#alpha vantage api code: 5ITM8RW00ZJV91OG
from alpha_vantage.timeseries import TimeSeries

api_key = '5ITM8RW00ZJV91OG'

ts = TimeSeries(key=api_key, output_format='pandas')

symbol = 'AMD'
data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

data['20_day_MA'] = data['4. close'].rolling(window=20).mean()

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

scaler = MinMaxScaler()
data[['4. close', '20_day_MA']] = scaler.fit_transform(data[['4. close', '20_day_MA']])

x = data[['20_day_MA', '5. volume']]
y = data['4. close'].shift(-1)

x = x[:-1]
y = y[:-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse}")