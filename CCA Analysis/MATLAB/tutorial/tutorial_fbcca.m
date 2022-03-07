%% Clear workspace
clear
close all
clc
% help tutorial_fbcca

%% Set paths

addpath('../src');

%% Parameter for analysis (Modify according to your analysis)

% Filename
filename = '../data/processed.mat';

% Data length for target identification [s]
len_gaze_s = 2;   

% Visual latency being considered in the analysis [s]
len_delay_s = 0.14;                  

% The number of sub-bands in filter bank analysis
num_fbs = 5;

% The number of harmonics in the canonical correlation analysis 
num_harms = 5;

% 100*(1-alpha_ci): confidence intervals
alpha_ci = 0.05;                 

%% Fixed parameter (Modify according to the experimental setting)

% Sampling rate [Hz]
fs = 250;                  

% Duration for gaze shifting [s]
len_shift_s = 0.2;                  

% List of stimulus frequencies
list_freqs = [9.25,11.25,13.25,9.75 11.75,13.75,10.25,12.25 14.25,10.75,12.75,14.75];
                                        
% The number of stimuli
num_targs = length(list_freqs);    

% Labels of data
labels = [1:1:num_targs];         

%% Preparing useful variables (DONT'T need to modify)

% Data length [samples]
len_gaze_smpl = round(len_gaze_s*fs);           

% Visual latency [samples]
len_delay_smpl = round(len_delay_s*fs);         

% Selection time [s]
len_sel_s = len_gaze_s + len_shift_s;

% Confidence interval
ci = 100*(1-alpha_ci);                  

%% Performing the FBCCA-based SSVEP detection algorithm
fprintf('Results of the FBCCA-based method.\n');

% Preparing data
load(filename);
[~, num_chans, ~, num_blocks] = size(eeg);
segment_data = 125+len_delay_smpl+1:125+len_delay_smpl+len_gaze_smpl;
eeg = eeg(:, :, segment_data, :); 

% Estimate classification performance
for block_i = 1:1:num_blocks
    
    % Test 
    testdata = squeeze(eeg(:, :, :, block_i));
    estimated = test_fbcca(testdata, list_freqs, fs, num_harms, num_fbs);
    
    % Evaluation 
    is_correct = (estimated==labels);
    accs(block_i) = mean(is_correct)*100;
    itrs(block_i) = itr(num_targs, mean(is_correct), len_sel_s);
    fprintf('Trial %d: Accuracy = %2.2f%%, ITR = %2.2f bpm\n',...
        block_i, accs(block_i), itrs(block_i));
    
end % block_i

% Summarize
[mu, ~, muci, ~] = normfit(accs, alpha_ci);
fprintf('Mean accuracy = %2.2f %% (%2d%% CI: %2.2f - %2.2f %%)\n',...
    mu, ci, muci(1), muci(2));

[mu, ~, muci, ~] = normfit(itrs, alpha_ci);
fprintf('Mean ITR = %2.2f bpm (%2d%% CI: %2.2f - %2.2f bpm)\n\n',...
    mu, ci, muci(1), muci(2));
