import json
import Curls
import Squats
import Extensions

def start(arr):
    for i in arr:
        if i == 'Bicep Curl':
            reps = int(arr['Bicep Curl']['reps'])
            print(reps)
            Curls.start(reps)
        elif i == 'Extensions':
            reps = int(arr['Extensions']['reps'])
            Extensions.start(reps)
        elif i == 'Squats':
            reps = int(arr['Squats']['reps'])
            Squats.start(reps)
