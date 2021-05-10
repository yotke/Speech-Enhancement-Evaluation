function [] = find_spectrum(name,noise_kind) %% Spectrum Showing:


addpath(strcat(pwd,'/matlab_Scripts'));
f=DrawSignal(name,noise_kind);
exportgraphics(f,strcat('spectrum_images/',name,'_',noise_kind,'.png'),'Resolution',300);


end

