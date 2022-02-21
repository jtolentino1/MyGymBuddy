import json
import Exercises.Curls
import Exercises.Squats
import Exercises.Extensions
import Exercises.Crunches
import Exercises.Rows
import Exercises.BenchPress

def start(arr):
    for i in arr:
        if i == 'Bicep Curl':
            reps = int(arr['Bicep Curl']['reps'])
            sets = int(arr['Bicep Curl']['sets'])
            Exercises.Curls.start(sets,reps)
        elif i == 'Extensions':
            reps = int(arr['Extensions']['reps'])
            sets = int(arr['Extensions']['sets'])
            Exercises.Extensions.start(sets, reps)
        elif i == 'Squats':
            reps = int(arr['Squats']['reps'])
            sets = int(arr['Squats']['sets'])
            Exercises.Squats.start(sets,reps)
        elif i == 'Crunches':
            reps = int(arr['Crunches']['reps'])
            sets = int(arr['Crunches']['sets'])
            Exercises.Crunches.start(sets, reps)
        elif i == 'Rows':
            reps = int(arr['Rows']['reps'])
            sets = int(arr['Rows']['sets'])
            Exercises.Rows.start(sets,reps)
        elif i == 'Benchpress':
            reps = int(arr['Benchpress']['reps'])
            sets = int(arr['Benchpress']['sets'])
            Exercises.BenchPress.start(sets,reps)