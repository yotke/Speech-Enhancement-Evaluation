%% main function, run OMLSA

function[] = Om_lsa_runner(noiseKind)

myDir = strcat(pwd,'/noised/',noiseKind,'_noise'); %gets directory
myFiles = dir(fullfile(myDir,'*.wav')); %gets all wav files in struct
for k = 1:length(myFiles)
    baseFileName = myFiles(k).name
    
    noise_audio = fullfile(strcat(pwd,'/noised/',noiseKind,'_noise'), baseFileName);
    fout_noise = fullfile(strcat(pwd,'/',noiseKind,'/my_output'),myFiles(k).name);
    
    [y_noise,out_noise] = omlsa(noise_audio,fout_noise);
    
    white_noise_audio = fullfile(strcat(pwd,'/noised/white_noise'), baseFileName);
    fout_white_noise = fullfile(strcat(pwd,'/white/my_output'),myFiles(k).name);
    
    [y_white,out_white] = omlsa(white_noise_audio,fout_white_noise);
  
    % all of your actions for filtering and plotting go here
end
end
