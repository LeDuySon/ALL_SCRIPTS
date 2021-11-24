import sys 
sys.path.append("../")
from utils import xyxy2yolo

class Vehicle():
  def __init__(self, frame, track_id, coord, class_type, lost, occluded, generated): # i[5], i[0], i[1:5], i[-1], i[6], i[7], i[8]
    self.coord = list(map(int, coord))
    self.type = " ".join(class_type).replace('"', '')
    self.frame = int(frame)
    self.track_id = int(track_id)
    self.lost = int(lost)
    self.occluded = int(occluded)
    self.generated = int(generated)
    self.class_dict = {"Truck": 0, "Bus": 1, "Car": 2, "Motorbike": 3, "Bicycle": 3, "Container": 4}

  def convert2yolo(self, img_size):
    return xyxy2yolo(self.coord, img_size)
  def class2idx(self):
    class_name = self.type.split(" ")[0]
    if(class_name in self.class_dict.keys()):
        return self.class_dict[class_name]
    return None
