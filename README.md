<h1 align="center"> My script for generate dataset </h1>
</br>
<p align="center"> 
  <img src="images/Signal.gif" alt="Sample signal" width="70%" height="70%">
</p>

<br>

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Setup"> ➤ Set up</a></li>
    <li><a href="#dataset structure"> ➤ Dataset Structure</a></li>
    <li><a href="#generate mot format dataset"> ➤ Generate MOT format dataset </a></li>
    <li><a href="#generate reid dataset for torchreid"> ➤ Generate reid dataset</a></li>
    <li><a href="#generate for bytetrack"> ➤ Generate bytetrack dataset</a></li>
    <li><a href="#references"> ➤ References</a></li>
    <li><a href="#contributors"> ➤ Contributors</a></li>
  </ol>
</details>


<h2 id="Setup"> :hammer: Set up </h2>
<br>

<pre><code>
git clone https://github.com/LeDuySon/ALL_SCRIPTS.git
conda create -n {name} python=3.8
conda activate {name}
pip install -r requirement.txt
</pre></code>

<h2 id="dataset structure"> :books: Dataset Structure</h2>
<br>

<ul>
  <li><h4> You have to prepare your dataset same as below</h4></li>
<li><h4 id="folder-structure"> Your dataset structure </h2></li>
<pre><code>
  {ROOT}
  ├── video1.mp4
  ├── video1
  │   └── gt
  │       ├── gt.txt
  │       └── labels.txt
  ├── video2.mp4
  ├── video2
  │   └── gt
  │       ├── gt.txt
  │       └── labels.txt
  ├── video3.mp4
  ├── video3
  │   └── gt
  │       ├── gt.txt
  │       └── labels.txt
   
</code></pre>
</ul>
  
<h2 id="generate mot format dataset"> :floppy_disk: Generate MOT format dataset </h2>
<br>
<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<ul>
<li><h4 id="folder-structure"> MOT dataset structure</h2></li>
<pre><code>
  {ROOT_MOT}
  ├── images
  │   ├── test
  │   └── train
  └── labels_with_ids
</code></pre>

<li> 
  <h4> Generate Steps: </h4>
    <ol>
      <li> Create a folder that have structure likes MOT dataset </li>
      <pre><code>
      bash create_folder_tree.sh {Name of ROOT_MOT}
      </pre></code>
      <li> Go to folder generate_fairmot_dataset/, run to generate frame</li>
      <pre><code>
      python generate_fairmot_dataset.py --video_path {video_path} --save_path {save_path} --frame_interval {frame_interval}
      </pre></code>
      <p> Note: 
      <ul>
        <li> video_path: Path to video file (Only support .mp4) </li>
        <li> save_path: Save folder path ( eg: {ROOT}/images/train or {ROOT}/images/test) </li>
        <li> frame_interval: Number of frame between 2 saving frames</li>
        <li> If you want to run on multiple video, run: </li>
      </ul>
        <pre><code>
          bash gen_frames {folder contain your .mp4 files} {save_path} {frame_interval}
        </pre></code>
      </p>
      <li> After that, run: </li>
      <pre><code>
      python create_dataset.py --root_path {root_path} --gt_path {gt_path}
      </pre></code>
      <p> Note:  
         <ul>
            <li> root_path: Path to your MOT dataset folder train or test(eg: {ROOT_MOT}/images/train or {ROOT_MOT}/images/test </li>
            <li> gt_path: Path to groundtruth folder ( eg: {ROOT}/train or {ROOT}/test) </li>
            <li> If you want to run on multiple video, run: </li>
         </ul>
      </p>
      <li> Just wait and have a coffee</li>
</li>
</ul>

<h2 id="generate reid dataset for torchreid"> :floppy_disk: Generate reid dataset </h2>

<ul>
<li><h5> Your dataset(train|test) must be the same as ours <a href="#dataset structure"> datasets </a> </li>
<li> Generate reid dataset for multiple videos with mode train or test </li>
<pre><code>
python generate_reid_dataset_multiple.py --data_path {path to your dataset, eg {ROOT} in our dataset} \
                                          --save_path {name of saving folders} --mode {mode train|test|normal}
</code></pre>
  
<li>If you want to prepare dataset entirely, run this: </li>
<pre><code>
 bash create_data.sh {path to your train dataset} {path to your test dataset} {name of saving folders}
</code></pre>

<li> Notes about {mode} args </li>
  <ul>
    <li> train: only save in train/ folder </li>
    <li> test: save to gallery/ folder and then split to query/ folder</li>
    <li> normal: save to train/ folder and then split to gallery/ and query/ folder</li>
   </ul>
</ul>

<h4> Results after generate: </h4>
<pre><code>
.          
├── gallery
├── query  
└── train  
    ├── 0  
    ├── 1  
    ├── 2  
    ├── 3  
    ├── 4  
    ├── 5  
    ├── 6  
    ├── 7  
    ├── 8  
    └── 9  

</code></pre>

<h2 id="generate for bytetrack"> :floppy_disk: Generate bytetrack dataset </h2>

<li><h4 id="folder-structure-bytetrack"> BYTETRACK dataset structure</h4></li>
<pre><code>
{ROOT_COCO}
├── annotations
├── test
├── train
└── val
</code></pre>

<li><h5> Your dataset(train|test) must be the same as ours <a href="#dataset structure"> datasets </a> </li>
<ol>
      <li> Create a folder that have structure likes COCO dataset </li>
      <pre><code>
      bash create_folder_tree.sh {Name of ROOT_COCO}
      </pre></code>
      <li> Run to generate frame from video</li>
      <pre><code>
      python generate_frame_from_videos.py --video_path {video_path} --save_path {save_path} --frame_interval {frame_interval}
      </pre></code>
      <p> Note: 
      <ul>
        <li> video_path: Path to video file (Only support .mp4) </li>
        <li> save_path: Save folder path ( eg: {ROOT}/images/train or {ROOT}/images/test) </li>
        <li> frame_interval: Number of frame between 2 saving frames</li>
        <li> If you want to run on multiple video, run: </li>
      </ul>
        <pre><code>
          bash gen_frames {folder contain your .mp4 files} {save_path} {frame_interval}
        </pre></code>
      </p>
      <li> After that, run: </li>
      <pre><code>
      python create_dataset.py --root_path {root_path} --gt_path {gt_path}
      </pre></code>
      <p> Note:  
         <ul>
            <li> root_path: Path to your MOT dataset folder train or test(eg: {ROOT_MOT}/images/train or {ROOT_MOT}/images/test </li>
            <li> gt_path: Path to groundtruth folder ( eg: {ROOT}/train or {ROOT}/test) </li>
         </ul>
      </p>
      <li> Finally, run this script to convert your dataset to coco format (get json files in annotation folder): </li>
      <pre><code>
      python convert_vtx_to_coco.py --data_path {ROOT_COCO}
      </pre></code>
      

## 

