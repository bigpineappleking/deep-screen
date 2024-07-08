import json
import os
import numpy as np

class Keypoint:
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score

class Instance:
    def __init__(self, keypoints, bbox, human_id):
        self.keypoints = keypoints
        self.bbox = bbox
        self.human_id = human_id

class FrameInstance:
    def __init__(self, frame_id, instances):
        self.frame_id = frame_id
        self.instances = instances

class VideoInstance:
    def __init__(self, file_name, frame_list, frame_size):
        self.file_name = file_name
        self.frame_list = frame_list
        self.frame_size = frame_size

def read_single_file(input_path):
    with open(input_path, 'r') as f:
        print(f"Read file : {input_path}")
        data = json.loads(f.read())
        parsed_data = parse_json(data, input_path)

        print(f"Frame Count : {len(parsed_data.frame_list)}")
    return parsed_data
        
def read_all_files(input_path):
    parsed_data_all = []
    json_files_path = [pos_json for pos_json in os.listdir(input_path) if pos_json.endswith('.json')]
    for file_path in json_files_path:
        parsed_data_all.append(read_single_file(input_path + file_path))
    return parsed_data_all

def parse_json(json_data, file_name):
    frame_size = []
    if 'video_info' in json_data:
        video_info = json_data['video_info']
        if 'video_shape' in video_info[0]:
            frame_size = video_info[0]['video_shape']
    frame_size = np.array(frame_size)

    instance_info = json_data['instance_info']
    frame_list = []

    for i in range(len(instance_info)):
        parsed_frame_id = instance_info[i]['frame_id']
        parsed_instances = instance_info[i]['instances']

        ## human_id not in every data file
        if 'human_id' in instance_info[i]:
            parsed_human_id = instance_info[i]['human_id']
        else:
            parsed_human_id = np.array([-1])

        instances = []
        for j in range(len(parsed_instances)):
            parsed_keypoints = parsed_instances[j]['keypoints']
            parsed_scores = parsed_instances[j]['keypoint_scores']
            keypoints = []
            for k in range(len(parsed_scores)):
                keypoints.append(Keypoint(np.array(parsed_keypoints[k]), parsed_scores[k]))

            ## bbox not in every data file
            if 'bbox' in parsed_instances[j]:
                parsed_bbox = parsed_instances[j]['bbox']
            else:
                parsed_bbox = []

            instances.append(Instance(keypoints, np.array(parsed_bbox), parsed_human_id[j]))

        frame_instances = FrameInstance(parsed_frame_id, instances)
        frame_list.append(frame_instances)
        video_instance = VideoInstance(file_name, frame_list, frame_size)
    return video_instance



# with open('../results_Fred_short_Gaussian2DSigma1_bboxthr0.6_no3Dfilter.json', 'r') as f:
#     data = f.read()

# parsed_data = json.loads(data)
# frame_list = parse_json(parsed_data)

# print(f"File name : updated_rain_centerBbox_23DSmooth.json")
# print(f"Frame Count : {len(frame_list)}")