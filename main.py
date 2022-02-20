import json
import Curls
import Squats
import Extensions
import Crunches
import Rows
import BenchPress

def start(arr):
    for i in arr:
        if i == 'Bicep Curl':
            reps = int(arr['Bicep Curl']['reps'])
            sets = int(arr['Bicep Curl']['sets'])
            Curls.start(sets,reps)
        elif i == 'Extensions':
            reps = int(arr['Extensions']['reps'])
            sets = int(arr['Extensions']['sets'])
            Extensions.start(sets, reps)
        elif i == 'Squats':
            reps = int(arr['Squats']['reps'])
            sets = int(arr['Squats']['sets'])
            Squats.start(sets,reps)
        elif i == 'Crunches':
            reps = int(arr['Crunches']['reps'])
            sets = int(arr['Crunches']['sets'])
            Crunches.start(sets, reps)
        elif i == 'Rows':
            reps = int(arr['Rows']['reps'])
            sets = int(arr['Rows']['sets'])
            Rows.start(sets,reps)
        elif i == 'Benchpress':
            reps = int(arr['Benchpress']['reps'])
            sets = int(arr['Benchpress']['sets'])
            BenchPress.start(sets,reps)
