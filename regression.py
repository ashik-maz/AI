# Linear Regression Example

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Input data (X)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Target data (Y)
y = np.array([2, 4, 6, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# Model parameters
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict a new value
new_x = [[6]]
prediction = model.predict(new_x)

print("Prediction for x = 6:", prediction[0])

# Plot
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()