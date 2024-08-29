import numpy as np
import matplotlib.pyplot as plt

# Calculating the coefficients of linear regression equation 
def calculate_linreg_coef(x, y):
    Grad, Coeff1 = np.polyfit(x, y, 1)
    return Grad, Coeff1

# Calculating the predicted values using the best-fit line
def calculate_predval(x, Grad, Coeff1):
    return Grad * x + Coeff1

# Calculating the error (observed - predicted)
def calculate_error(observed, predicted):
    return observed - predicted

# Calculating the variance of the error
def calculate_error_var(error):
    return np.var(error)

# Creating NumPy arrays for distances and RSSI values
distances = np.array([1, 2, 2, 2, 4, 7, 9, 12, 12, 14, 15, 22, 31, 31, 43, 49, 77, 109, 122, 154, 172, 172, 172, 172, 243, 247, 243, 243])
rssi_values = np.array([-48,-50,-47,-48,-53,-57,-59,-62,-62,-63,-64,-67,-70,-70,-73,-74,-78,-81,-82,-84,-85,-85,-85,-86,-88,-88,-90,-91])

# Calculating the logarithm of distances
log_distances = np.log10(distances)

# Calculate linear regression coefficients
Grad, Coeff1 = calculate_linreg_coef(log_distances, rssi_values)

# Calculate predicted RSSI values
predicted_rssi = calculate_predval(log_distances, Grad, Coeff1)

# Calculating the error
error = calculate_error(rssi_values, predicted_rssi)

# Calculating error variance
error_variance = calculate_error_var(error)

# Creating a scatter plot
plt.scatter(log_distances, rssi_values, label='RSSI Data')

# Plotting the best-fit line
plt.plot(log_distances, predicted_rssi, color='red', label=f'Best-fit Line :-Gradient: {Grad:.2f}')
path_loss_exponent = abs(Grad / 10)
print(f'Path Loss Exponent: {path_loss_exponent:.2f}')

# Add labels and a title
plt.xlabel('Log Distance')
plt.ylabel('RSSI Values')
plt.title('RSSI vs. Log Distance with Best-fit Line')

# Showing a legend as well as showing the plot
plt.legend()
print(f'Error Variance: {error_variance:.2f}')
plt.show()


'''
**Step1: Finding the Path Loss Exponent**
Below are the steps I have followed:-

Data Collection: I gathered the data using "WiFi Analyzer" app, which resulted in two lists: distances and RSSI values.

Distance Transformed by taking log: I converted the distances into the logarithmic scale (base 10) using log10(x) to better understand the relationship between distance and RSSI.

Data Visualization using matplotlib: The data was visualized using the matplotlib library, with distances on the x-axis and RSSI values on the y-axis.
                    Then I created a scatter plot to display the data points.

Best-Fit Line: A best-fit line was added to the plot using linear regression. The slope of this line represents the path loss exponent, which was calculated as the absolute value of the slope divided by 10.

Path Loss Exponent: The path loss exponent was computed and displayed, providing insights into how signal strength attenuates with distance.

Variance Calculation: The variance of the error (the difference between observed and predicted RSSI values) was calculated and shown as the "variance" in the final output.

I am attaching the output which is plot RSSI values and Log Distances
'''