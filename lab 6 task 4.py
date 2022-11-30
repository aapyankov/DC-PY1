import json

INPUT_FILE = "input_1.csv"

def csv_to_list_dict(file_name) -> list[dict]:
       with open(file_name, 'r') as f:
        headers = f.readline().split(",")
        title = [element.rstrip() for element in headers]
        list_dict = []
        for line in f:
            line = line.split(',')
            line = [element.rstrip() for element in line]
            line = dict(zip(title, line))
            list_dict.append(line)
        return list_dict
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
