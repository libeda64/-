# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    with open('input.csv', 'r') as f:
        dict_reader = csv.DictReader(f)
        headers = dict_reader.fieldnames
        list = []
        for line in dict_reader:
            data = {}
            for h in headers:
                data[h] = line[h]
            list.append(data)
        s = json.dumps(list, indent=4, sort_keys=False)
        print(s)

if __name__ == '__main__':
    task()
