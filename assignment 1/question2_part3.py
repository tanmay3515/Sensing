import numpy as np
import random

# signal arrival times of each satellite 
time_of_flights =([3.162277660168379e-07, 1.201850425154663e-06, 8.376554582086042e-07, 2.1937410968480306e-06, 5.678908345800274e-07])
def Mutual_Distance_Witherror(Tim):

    err_strt =1e-09
    err_end =1e-08
    errror =random.uniform(err_strt,err_end)
    Dist = (Tim + errror)* 300000000
    return Dist
#  speed of light as 300000000 m/s 



x1, y1, z1 = 60, 30, 50
x2, y2, z2 = 300, 400, 100
x3, y3, z3 = -150, 95, 75
x4, y4, z4 = 700, -50, -125
x5, y5, z5 = 260, 120, 45

r2 = Mutual_Distance_Witherror(time_of_flights[1])
r3 = Mutual_Distance_Witherror(time_of_flights[2])
r4 = Mutual_Distance_Witherror(time_of_flights[3])
r5 = Mutual_Distance_Witherror(time_of_flights[4])
r1 = Mutual_Distance_Witherror(time_of_flights[0])

# Create the matrix A
A = np.array([
    [2*(x2-x1), 2*(y2-y1), 2*(z2-z1)],
    [2*(x3-x2), 2*(y3-y2), 2*(z3-z2)],
    [2*(x4-x3), 2*(y4-y3), 2*(z4-z3)],
    [2*(x5-x4), 2*(y5-y4), 2*(z5-z4)]
])

# Create the vector b
b = np.array([
    [(r1**2 - r2**2) - (x1**2 - x2**2) - (y1**2 - y2**2) - (z1**2 - z2**2)],
    [(r2**2 - r3**2) - (x2**2 - x3**2) - (y2**2 - y3**2) - (z2**2 - z3**2)],
    [(r3**2 - r4**2) - (x3**2 - x4**2) - (y3**2 - y4**2) - (z3**2 - z4**2)],
    [(r4**2 - r5**2) - (x4**2 - x5**2) - (y4**2 - y5**2) - (z4**2 - z5**2)]
])

print("Matrix A :")
print(A)

print("Vector b :")
print(b)
# Calculate the solution using matrix inverse
user_pos = np.linalg.solve(A.T @ A, A.T @ b)

print("User's Position :")
print(user_pos)


'''
Mutual_Distance_Witherror(Tim): This function calculates the distance traveled by a signal while
introducing a simulated error in signal arrival times. The error range is defined from err_strt (1e-09)
to err_end (1e-08).
provided Input: Tim which is Signal arrival time.
Output Given: Dist which is Calculated distance traveled by the signal with simulated error.

Basically our function adds a random error in the specified range to the input signal arrival time. It 
then multiplies the resulting time with the speed of light to calculate the distance traveled by the signal. 
The distance with error is returned as the output.

:- defined signal arrival times (time_of_flights) and satellite coordinates.
:- Distance Calculation with Error: The distances (r1 to r5) between the user and each satellite are calculated
using the Mutual_Distance_Witherror function, which accounts for signal arrival time errors.
:- Similar to the previous Question 2 part 2, the matrix A captures differences in coordinates between consecutive
satellites.
:- The vector b is constructed using differences in squared distances and coordinates, accounting for the squared 
signal arrival time errors and squared coordinate differences.
:- The user's position is estimated by solving the system of equations represented by matrix A and vector b, just as 
in the previous program's code.
:- The matrix A and vector b are displayed to showcase their contents. The estimated user's position is then printed.

'''