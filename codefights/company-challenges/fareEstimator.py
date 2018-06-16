import numpy as np
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    return np.add((ride_time * np.array(cost_per_minute)), (ride_distance * np.array(cost_per_mile)))

# test 1
print(fareEstimator(30, 7, [0.2, 0.35, 0.4, 0.45], [1.1, 1.8, 2.3, 3.5]))