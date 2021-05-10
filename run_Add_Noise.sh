#!/bin/bash

noiseKind=$1
db_ratio=$2
mkdir noised
mkdir noised/"$noiseKind"_noise
mkdir noised/white_noise


chmod 777 add_noise.m


cur_dir="$pwd"
matlab -nodisplay -nodesktop -r "Add_noise('$noiseKind',$db_ratio) ; quit"
cd $cur_dir

