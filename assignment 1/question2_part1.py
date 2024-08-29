# User's position
user_position = (100, 100, 100)

# Satellite positions (x, y, z)
satellite_positions = [
  (60, 30, 50),
(300, 400, 100),
(-150, 95, 75),
(700, -50, -125),
(260, 120, 45)
]

# Speed of light in meters per second
speed_of_light = 300000000  # meters/second

# Calculate signal propagation time for each satellite
signal_times = []
for sat_pos in satellite_positions:
    distance = ((user_position[0] - sat_pos[0]) ** 2 +
               (user_position[1] - sat_pos[1]) ** 2 +
               (user_position[2] - sat_pos[2]) ** 2)**0.5
    # signal propogation
    signal_time = distance / speed_of_light
    # Appending signal time to the list
    signal_times.append(signal_time)

# Print signal times
for i, time in enumerate(signal_times):
    print(f"Signal time for satellite {i+1}: {time:.10f} seconds")


    '''
    Report :-
    
    Our main objective is to calculate the signal propagation times for a user's position in relation to a
    predefined list of satellite positions. By estimating the time it takes for signals to travel between
    these points.
    
    - The user's position is set at coordinates (100, 100, 100), and the positions of five satellites are 
    provided in the satellite_positions list manually.
    - The code iterates through each satellite position and calculates the distance between the 
    user and the satellite using basic distance formula. This distance is then divided by the speed of light
    to determine the signal propagation time for each satellite.(we have taken speed of light as 3*10^8 
    meter/seconds)
    - The calculated signal propagation times are collected in the signal_times list.
    - The code's output provides the signal propagation times for each satellite in seconds
    '''
    
