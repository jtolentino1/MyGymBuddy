import json
import Curls
import Squats

def main(arr):
    for i in arr:
        if i == 'Bicep Curl':
            Curls.main()
        elif i == 'Extensions':
            Squats.main()
        elif i == 'Squats':
            Squats.main()
