function eeg = converter(~)
% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();

% resolve a stream...
disp('Resolving an EEG stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'name','SSVEP_CCA'); end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});

disp('Now receiving chunked data...');
number_targets = 12;
% eeg = zeros(number_targets, a(1), a(2));
for i = 1:1:number_targets
    % while true
        % get chunk from the inlet
        [chunk,stamps] = inlet.pull_chunk();
        a = size(chunk);
        for s=1:length(stamps)
            % and display it
            fprintf('%.2f\t',chunk(:,s));
            fprintf('%.5f\n',stamps(s));
            eeg(i,:,s) = chunk(:,s);
        end
        % eeg(i,:,:) = chunk(:;
        pause(5);
        % eeg = zeros(number_targets, a(1), a(2));
    %end
end
end