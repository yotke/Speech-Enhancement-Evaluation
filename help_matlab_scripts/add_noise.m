%add noise to audio files
myDir = '/home/yotam/softwares/project/LibriTTS/part_wav_files';
ratio =5; % ratio of signal to noise.
db_ratio=10^(ratio/20);
[babble_noise,Fs_b]= audioread('/home/yotam/softwares/project/matlab/bubble noises/babble.wav');

myFiles = dir(fullfile(myDir,'*.wav')); %gets all flac files in struct
for k = 1:length(myFiles)
    
    name = fullfile('/home/yotam/softwares/project/LibriTTS/part_wav_files',myFiles(k).name);
    
    [y_clean,Fs] = audioread(name);%Read all audio set from clean directory
    babble_noised_signal = y_clean+ babble_noise(1+1000*k:1000*k+length(y_clean))/db_ratio; %+ babble_noise(10*k:10*k+length(y_clean))/db_ratio
     
    % Write to a new file outside matlab.
    fout_name = fullfile('/home/yotam/softwares/project/matlab/noised/babble_noise',myFiles(k).name);
    audiowrite(fout_name,babble_noised_signal,Fs)
    
    sigma = rms(y_clean)/db_ratio;
    white_noise = normrnd(0,sigma,length(y_clean),1);
    white_noised_signal = y_clean+white_noise;
    
    
    %Write to a new file outside matlab.
    fout_name = fullfile('/home/yotam/softwares/project/matlab/noised/white_noise',myFiles(k).name);
    audiowrite(fout_name,white_noised_signal,Fs)
    
end




%sound(z,Fs)
%S_im=imnoise(y_clean,'Gaussian',Mean,Var);
%out=awgn(y_clean,27); % using matlab to create a normal distribution
%fout = strcat(fout_name,'.wav');
%y_i = strcat('y_',out_num); % a new dateset
%myDir = uigetdir; %gets directory