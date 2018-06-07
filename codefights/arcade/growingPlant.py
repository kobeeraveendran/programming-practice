def growingPlant(upSpeed, downSpeed, desiredHeight):
    plant_height = 0
    days = 0

    while plant_height < desiredHeight:
        plant_height += upSpeed
        days += 1
        if plant_height >= desiredHeight:
            return days
        plant_height -= downSpeed