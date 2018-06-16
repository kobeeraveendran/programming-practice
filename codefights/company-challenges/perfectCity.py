import math
def perfectCity(departure, destination):
    path_length = 0
    nearest_start_x = math.ceil(departure[0]) if departure[0] < destination[0] else math.floor(departure[0])
    nearest_start_y = math.ceil(departure[1]) if departure[1] < destination[1] else math.floor(departure[1])
    nearest_end_x = math.floor(destination[0]) if destination[0] > nearest_start_x else math.ceil(destination[0])
    nearest_end_y = math.floor(destination[1]) if destination[1] > nearest_start_y else math.ceil(destination[1])
    
    delta_x_start = abs(nearest_start_x - departure[0])
    delta_y_start = abs(nearest_start_y - departure[1])
    delta_x_end = abs(nearest_end_x - destination[0])
    delta_y_end = abs(nearest_end_y - destination[1])

    euclidian_distance = abs(nearest_end_x - nearest_start_x) + abs(nearest_end_y - nearest_start_y)

    path_length = delta_x_start + delta_y_start + delta_x_end + delta_y_end + euclidian_distance

    return path_length

# should be 2.7
print(perfectCity([0.4, 1], [0.9, 3]))
# should be 7.7 was 8.3
print(perfectCity([0, 0.2], [7, 0.5]))