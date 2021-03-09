%add noise to audio files
myDir = '/home/yotam/softwares/project/LibriTTS/part_wav_files';
concatenate_wav_file=0;
names_array="";
length_array=1;
number_of_files=0;
myFiles = dir(fullfile(myDir,'*.wav')); %gets all flac files in struct
number_of_files = length(myFiles);
for k = 1:length(myFiles)
    
    name = fullfile('/home/yotam/softwares/project/LibriTTS/part_wav_files',myFiles(k).name);
    
    [y_clean,Fs] = audioread(name);%Read all audio set from clean directory
    length_array(end+1) = length_array(end)+length(y_clean);
    names_array(end+1) = myFiles(k).name;
    concatenate_wav_file= [concatenate_wav_file;y_clean];

end
% Write to a new file outside matlab.
fout_name = fullfile('/home/yotam/softwares/project/matlab/concatenate_file','LibriSpeech_file.wav');
audiowrite(fout_name,concatenate_wav_file,Fs)


myDir = '/home/yotam/softwares/project/matlab/concatenate_file';
name = fullfile(myDir,'LibriSpeech_file.wav');
concatenate_file = audioread(name);
for k = 1:length(myFiles)
    length_y = length_array(k+1);
    sapareted_wav_files = concatenate_file(length_array(k):length_array(k+1));
    % Write to a new file outside matlab.
    fout_name = fullfile('/home/yotam/softwares/project/matlab/saparated_files',names_array(k+1));
    audiowrite(fout_name,sapareted_wav_files,Fs);
end

