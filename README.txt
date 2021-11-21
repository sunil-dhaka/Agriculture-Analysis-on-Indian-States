NOTE: To be able to run data.py one needs an API key and have to store it into login.py.
Otherwise can use stored data from datasets-folder.

-----------------Project README.txt------------------


Plugins-
Software: python3 jupyter notebook (.sh files run python3 jupyter notebooks)

Environments: conda 4.10.3, python 3.8.5


Dependencies-
Python Libraries: pandas 1.1.3, numpy 1.19.2, geopandas 0.10.2, 
requests 2.26.0, matplotlib 3.4.3, os, warnings, seaborn 0.11.2

------------------------------------------------------------------------------------------------

Programs-

.sh files:

project.sh 
top level script that runs the entire project

How to use:
In order to run all programs sequentially, run the following command from the terminal-
bash project.sh 

One could use `time` command before bash execution to see how much time script takes to run.

Things to note:
It takes about 10 mins to run on my machine.



How to run particular shell script:
--------------------------------------------------------------------------------------------
analysis.sh
runs analysis.ipynb as
jupyter nbconvert --to notebook --execute analysis.ipynb

state-geo-analysis.sh
runs state-geo-analysis.ipynb as
jupyter nbconvert --to notebook --execute state-geo-analysis.ipynb

district-geo-analysis.sh
runs district-geo-analysis.ipynb as
jupyter nbconvert --to notebook --execute district-geo-analysis.ipynb

area.sh
runs area.py

data.sh
runs data.py
------------------------------------------------------------------------------------------------

- NOTE: Every detail about the procedure of analysis files is given in markdowns and comments of notebooks. Also relevent obervation about outputs are given in the last markdown section of each notebook file with appropriate data displyed above or below the obervations section, for better understanding and readibility. Even particular dataset files that are used to solve the question are mentioned in the markdowns. Please look there for minor details, here I am giving a summarised input/output for all notebooks.

Jupyter Notebook and Python Script files points:

area.py
Input: None

Output: datasets/area.csv

data.py
Input: None

Output: datasets/crop_production.csv

state-geo-analysis.ipynb
Input: datasets/area.csv, datasets/crop_production.csv, datasets/geo_maps/gadm36_IND_1.shp

Output: animation-images/*, project_report_images/*

districts-geo-analysis.ipynb
Input: datasets/area.csv, datasets/crop_production.csv, datasets/geo_maps/gadm36_IND_2.shp

Output: project_report_images/*

------------------------------------------------------------------------------------------------
Dir Structure on Level 1:
.
├── analysis.sh
├── animation-images
│   ├*.png files
│   ├*.gif files
├── area.py
├── area.sh
├── data.py
├── datasets
│   ├── area.csv
│   ├── crop_production.csv
│   └── geo_maps
├── data.sh
├── district-geo-analysis.ipynb
├── district-geo-analysis.sh
├── general.md
├── gpu_server.md
├── LICENSE
├── login.py
├── project-ideas.md
├── project_report_images
├── project.sh
├── README.md
├── README.txt
├── state-geo-analysis.ipynb
└── state-geo-analysis.sh
