    % function right = converter(file)

addpath('.');

% file = '../data/kill.mat';
% fds = fileDatastore('*.mat', 'ReadFcn', @importdata);
% fullFileNames = fds.Files;
% numFiles = length(fullFileNames);
% 
% for k = 1:numFiles
%     fprintf('Reading file %s\n', fullFileNames{k})
%     new = load(fullFileNames{k});
%     new.data = new.data(:,:,1,:,:);
%     new.data = squeeze(new.data);
%     new.data = reshape(new.data,[12, 8, 710, 10]);
%     eeg = new.data;
%     save('kill.mat','eeg')
% end

new = load('S001.mat');
new.data = new.data(:,:,1,:,:);
new.data = squeeze(new.data);
new.data = permute(new.data,[4 1 2 3]);
eeg = new.data;
save('processed.mat','eeg')