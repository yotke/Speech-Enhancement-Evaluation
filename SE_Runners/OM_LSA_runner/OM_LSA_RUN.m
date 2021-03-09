%% main function, run OMLSA



dataset=rand(1);
myDir = '/home/yotam/softwares/project/matlab/noised/babble_noise'; %gets directory
myFiles = dir(fullfile(myDir,'*.wav')); %gets all wav files in struct
for k = 1:length(myFiles)
    baseFileName = myFiles(k).name
    
    babble_noise_audio = fullfile('/home/yotam/softwares/project/matlab/noised/babble_noise', baseFileName);
    fout_babble_noise = fullfile('/home/yotam/softwares/project/LibriTTS_OM_LSA/babble/my_output',myFiles(k).name);
    
    [y_babble,out_babble] = omlsa(babble_noise_audio,fout_babble_noise);
    
    white_noise_audio = fullfile('/home/yotam/softwares/project/matlab/noised/white_noise', baseFileName);
    fout_white_noise = fullfile('/home/yotam/softwares/project/LibriTTS_OM_LSA/white/my_output',myFiles(k).name);
    
    [y_white,out_white] = omlsa(white_noise_audio,fout_white_noise);
  
    % all of your actions for filtering and plotting go here
end
