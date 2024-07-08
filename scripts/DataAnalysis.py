import json
import os
import matplotlib.pyplot as plt
import numpy as np

# process single file
def frequency_table(instance):
    figure_count = []
    for i in instance.frame_list:
        figure_count.append(len(i.instances))

    figure_max = max(figure_count)

    counter = np.zeros(figure_max+1)
    for i in range(figure_max+1):
        counter[i] = figure_count.count(i)
    return counter

def body_position_side(instance):
    position_side = []
    for i in instance.frame_list:
        for j in i.instances:
            center_x = (j.bbox[0][0] + j.bbox[0][2])/2
            if center_x >= instance.frame_size[0]/2:
                position_side.append('right')
            else:
                position_side.append('left')
    return position_side

def body_length_graph(instance):
    body_length = []
    for i in instance.frame_list:
        length_list = []
        for j in i.instances:
            length_list.append(np.abs(j.bbox[0][1] - j.bbox[0][3]))
        length_list = np.array(length_list)
        body_length.append(np.max(length_list))
    body_length = np.array(body_length)
    if instance.frame_size.shape != 0:
        body_length = body_length/ instance.frame_size[1]
    return body_length

def plot_graph_xy(list,title,x_label,y_label):
    # body_lengh = body_length_graph(instance)
    # plt.title(instance.file_name)
    plt.title(title)  
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    # plt.xlabel("frame id") 
    # plt.ylabel("body height ratio(maximum)")
    x = np.arange(0, len(list)) 
    plt.plot(x, list) 
    plt.show()

    # person_count = frequency_table(parsed_files[i])

    # plt.figure(figsize=(12, 6))
    # plt.barh(np.arange(len(person_count)), person_count)

    # for index, value in enumerate(person_count):
    #     plt.text(value, index, str(value))
    # plt.title(f"Frequency table of Identified Skeletons : {json_files[i]}")
    # plt.show()


