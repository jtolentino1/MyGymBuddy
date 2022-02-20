import json
import Curls
import Squats

def main(arr):
    for i in arr:
        if i == 'Bicep Curl':
            reps = arr['Bicep Curl']['reps']
            Curls.start(reps)
        elif i == 'Extensions':
            reps = arr['Bicep Curl']['reps']
            Squats.start(reps)
        elif i == 'Squats':
            reps = arr['Bicep Curl']['reps']
            Squats.start(reps)
