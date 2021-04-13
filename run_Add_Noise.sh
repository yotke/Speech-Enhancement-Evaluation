#!/bin/bash

mkdir noised
mkdir noised/babble_noise
mkdir noised/white_noise

chmod 777 add_noise.m

#path_IN=/home/yotam/softwares/project/matlab/my_example_wavs/noised
#path_OUT=/home/yotam/softwares/project/matlab/OUT

cur_dir="$pwd"
matlab -nodisplay -nodesktop -r 'add_noise; quit'
cd $cur_dir
#matlab -nodisplay -nodesktop -r 'cd /home/yotam/softwares/project/matlab/matlab_scripts; babble_5db; quit'

