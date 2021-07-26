import os 


def get_frame_have_objects(label_path):
    label_files = os.listdir(label_path)
    
    label_names = list(map(lambda x: x.split(".")[0], label_files))
    
    return label_names
    #print(label_names[:5])



