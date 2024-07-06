from ParseData import parse_json
import json
import os
import matplotlib.pyplot as plt
import numpy as np

folder_path = '../data/'
json_files = [pos_json for pos_json in os.listdir(folder_path) if pos_json.endswith('.json')]

parsed_files = []
for i in range(len(json_files)):
    with open(folder_path + json_files[i], 'r') as f:
        print(f"Read file : {json_files[i]}")
        data = json.loads(f.read())
        parsed_data = parse_json(data)

        print(f"Frame Count : {len(parsed_data)}")
        parsed_files.append(parsed_data)
print(parsed_files[1][0].instances[0].bbox)

def frequency_table(instance):
    figure_count = []
    for i in instance:
        figure_count.append(len(i.instances))

    figure_max = max(figure_count)

    counter = np.zeros(figure_max+1)
    for i in range(figure_max+1):
        counter[i] = figure_count.count(i)
    return counter

def body_length_graph(instance):

    return 0


## run frequency table graph
for i in range(len(parsed_files)):
    body_lengh = body_length_graph(parsed_files[i])
    # person_count = frequency_table(parsed_files[i])

    # plt.figure(figsize=(12, 6))
    # plt.barh(np.arange(len(person_count)), person_count)

    # for index, value in enumerate(person_count):
    #     plt.text(value, index, str(value))
    # plt.title(f"Frequency table of Identified Skeletons : {json_files[i]}")
    # plt.show()


