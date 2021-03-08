#!/bin/bash


#This script get from the user the number of text file he want to .. 
#open and the kind of the file he want to open, including (noised DTLN and Baidu processed, noised Baidu processed, clean Baidu processed)
# The script open the exact file with the number given in every directory needed.
#Additionally This script open the file with the number given in the clean original and original text directories.


main_directory=$(pwd)
part_flag=''


while getopts ":p:" opt; do
  case $opt in
    p)
      part_flag='true'
      echo "-o was triggered, Parameter: $OPTARG" >&2
      shift      

      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

noise_kind=$3

open_files(){

if [[ $part_flag == 'true' ]];then
	clean_directory='part_clean_original_txt_file'
else 
	clean_directory='clean_original_txt_file'
fi
xdg-open $main_directory/original_txt_files/$1.original.txt &
xdg-open $main_directory/$clean_directory/$1.original.txt &
xdg-open $main_directory/$noise_kind/diff/$2/different_words/$1.txt & 
xdg-open $main_directory/$noise_kind/my_output/$2/$1.txt &

}

open_files $1 $2
