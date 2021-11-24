set -e 

video_path=$1
save_path=$2
frame_interval=$3

for video in ${video_path}/*.mp4; do
    name=(${video//// })
    folder_name=$(echo ${name[-1]} | cut -d'.' -f 1)
    save_folder="${save_path}${folder_name}"
    echo $save_folder
    if [ ! -d $save_folder ]
    then
        python generate_frame_from_videos.py --video_path $video --save_path $save_folder --frame_interval $frame_interval
    else
        echo "Already run"
    fi
done
