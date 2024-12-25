# TODO решите задачу
import json
import pprint
def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
    sum = 0
    for l in data:
        a = l['score']*l['weight']
        sum += a
    return(round(sum,3))

print(task())
