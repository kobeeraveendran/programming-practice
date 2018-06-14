import numpy as np
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    return np.add((ride_time * np.array(cost_per_minute)), (ride_distance * np.array(cost_per_mile)))