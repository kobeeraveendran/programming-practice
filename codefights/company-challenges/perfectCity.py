import math
def perfectCity(departure, destination):
    path_length = 0
    nearest_start_x = math.ceil(departure[0]) if departure[0] < destination[0] else math.floor(departure[0])
    nearest_start_y = math.ceil(departure[1]) if departure[1] < destination[1] else math.floor(departure[1])
    nearest_end_x = math.ceil(destination[0]) if destination[0] > departure[0] else math.floor(destination[0])
    nearest_end_y = math.ceil(destination[1]) if destination[1] > departure[1] else math.floor(destination[1])

    delta_x_start = abs(nearest_start_x - departure[0])
    delta_y_start = abs(nearest_start_y - departure[1])
    delta_x_end = abs(nearest_end_x - destination[0])
    delta_y_end = abs(nearest_end_y - destination[1])

    euclidian_distance = abs(nearest_end_x - nearest_start_x) + abs(nearest_end_y - nearest_start_y)

    #print(nearest_start_x, nearest_start_y)
    #print(nearest_end_x, nearest_end_y)
    #print(euclidian_distance)

    path_length = delta_x_start + delta_y_start + delta_x_end + delta_y_end + euclidian_distance

    return path_length

# should be 2.7
print(perfectCity([0.4, 1], [0.9, 3]))
print(perfectCity([0.5, 0.5], [1.5, 1.5]))