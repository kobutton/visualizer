from flask import (Flask, render_template)
import requests
import itertools
import os
    

app = Flask(__name__)

@app.route('/')
def root_path():
    random_numbers = requests.get(os.getenv("RANDONET_SERVICE_URL"), verify=False).json()
    random_numbers.sort()
    total_nums = len(random_numbers)
    groupings = [(k, len(list(g))) for k, g in itertools.groupby(random_numbers, key=lambda n: n//100000)]
    groups= [f'{x*100000}\'s' for x,y in groupings]
    groups[0] = '0-99999'
    data_points=['data1']+[y for x,y in groupings]
    return render_template('randomness.html', total_nums=total_nums, groups=str(groups), data_points=data_points)