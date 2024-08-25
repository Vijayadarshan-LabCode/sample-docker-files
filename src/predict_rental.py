import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Load Data
rentalPD = pd.read_csv('data/rental_1000.csv')

# Prepare Data
X = rentalPD[['rooms', 'sqft']].values  # Features - rooms and sqft
y = rentalPD['price'].values            # Label - price

# Split Data for Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model Training
model = LinearRegression().fit(X_train, y_train)

# Actuals and Predictions from dataset
predicted_rental = model.predict(np.array([[X_test[0][0], X_test[0][1]]]))

print("########################################### Testing Data Rental Price Prediction ###########################################")
print("Actual Rental Price for Property with rooms=",X_test[0][0],"and Area Sqft=",X_test[0][1],"is=",y_test[0])
print("Predicted Rental Price for Property with rooms=",X_test[0][0],"and Area Sqft=",X_test[0][1],"is=",predicted_rental)
print("########################################### Testing Data Rental Price Prediction ###########################################")

# Predict on test data
y_pred = model.predict(X_test)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error (RMSE):", rmse)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)

# Get user input for number of rooms and square footage
#rooms = int(input("Enter the number of rooms: "))
#sqft = int(input("Enter the square footage: "))

# Predict rental price based on user input
#user_input = np.array([[rooms, sqft]])
#predicted_price = model.predict(user_input)

#print("########################################### User Input Data Rental Price Prediction ###########################################")
#print(f"Predicted Rental Price for {rooms} rooms and {sqft} sqft is {predicted_price[0]}")
#print("########################################### User Input Data Rental Price Prediction ###########################################")


