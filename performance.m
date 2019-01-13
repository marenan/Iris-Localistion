detector = vision.CascadeObjectDetector('trained_model.xml');
imgSets = imageSet('test','recursive');
for k=11:21
   img = read(imgSets(1),k);
   img = rgb2gray(img);
   J = imnoise(img,'salt & pepper',0.02);
   J = filter2(fspecial('average',3),J)/255;
   J = medfilt2(J);
   J = imnoise(J,'gaussian',0,0.025);
   bbox = step(detector,J);
   detectedImg = insertObjectAnnotation(J,'rectangle',bbox,'iris');
   figure; imshow(detectedImg);
end

