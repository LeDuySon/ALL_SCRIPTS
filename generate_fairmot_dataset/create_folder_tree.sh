name=$1 # root name of folder tree

mkdir $name 
cd $name 
# images branch
mkdir images
#labels branch 
mkdir labels_with_ids

cd images
mkdir test
mkdir train

cd ../.. # main folder
