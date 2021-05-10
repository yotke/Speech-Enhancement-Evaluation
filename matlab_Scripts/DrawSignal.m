function [t] = DrawSignal(name,noise_kind)


input_signal=name;

name=split(name,'.');

t=figure();
%title('ohh ok')=
hold on;

[y_clean,Fs] = audioread(strcat(pwd,'/part_wav_files/',input_signal));%Read audio set from clean directory

subplot(3,2,1);
title('Clean Signal');
easyPlot(y_clean)

subplot(3,2,2);
title('Clean Signal FFT');
spectrum(y_clean,Fs);

[y_noisy,Fs] = audioread(strcat(pwd,'/noised/',noise_kind,'_noise/',input_signal));%Read audio set from clean directory

subplot(3,2,3);
title('Noisy Signal');
easyPlot(y_noisy)

subplot(3,2,4);
title('Noisy Signal FFT');
spectrum(y_noisy,Fs);


[y_processed,Fs] = audioread(strcat(pwd,'/',noise_kind,'/my_output/',input_signal));%Read audio set from clean directory

subplot(3,2,5);
title('Processed Signal');

easyPlot(y_processed)

subplot(3,2,6);
title('Processed Signal FFT');
spectrum(y_processed,Fs);

end

