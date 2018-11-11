positive_ins = pos_roi_2_b;
pos_dir = fullfile('C:\Users\Vineet\Desktop\me\sem-3\DSAA\cascader\positive');
addpath(pos_dir);
neg_dir = fullfile('C:\Users\Vineet\Desktop\me\sem-3\DSAA\cascader\negative');

trainCascadeObjectDetector('trained_model.xml',positive_ins,neg_dir,...
    'NumCascadeStages',10,'FeatureType','Haar');

