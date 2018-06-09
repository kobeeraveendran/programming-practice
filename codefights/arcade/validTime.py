def validTime(time):
    time = time.split(':')
    hours = time[0]
    mins = time[1]

    return 0 <= int(hours) <= 23 and 0 <= int(mins) <= 59