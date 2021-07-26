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


<h2> 1. Set up </h2>
<br>

``` 
git clone https://github.com/LeDuySon/ALL_SCRIPTS.git
conda create -n {name} python=3.8
conda activate {name}
pip install -r requirement.txt
```

<h2> :floppy_disk: Generate MOT format dataset </h2>
<br>

<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<h4 id="folder-structure"> :cactus: Folder Structure</h2>
  code
  ```
  .
  ├── images
  │   ├── results
  │   │   ├── fairmot_dla34_baseline
  │   │   └── fairmot_dla34_finetune_all_reidim64
  │   ├── test
  │   │   ├── seq1
  │   │   │   ├── det
  │   │   │   ├── gt
  │   │   │   └── img1
  │   │   ├── seq2
  │   │   │   ├── det
  │   │   │   ├── gt
  │   │   │   └── img1
  │   │   └── seq3
  │   │       ├── det
  │   │       ├── gt
  │   │       └── img1
  │   └── train
  │       ├── seq4
  │       │   ├── det
  │       │   ├── gt
  │       │   └── img1
  │       ├── seq5
  │       │   ├── det
  │       │   ├── gt
  │       │   └── img1
  └── labels_with_ids
      ├── test
      │   ├── seq1
      │   │   └── img1
      │   ├── seq2
      │   │   └── img1
      │   └── seq3
      │       └── img1
      └── train
  ```
   

## 

