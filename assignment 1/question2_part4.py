import numpy as np
import random
import matplotlib.pyplot as plt

time_of_flights =([3.162277660168379e-07, 1.201850425154663e-06, 8.376554582086042e-07, 2.1937410968480306e-06, 5.678908345800274e-07])
def euclidean_distance(n, error_factor):
    # Calculate error bounds based on the given error factor
    err_strt  = 1e-09
    err_end = 1e-08
    reg = 50
    random.seed(reg)
    # Introduce a random error within the calculated bounds
    errror = random.uniform(err_strt , err_end)
    d = (n + errror* error_factor) * 300000000
    return d

# Calculation Euclidian Distance
def distance_error(vector1, vector2):
    distance = np.linalg.norm(vector2 - vector1)
    return distance


# known points Coordinates
x1, y1, z1 = 60, 30, 50
x2, y2, z2 = 300, 400, 100
x3, y3, z3 = -150, 95, 75
x4, y4, z4 = 700, -50, -125
x5, y5, z5 = 260, 120, 45


# Vary the error factor from 1 to 10
error_factors = np.linspace(1, 10, 11)
avg_errors = []

# Loop through different error factors
for error_factor in error_factors:
    # Calculate distances with introduced errors
    r1 = euclidean_distance(time_of_flights[0], error_factor)
    r2 = euclidean_distance(time_of_flights[1], error_factor)
    r3 = euclidean_distance(time_of_flights[2], error_factor)
    r4 = euclidean_distance(time_of_flights[3], error_factor)
    r5 = euclidean_distance(time_of_flights[4], error_factor)

    # Create the matrix A for trilateration
    A = np.array([
        [2*(x2-x1), 2*(y2-y1), 2*(z2-z1)],
        [2*(x3-x2), 2*(y3-y2), 2*(z3-z2)],
        [2*(x4-x3), 2*(y4-y3), 2*(z4-z3)],
        [2*(x5-x4), 2*(y5-y4), 2*(z5-z4)]
    ])

    # Create the vector b for trilateration
    b = np.array([
        [r1**2 - r2**2 + x2**2 - x1**2 + y2**2 - y1**2 + z2**2 - z1**2],
        [r2**2 - r3**2 + x3**2 - x2**2 + y3**2 - y2**2 + z3**2 - z2**2],
        [r3**2 - r4**2 + x4**2 - x3**2 + y4**2 - y3**2 + z4**2 - z3**2],
        [r4**2 - r5**2 + x5**2 - x4**2 + y5**2 - y4**2 + z5**2 - z4**2]
    ])

    # Calculate the solution using matrix inverse for comparison
    solution = (100,100,100)
    solution2 = np.linalg.solve(A.T @ A, A.T @ b)

    # Calculate and store the distance error
    error = distance_error(solution, solution2)
    avg_errors.append(error)

# Plotting the results
plt.plot(error_factors, avg_errors, marker='o')
plt.xlabel('Average Timing Error')
plt.ylabel('Average Localization Error')
plt.title('Effect of Timing Errors on Localization Error')
plt.grid()
plt.show()

'''
The Function euclidean_distance(n, error_factor) calculates the Euclidean distance for 
signal arrival times while introducing timing errors. The error factor ranges from 1 to 
10. It generates a random error within defined bounds (err_strt and err_end), multiplies 
it by the error factor, and calculates the distance.
distance_error(vector1, vector2) This function calculates the Euclidean distance between 
two vectors using the np.linalg.norm() function from the NumPy library.


Initially we are provided with the satellite coordinates.
:- Varying Error Factors and Calculating Errors: The code varies the error factor from 1 to 
10 and calculates the average errors for each factor. The loop simulates errors, calculates 
distances, and constructs the matrix A and vector b for trilateration.
:- Comparison Solution: The code calculates the solution using a manually specified user position. 
It then calculates another solution using the matrix inverse for comparison purposes.
:- Calculating Distance Errors: The code calculates and stores the distance error between 
the manually specified solution and the matrix-inverse solution.

:- At Last Plotting the Results:
The code utilizes the matplotlib.pyplot library to plot the effect of timing errors on localization
error. The error factors are plotted on the x-axis, and the distance errors are plotted on the y-axis.
'''