import os
import numpy as np
import json
import cv2
import argparse


# Use the same script for MOT16


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="argument")
    parser.add_argument("--data_path", type=str, help="path to folder contain dataset", default="BYTETRACK_VTX")
    args = parser.parse_args()

    DATA_PATH = args.data_path
    OUT_PATH = os.path.join(DATA_PATH, 'annotations')
    SPLITS = ['val', 'test', 'train']  

    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)

    for split in SPLITS:
        if split == "test":
            data_path = os.path.join(DATA_PATH, 'test')
        elif split == "val":
            data_path = os.path.join(DATA_PATH, 'val')
        else:
            data_path = os.path.join(DATA_PATH, 'train')
        if not os.path.exists(data_path):
            print(f"{data_path} not existed")
            continue

        out_path = os.path.join(OUT_PATH, '{}.json'.format(split))
        out = {'images': [], 'annotations': [], 'videos': [],
               'categories': [{'id': 1, 'name': 'pedestrian'}]}
        seqs = os.listdir(data_path)
        image_cnt = 0
        ann_cnt = 0
        video_cnt = 0
        tid_curr = 0
        tid_last = -1
        for seq in sorted(seqs):
            video_cnt += 1  # video sequence number.
            out['videos'].append({'id': video_cnt, 'file_name': seq})
            seq_path = os.path.join(data_path, seq)
            img_path = os.path.join(seq_path, 'img1')
            ann_path = os.path.join(seq_path, 'gt/gt.txt')
            images = os.listdir(img_path)
            num_images = len([image for image in images if 'jpg' in image])  # half and half

            if HALF_VIDEO and ('half' in split):
                image_range = [0, num_images // 2] if 'train' in split else \
                              [num_images // 2 + 1, num_images - 1]
            else:
                image_range = [0, num_images - 1]

            for i in range(num_images):
                if i < image_range[0] or i > image_range[1]:
                    continue
                img = cv2.imread(os.path.join(data_path, '{}/img1/frame_{:06d}.jpg'.format(seq, i + 1)))
                height, width = img.shape[:2]
                image_info = {'file_name': '{}/img1/frame_{:06d}.jpg'.format(seq, i + 1),  # image name.
                              'id': image_cnt + i + 1,  # image number in the entire training set.
                              'frame_id': i + 1 - image_range[0],  # image number in the video sequence, starting from 1.
                              'prev_image_id': image_cnt + i if i > 0 else -1,  # image number in the entire training set.
                              'next_image_id': image_cnt + i + 2 if i < num_images - 1 else -1,
                              'video_id': video_cnt,
                              'height': height, 'width': width}
                out['images'].append(image_info)
            print('{}: {} images'.format(seq, num_images))


            if split != '':
                anns = np.loadtxt(ann_path, dtype=np.float32, delimiter=',')

                print('{} ann images'.format(int(anns[:, 0].max())))
                for i in range(anns.shape[0]):
                    frame_id = int(anns[i][0])
                    if frame_id - 1 < image_range[0] or frame_id - 1 > image_range[1]:
                        continue
                    track_id = int(anns[i][1])
                    cat_id = int(anns[i][7])
                    ann_cnt += 1
                    category_id = 1

                    ann = {'id': ann_cnt,
                           'category_id': category_id,
                           'image_id': image_cnt + frame_id,
                           'track_id': tid_curr,
                           'bbox': anns[i][2:6].tolist(),
                           'conf': float(anns[i][6]),
                           'iscrowd': 0,
                           'area': float(anns[i][4] * anns[i][5])}
                    out['annotations'].append(ann)
            image_cnt += num_images
            print(tid_curr, tid_last)
        print('loaded {} for {} images and {} samples'.format(split, len(out['images']), len(out['annotations'])))
        json.dump(out, open(out_path, 'w'))
