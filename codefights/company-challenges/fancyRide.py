def fancyRide(l, fares):
    car_choices = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]

    for i in range(len(fares)):
        if l * fares[i] > 20:
            return car_choices[i - 1]
    
    return car_choices[-1]