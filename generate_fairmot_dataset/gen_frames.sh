video_path=$1
save_path=$2
mode=$3
for video in ${video_path}/*.mp4; do
    echo $video
    echo "TEST"
    python generate_fairmot_dataset.py --video_path $video --save_path $save_path --mode $mode
done
