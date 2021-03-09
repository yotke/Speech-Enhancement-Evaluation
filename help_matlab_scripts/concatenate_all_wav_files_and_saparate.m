%add noise to audio files
myDir = '/home/yotam/softwares/project/LibriTTS/all_wav_files';

[names_array,length_array,number_of_files,Fs] = concatenate_wav_files(myDir);

saparetor_wav_file('LibriSpeech_file.wav',names_array,length_array,number_of_files,Fs);

