%add noise to audio files
noiseKind = input(prompt,'s');
myDir = strcat(pwd,'/part_wav_files');
ratio =5; % ratio of signal to noise.
db_ratio=10^(ratio/20);
[noise,Fs_b]= audioread(strcat('/home/yotam/softwares/project/matlab/',noiseKind,' noises/',noiseKind,'.wav'));

myFiles = dir(fullfile(myDir,'*.wav')); %gets all flac files in struct
for k = 1:length(myFiles)
    
    name = fullfile(strcat(pwd,'/part_wav_files'),myFiles(k).name);
    
    [y_clean,Fs] = audioread(name);%Read all audio set from clean directory
   noised_signal = y_clean+ noise(1+1000*k:1000*k+length(y_clean))/db_ratio; %+ babble_noise(10*k:10*k+length(y_clean))/db_ratio
     
    % Write to a new file outside matlab.
    fout_name = fullfile(strcat(pwd,'/noised/',noiseKind,'_noise'),myFiles(k).name);
    audiowrite(fout_name,noised_signal,Fs)
    
    
    sigma = rms(y_clean)/db_ratio;
    white_noise = normrnd(0,sigma,length(y_clean),1);
    white_noised_signal = y_clean+white_noise;
    
    
    %Write to a new file outside matlab.
    fout_name = fullfile(strcat(pwd,'/noised/white_noise'),myFiles(k).name);
    audiowrite(fout_name,white_noised_signal,Fs)
    
end

