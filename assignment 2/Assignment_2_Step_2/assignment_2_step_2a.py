import numpy as np

path_loss_exponent = 1.91 # Path loss exponent which i got from step 1
reference_distance = 1.0   # Assuming Reference distance to be 1 m 
received_reference_dBm = -42.0  # Received power at reference distance in dBm
received_unknown_dBm = -88.0  # Received power at an unknown distance in dBm

# Estimate the distance (d) from received power (Pr_dBm) and path loss exponent (n)
estimated_distance_meters = reference_distance * 10**((received_reference_dBm - received_unknown_dBm) / (10 * path_loss_exponent))

# Print the estimated distance
print(f"Estimated distance: {estimated_distance_meters:.2f} meters")


'''
Step-2(a):-

:- Basically This code calculates the estimated distance (estimated_distance_meters) between the transmitter and receiver using the path loss formula:
:- After importing numpy I have defined the parameterrs and then estimated the distance in meters using the formula

'''