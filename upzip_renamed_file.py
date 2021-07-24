import os
import glob
import zipfile
import re 

def unzip_file(file):
    tmp = file.split("/")
    main_folder = tmp[0]
    video_name = get_video_name(tmp[1].upper())
    extract_folder = os.path.join(main_folder, video_name)
    print("Extract: ", extract_folder)
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    
    return "Success"

video_name_pattern = r"(NVR-CH.*E[0-9]{8}-[0-9]{6})"

def get_video_name(file):
    name = re.findall(video_name_pattern, file)[0]
    return name

folders = ["train", "test"]
for folder in folders:
    zip_files = glob.glob(folder + "/*.zip")
    for zip_file in zip_files:
        unzip_file(zip_file)
