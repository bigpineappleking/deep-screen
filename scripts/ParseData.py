import json
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
        

def parse_json(json_data):
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
    return frame_list



# with open('../results_Fred_short_Gaussian2DSigma1_bboxthr0.6_no3Dfilter.json', 'r') as f:
#     data = f.read()

# parsed_data = json.loads(data)
# frame_list = parse_json(parsed_data)

# print(f"File name : updated_rain_centerBbox_23DSmooth.json")
# print(f"Frame Count : {len(frame_list)}")