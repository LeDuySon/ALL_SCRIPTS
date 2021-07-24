
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--target_path', '-V', type=str,
                    help='video path to extract frame')

args = parser.parse_args()

frame_count = 0

files = os.listdir(args.target_path)
while frame_count <= 19199:
    num_zeros = 6 - len(str(frame_count))
    save_name ="frame_"+  "0" * num_zeros + str(frame_count) + ".txt"
    save_file = os.path.join(args.target_path, save_name)
    if(save_name not in files):
        with open(save_file, "wt") as f:
            f.write("")
    frame_count += 1
    

    
