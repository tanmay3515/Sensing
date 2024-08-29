import numpy as np

# Define the function for distance estimation
def estimate_distance(received_reference_dBm, received_unknown_dBm, path_loss_exponent, reference_distance=1.0):
    estimated_distance = reference_distance * 10**((received_reference_dBm - received_unknown_dBm) / (10 * path_loss_exponent))
    return estimated_distance

# Define parameters
path_loss_exponent = 1.91  # path loss exponent obtained in step 1
received_reference_dBm = -42.0  # Received power at reference distance in dBm
received_unknown_dBm_values = [-47, -53, -64, -70, -85, -90]  # Received power at desired distances in dBm
actual_distances = [2, 4, 15, 31, 172, 243]  # Corresponding actual distances in meters

# Calculate absolute errors and average error
absolute_errors = []

for i in range(6):
    predicted_distance = estimate_distance(received_reference_dBm, received_unknown_dBm_values[i], path_loss_exponent, 1.0)
    absolute_error = abs(predicted_distance - actual_distances[i])
    absolute_errors.append(absolute_error)

average_error = np.mean(absolute_errors)

# Print results
print("Path Loss Exponent:", path_loss_exponent)
print("Received Power Values (dBm):", received_unknown_dBm_values)
print("Actual Distances (meters):", actual_distances)
print("Absolute Errors (meters):", absolute_errors)
print("Average Distance Error (meters):", average_error)


'''
Step-2(b):-

Due to the presence of noise, errors may occur in estimating the range or distance. To quantify these errors, I am calculating the discrepancy between
the estimated and actual distances for 6 different scenarios. Finally, reporting the average error across these experiments.

'''