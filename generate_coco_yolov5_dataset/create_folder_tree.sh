dataset_path=$1

if [ $# -eq 2 ]
then
	path_name=$2
else
 	path_name="ql48d" #default value for our uet projects
fi

if [ -d "${dataset_path}" ]; then
	echo "Folder tree already existed, so skip"
else
	echo "Create dataset tree!!!"
	mkdir $dataset_path
	mkdir "${dataset_path}/uet_vehicle_dataset"
	# image branch
	mkdir "${dataset_path}/uet_vehicle_dataset/images"
	mkdir "${dataset_path}/uet_vehicle_dataset/images/train_${path_name}" # quoc lo 48d -> ten nga tu
	mkdir "${dataset_path}/uet_vehicle_dataset/images/val_${path_name}"
	mkdir "${dataset_path}/uet_vehicle_dataset/images/test_${path_name}"

	# label branch
	mkdir "${dataset_path}/uet_vehicle_dataset/labels"                   
	mkdir "${dataset_path}/uet_vehicle_dataset/labels/train_${path_name}"
	mkdir "${dataset_path}/uet_vehicle_dataset/labels/val_${path_name}"  
	mkdir "${dataset_path}/uet_vehicle_dataset/labels/test_${path_name}" 

	echo "FINISH"
fi


