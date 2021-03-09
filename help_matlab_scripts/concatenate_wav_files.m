function [names_array,length_array,number_of_files,Fs] = concatenate_wav_files(myDir)
    concatenate_wav_file=0;
    names_array="";
    length_array=1;
    myFiles = dir(fullfile(myDir,'*.wav')); %gets all flac files in struct
    number_of_files = length(myFiles);
    for k = 1:length(myFiles)
        name = fullfile(myDir,myFiles(k).name);
        [y_clean,Fs] = audioread(name);%Read all audio set from clean directory
        length_array(end+1) = length_array(end)+length(y_clean);
        names_array(end+1) = myFiles(k).name;
        concatenate_wav_file= [concatenate_wav_file;y_clean];
    end
    % Write to a new file outside matlab.
    fout_name = fullfile('/home/yotam/softwares/project/matlab/concatenate_file','LibriSpeech_file.wav');
    audiowrite(fout_name,concatenate_wav_file,Fs)
end

