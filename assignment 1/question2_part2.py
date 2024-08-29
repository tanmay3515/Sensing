
import numpy as np
import random

# manually inserted Signal arrival time of each satellites
signal_arrival_times =[3.162277660168379e-07, 1.201850425154663e-06, 8.376554582086042e-07, 2.1937410968480306e-06, 5.678908345800274e-07]
def Mutual_Distance(Tim):
# speed of light as 300000000m/s
    Dist = (Tim)* 300000000
    return Dist

# Assigning coordinates of the satellites manually 
x1, y1, z1 = 60, 30, 50
x2, y2, z2 = 300, 400, 100
x3, y3, z3 = -150, 95, 75
x4, y4, z4 = 700, -50, -125
x5, y5, z5 = 260, 120, 45

# Calculating distance of user and satellites using Mutual_Distance function and assigning them
r1 = Mutual_Distance(signal_arrival_times[0])
r2 = Mutual_Distance(signal_arrival_times[1])
r3 = Mutual_Distance(signal_arrival_times[2])
r4 = Mutual_Distance(signal_arrival_times[3])
r5 = Mutual_Distance(signal_arrival_times[4])

# Create the matrix A
A = np.array([
    [2*(x2-x1), 2*(y2-y1), 2*(z2-z1)],
    [2*(x3-x2), 2*(y3-y2), 2*(z3-z2)],
    [2*(x4-x3), 2*(y4-y3), 2*(z4-z3)],
    [2*(x5-x4), 2*(y5-y4), 2*(z5-z4)]
])

# Create the vector b
b = np.array([[(r1**2 - r2**2) - (x1**2 - x2**2) - (y1**2 - y2**2) - (z1**2 - z2**2)],
              [(r2**2 - r3**2) - (x2**2 - x3**2) - (y2**2 - y3**2) - (z2**2 - z3**2)],
              [(r3**2 - r4**2) - (x3**2 - x4**2) - (y3**2 - y4**2) - (z3**2 - z4**2)],
              [(r4**2 - r5**2) - (x4**2 - x5**2) - (y4**2 - y5**2) - (z4**2 - z5**2)]
             ])

# Printing matrix A and Vector b
print("Matrix A:")
print(A)

print("Vector b:")
print(b)
# Calculate the solution using matrix inverse
user_pos = np.linalg.solve(A.T @ A, A.T @ b)

print("User's Position :")
print(user_pos)

'''
 Mutual_Distance function calculates the distance that a signal travels based on the time 
 it took for the signal to arrive. The speed of light is considered as 300000000 meters per 
 second.
 Tim is the Time taken for the signal to arrive.
 Dist is Calculated distance traveled by the signal.
 Our function multiplies the input Tim with the speed of light (300000000) to obtain the
 distance that the signal has traveled. This distance is returned as the output.

 For differences in coordinates between consecutive satellites we created a Matrix A. Each 
 row of the matrix represents the differences in x, y, and z coordinates for two successive 
 satellites. For instance, the row [2*(x2-x1), 2*(y2-y1), 2*(z2-z1)] captures the differences
 between satellite 2 and satellite 1 in the x, y, and z dimensions, respectively.
 After That constructs a vector b using the differences in squared distances between consecutive 
 satellites and the differences in coordinates. Each element of the vector b represents the
 difference between the squared distances (ranging from r1 to r5) and the differences in squared 
 coordinates (x, y, z) between successive satellites. This equation embodies the concept of 
 trilateration
 The user's position is estimated by solving the system of equations represented by matrix A and 
 vector b. This is done by calculating the dot product of the transpose of matrix A and matrix A,
 as well as the dot product of the transpose of matrix A and vector b. The resulting matrices are
 used to compute the estimated user's position.
'''