#mode=$1 # mode train or test for split data
data_path_train=$1 # path to your folder contain train videos
data_path_test=$2 # path to your folder contain test videos
save_path=$3 # name folder u want to save 

echo "START CREATE TRAIN DATA"
python generate_reid_dataset_multiple.py --data_path $data_path_train --save_path $save_path --mode "train"

sleep 3
echo "START CREATE TEST DATA"
python generate_reid_dataset_multiple.py --data_path $data_path_test --save_path $save_path --mode "test"

echo "[FINISH]"



