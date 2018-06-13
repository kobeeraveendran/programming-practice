import numpy as np

def launchSequenceChecker(systemNames, stepNumbers):
    unique_systems = {}

    for i in range(len(systemNames)):
        if systemNames[i] in unique_systems:
            unique_systems[systemNames[i]].append(stepNumbers[i])
        else:
            unique_systems[systemNames[i]] = [stepNumbers[i]]
        
    for key in unique_systems:
        if not is_ascending(unique_systems[key]):
            return False

    return True

def is_ascending(launch_sequence):
    if len(set(launch_sequence)) != len(launch_sequence):
        return False
    
    launch_sorted = sorted(launch_sequence)

    for i in range(len(launch_sequence)):
        if launch_sequence[i] != launch_sorted[i]:
            return False

    return True

test1_names = ['stage_1', 'stage_2', 'dragon', 'stage_1', 'stage_2', 'dragon']
test1_steps = [1, 10, 11, 2, 12, 111]

print(launchSequenceChecker(test1_names, test1_steps))