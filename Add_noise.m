function [] = Add_noise(noiseKind,db_ratio)
%add noise to audio files
myDir = strcat(pwd,'/part_wav_files');
%db_ratio =10; % ratio of signal to noise.
ratio=10^(db_ratio/20)
%ratio=20*log(x);
string=strcat("/home/yotam/softwares/project/matlab/",noiseKind," noises/",noiseKind,".wav")
[noise,Fs_b]= audioread(string);

myFiles = dir(fullfile(myDir,'*.wav')); %gets all flac files in struct
for k = 1:length(myFiles)
    
    name = fullfile(strcat(pwd,'/part_wav_files'),myFiles(k).name);
    
   [y_clean,Fs] = audioread(name);%Read all audio set from clean directory
   y_rms=rms(y_clean);
   noise_rms=rms(noise);
   noised_signal = y_clean/y_rms+(noise(1:length(y_clean),1))/ratio/noise_rms(1); 
     
    % Write to a new file outside matlab.
    fout_name = fullfile(strcat(pwd,'/noised/',noiseKind,'_noise'),myFiles(k).name);
    audiowrite(fout_name,noised_signal,Fs)
    
    
    sigma = rms(y_clean)/ratio;
    white_noise = normrnd(0,sigma,length(y_clean),1);
    white_noised_signal = y_clean+white_noise;
    
    
    %Write to a new file outside matlab.
    fout_name = fullfile(strcat(pwd,'/noised/white_noise'),myFiles(k).name);
    audiowrite(fout_name,white_noised_signal,Fs)
    
end


end

