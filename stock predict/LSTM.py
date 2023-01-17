import numpy as np
import pandas as pd
from keras.layers import LSTM, Dense
from keras.models import Sequential

# Load the data
data = pd.read_csv("stock_prices.csv")

# Split the data into training and test sets
train_data = data[:int(data.shape[0] * 0.8)]
test_data = data[int(data.shape[0] * 0.8):]

# Define the LSTM model
model = Sequential()
model.add(LSTM(100, input_shape=(None, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(train_data, train_data, epochs=100, batch_size=32)

# Make predictions on the test set
predictions = model.predict(test_data)
print("Predicted Value",predictions)
# Evaluate the model's performance
mse = np.mean((predictions - test_data) ** 2)
print("Mean Squared Error: ", mse)

