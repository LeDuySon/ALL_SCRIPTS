import cv2
import math
import numpy as np
import argparse
import os
from del_noobj_frame import get_frame_have_objects
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_path', '-V', type=str,
                    help='video path to extract frame')
parser.add_argument('--save_path', '-sp', type=str, 
                    help="save frame video path")
parser.add_argument('--frame_interval', '-fi', type=int,
                    help="only save frame if frame index % frame_interval == 0", default=1)

# this arg decides whether or not save frame that dont have any object in it. 
# Train mode: not save frame cuz it will not find txt file for this frame -> error when training
# test mode: save frame to calculate framerate exactly
#parser.add_argument('--mode', type=str, help="train or test")


args = parser.parse_args()

videoFile = args.video_path
vidcap = cv2.VideoCapture(videoFile)
success, image = vidcap.read()

#################### Setting up parameters ################

seconds = 5
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
print("Frame rate: ", fps)

if(not os.path.exists(args.save_path)):
    os.mkdir(args.save_path)

tmp_name = args.video_path.split("/")
cat_name = "/".join(tmp_name[-2:])[:-4]
#label_path = "/mnt/1T/TRAIN_DATASET/fairmot_dataset/UET_MOT/labels_with_ids/{}/img1".format(cat_name)

#valid_frames = get_frame_have_objects(label_path)
#################### Initiate Process ################
while success:
    frameId = int(round(vidcap.get(1))) - 1 #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    if(frameId % 1000 == 0):
        print(frameId)
    print(frameId)
    success, image = vidcap.read()
    num_zeros = 6 - len(str(frameId))
    save_img_name = "frame_" + "0" * num_zeros + str(frameId) + ".jpg" # frame name format: frame_xxxxxx.jpg
    save_name = save_img_name.split(".")[0]
 #   if(save_name not in valid_frames and args.mode == "train"):
 #       continue    
    save_file = os.path.join(args.save_path, save_img_name)
    if(frameId % args.frame_interval == 0):
        cv2.imwrite("%s" % save_file, image)
        
vidcap.release()
print("Complete")
