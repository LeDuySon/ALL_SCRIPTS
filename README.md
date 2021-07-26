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
    <li><a href="Setup"> ➤ Set up</a></li>
    <li><a href="#generate mot format dataset"> ➤ Generate MOT format dataset </a></li>
    <li><a href="#generate reid dataset for torchreid"> ➤ Prerequisites</a></li>
    <li><a href="#references"> ➤ References</a></li>
    <li><a href="#contributors"> ➤ Contributors</a></li>
  </ol>
</details>


<h2> :hammer: Set up </h2>
<br>

<pre><code>
git clone https://github.com/LeDuySon/ALL_SCRIPTS.git
conda create -n {name} python=3.8
conda activate {name}
pip install -r requirement.txt
</pre></code>

<h2> :floppy_disk: Generate MOT format dataset </h2>
<br>
<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<ul>
<li><h4 id="folder-structure"> MOT dataset structure</h2></li>
<pre><code>
  {ROOT}
  ├── images
  │   ├── test
  │   └── train
  └── labels_with_ids
</code></pre>
<li><h4 id="folder-structure"> Your dataset structure</h2></li>
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
<li> 
  <h4> Generate Steps: </h4>
    <ol>
      <li> Create a folder that have structure likes MOT dataset </li>
      <li> Go to folder generate_fairmot_dataset/, run to generate frame</li>
      <pre><code>
      python generate_fairmot_dataset.py --video_path {video_path} --save_path {save_path}
      </pre></code>
      <p> Note: 
        
        - video_path: Path to video file (Only support .mp4)
        
        - save_path: Save folder path ( eg: {ROOT}/images/train or {ROOT}/images/test)
        
        - If you want to run on multiple video, run:
        
        <pre><code>
          bash gen_frames {folder contain your .mp4 files} {save_path}
        </pre></code>
      </p>
      <li> After that, run: </li>
      <pre><code>
      python create_dataset.py --root_path {root_path} --gt_path {gt_path}
      </pre></code>
      <p> Note: 
        
        - root_path: Path to your MOT dataset folder train or test(eg: {ROOT}/images/train or {ROOT}/images/test
        
        - gt_path: Save folder path ( eg: {ROOT}/images/train or {ROOT}/images/test)
        
      </p>
      <li> Just wait and have a coffee</li>
</li>
</ul>

<h2> :floppy_disk: Generate reid dataset </h2>

.............


   

## 

