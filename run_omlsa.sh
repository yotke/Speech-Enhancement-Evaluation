#!/bin/bash



#chmod 777 OM_LSA_RUN.m
chmod 777 omlsa.m

noise_kind=$1
mkdir $noise_kind
mkdir $noise_kind/my_output
mkdir white
mkdir white/my_output


cur_dir="$pwd"

matlab -nodisplay -nodesktop -r "Om_lsa_runner('$noise_kind'); quit"

cd $cur_dir

#matlab -nodisplay -nodesktop -r 'cd /home/yotam/softwares/project/matlab/matlab_scripts; babble_5db; quit'

