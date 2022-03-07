function eeg = lsl_mat()

addpath('./src');

% Load important constants
fs = 125;
list_freqs = [5, 5.25, 5.5 5.75, 6, 6.25 6.5, 6.75, 7 7.25, 7.5, 7.75];
% The number of sub-bands in filter bank analysis
num_fbs = 5;

% The number of harmonics in the canonical correlation analysis 
num_harms = 5;
% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();

% resolve a stream...
disp('Resolving an EEG stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'name','SSVEP_CCA'); end
disp('Resolving a Markers stream...');
result1 = {};
while isempty(result1)
    result1 = lsl_resolve_byprop(lib,'name','crosshairMarkers'); end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});
inlet1 = lsl_inlet(result1{1});

disp('Now receiving chunked data...');
number_targets = length(list_freqs);

% eeg = zeros(number_targets, size(chunk));
% for i = 1:1:number_targets
    while true
        % get chunk from the inlets
        [mrks,ts] = inlet1.pull_sample();
        %if mrks{1} == 'Start'
            [chunk,stamps] = inlet.pull_chunk();
            a = size(chunk);
            eeg = zeros(number_targets, a(1), a(2));
            %eeg
            for s=1:length(stamps)
                % and display it
                fprintf('%.2f\t',chunk(:,s));
                fprintf('%.5f\n',stamps(s));
                eeg(2,:,s) = chunk;
            end
        %end
    pause(5);
    target = test_fbcca(eeg, list_freqs, fs, num_harms, num_fbs);
    fprintf('Predicted number \n', target)
    end
end