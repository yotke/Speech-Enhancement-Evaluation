function saparetor_wav_file(concatenate_wav_file,names_array,length_array,number_of_files,Fs)


    myDir = '/home/yotam/softwares/project/matlab/concatenate_file';
    name = fullfile(myDir,concatenate_wav_file);
    concatenate_file = audioread(name);
    for k = 1:number_of_files
        length_y = length_array(k+1);
        sapareted_wav_files = concatenate_file(length_array(k):length_array(k+1));
        % Write to a new file outside matlab.
        fout_name = fullfile('/home/yotam/softwares/project/matlab/saparated_files',names_array(k+1));
        audiowrite(fout_name,sapareted_wav_files,Fs);
    end
end

