import json

INPUT_FILE = "input_1.csv"

def csv_to_list_dict(file_name) -> list[dict]:
       with open(file_name, 'r') as f:
        headers = f.readline()
        headers = headers.rstrip()
        title = headers.split(",") #split использую для разделения по элементам, так как в csv элементы перечислены через запятую
        list_dict = []
        for line in f:
            line = line.rstrip()
            line = line.split(",")
            line = dict(zip(title, line))
            list_dict.append(line)
        return list_dict
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
