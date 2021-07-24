import os 
import glob
import re
import argparse
import cv2 
import shutil
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--root_path', '-rp', type=str,
                                    help="path to root folder which contains seq folder")
parser.add_argument('--gt_path', '-gt', type=str, 
                                    help="path to groundtruth file")

#parser.add_argument('--img_sz', '-s', type=str, nargs="+", help="image resolution (w, h")
args = parser.parse_args()

def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def create_img1_folder(seq):
    imgs = glob.glob(seq + "/*.jpg")
    img1 = os.path.join(seq, "img1")
    seq_length = len(imgs)
    create_folder(img1)

    # check img size 
    img_mat = cv2.imread(imgs[0])
    h, w = img_mat.shape[:2]

    for img in imgs:
        shutil.move(img, img1)

    return seq_length, w, h

def create_seqinfo(cur_path, **kwargs):
    with open(os.path.join(cur_path, "seqinfo.ini"), "w") as f:
        f.write("[Sequence]\n")
        for k, v in kwargs.items():
            f.write("{}={}".format(k, v) + "\n")

def create_gt(src, dst):
    create_folder(dst)
    dst = os.path.join(dst, "gt.txt")
    shutil.copyfile(src, dst)

seqinfo_dict = {"name": "",
                "imDir": "",
                "frameRate": 10,
                "seqLength": 0,
                "imWidth": 1920,
                "imHeight": 1080,
                "imExt": ".jpg"}

seqs = glob.glob(args.root_path + "/*")
for seq in seqs:
    # create img1 files
    #seq_length, w, h = create_img1_folder(seq)
    name = seq.split("/")[-1]
    
    # create seqinfo.ini file
    #tmp = seqinfo_dict.copy()
    #tmp["seqLength"] = seq_length
    #tmp["imWidth"] = w
    #tmp["imHeight"] = h
    #tmp["imDir"] = "img1"
    #tmp["name"] = name
    #create_seqinfo(seq, **tmp)
    #print("Finish ", seq)
    
    # create gt folder
    gt_save = os.path.join(seq, "gt")
    gt_copy_from = os.path.join(args.gt_path, name, "gt/gt.txt")
    create_gt(gt_copy_from, gt_save)
    
    # create det folder
    create_folder(os.path.join(seq, "det"))


    
