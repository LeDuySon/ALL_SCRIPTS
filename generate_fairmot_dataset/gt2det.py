import os

path = "MOT20/images/train/video30min/gt/gt.txt"

rows = []
with open(path, "rt") as f:
    for line in f:
        cols = line.strip().split(",")
        cols[1] = "-1"
        cols[7] = "-1"
        cols[8] = "-1"
        rows.append(",".join(cols))

det_path = path.split("/")[:-2] + ["det", "det.txt"]
det_path = "/".join(det_path)
with open(det_path, "wt") as f:
    for row in rows:
        f.write(row + "\n")