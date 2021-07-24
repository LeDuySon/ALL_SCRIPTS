import cv2
import math
import numpy as np
import argparse
import os
# Make sure that the print function works on Python 2 and 3
#from del_noobj_frame import get_frame_have_objects
# Capture every n seconds (here, n = 5) 
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_path', '-V', type=str,
                    help='video path to extract frame')
parser.add_argument('--save_path', '-sp', type=str, 
                    help="save frame video path")


args = parser.parse_args()

#################### Setting up the file ################
videoFile = args.video_path
vidcap = cv2.VideoCapture(videoFile)
success, image = vidcap.read()

#################### Setting up parameters ################

seconds = 5
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
print("Frame rate: ", fps)

if(not os.path.exists(args.save_path)):
    os.mkdir(args.save_path)
#valid_frames = get_frame_have_objects()
#################### Initiate Process ################
while success:
    frameId = int(round(vidcap.get(1))) - 1 #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    if(frameId % 1000 == 0):
        print(frameId)
    print(frameId)
    success, image = vidcap.read()
    num_zeros = 6 - len(str(frameId))
    save_img_name = "frame_" + "0" * num_zeros + str(frameId) + ".jpg"
    save_name = save_img_name.split(".")[0]
    #if(save_name not in valid_frames):
    #    continue    
    save_file = os.path.join(args.save_path, save_img_name)
    cv2.imwrite("%s" % save_file, image)
        
vidcap.release()
print("Complete")
