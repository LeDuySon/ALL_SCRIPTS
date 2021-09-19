import cv2
import numpy as np
import argparse
import os
import re
import glob
from collections import defaultdict
from vehicle import Vehicle

def get_video_path(text_path, root_path):
  """Convert ground truth file name to video path

  Args:
      text_path ([str]): path to gt file, format: {camera_day_hour_minute}
      root_path ([str]): root path of folder contain all videos
  """

  name = text_path.split("/")[-1].split(".")[0] # asdsad/text_name.txt
  camera, _, hour, minute = name.split("_")
  day_pattern = r"([0-9]{4})([0-9]{2})([0-9]{2})"
  tmp = re.search(day_pattern, _)
  day = "-".join(tmp.groups()) # 20180315 -> 2018-03-15

  return os.path.join(root_path, camera, day, hour, minute + ".mp4")

def video2image(video_path, save_path):
  """Generate image from video

  Args:
      video_path ([type]): path to videooooooooo
      save_path ([type]): path to folder contain image after generate
  """
  print(video_path)
  vidcap = cv2.VideoCapture(video_path)
  success, image = vidcap.read()
  fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
  print("Frame rate: ", fps)

  video_name = "_".join(video_path.split("/")[-4:]).split(".")[0]
  img_size = None
  print(video_name)
  #################### Initiate Process ################
  while success:
    #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
      frameId = int(round(vidcap.get(1))) - 1 
      success, image = vidcap.read()

      if(success):
        if(img_size is None):
          img_size = image.shape
        num_zeros = 6 - len(str(frameId))
        save_img_name = video_name + "_" + "0" * num_zeros + str(frameId) + ".jpg" # frame name format: frame_xxxxxx.jpg
        print(save_img_name)
        save_file = os.path.join(save_path, save_img_name)
        cv2.imwrite("%s" % save_file, image)
      else:
        print("Frame {} invalid".format(frameId))
          
  vidcap.release()
  # return video name for generate groundtruth
  return video_name, img_size


def get_obj_per_frame(file):
  with open(file, "rt") as f:
    lines = f.readlines() 
  # frame, track_id, coord, class_type, lost, occluded, generated -> i[5], i[0], i[1:5], i[9:], i[6], i[7], i[8]
  lines = list(map(lambda x:x.strip().split(" "), lines))
  objs = []
  for i in lines:
    objs.append(Vehicle(i[5], i[0], i[1:5], i[9:], i[6], i[7], i[8]))

  group_frame = defaultdict(list)
  for obj in objs:
      group_frame[obj.frame].append(obj)
  return group_frame

def create_gt(file, save_name, save_path, img_size):
  """[summary]

  Args:
      file ([type]): groundtruth file
      save_name ([type]): base name of video respect to our groundtruth
      save_path ([type]): path to folder 
      img_size: resolution of our video
  """
  group_frame = get_obj_per_frame(file)

  save_format = "{class_idx} {x_center} {y_center} {w} {h}\n"
  for idx in range(len(group_frame.keys())):
      file_name = save_name + "_" + "0" * (6 - len(str(idx))) + str(idx) + ".txt"
      with open(os.path.join(save_path, file_name), "w") as f:
          for obj in group_frame[idx]:
            if obj.lost:
              continue 
            class_idx = obj.class2idx() 
            if(class_idx is None):
              continue 
            x_center, y_center, w, h = obj.convert2yolo(img_size)
            line = save_format.format(class_idx=class_idx, x_center=x_center, y_center=y_center, w=w, h=h)
            f.write(line)

def run(args):
  gt_files = glob.glob(args.gt_path + "/*.txt")
  print(gt_files)
  for file in gt_files:
    video = get_video_path(file, args.video_path)
    video_name, img_size = video2image(video, args.save_path)

    save_gt_path = args.save_path.replace("images", "labels")
    create_gt(file, video_name, save_gt_path, img_size)



if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('--gt_path', '-V', type=str,
                      help='folder contains all groundtruth files, from gt files name -> find videos')
  parser.add_argument('--video_path', '-vp', type=str,
                      help="folder contains all videos")
  parser.add_argument('--save_path', '-sp', type=str, 
                      help="save frame video path")
  #parser.add_argument('--mode', type=str, help="train or test")
  args = parser.parse_args()

  run(args)
