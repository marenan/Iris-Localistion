detector = vision.CascadeObjectDetector('trained_model.xml');

imgSets = imageSet('test','recursive');
n =  uint32([trd.Count]);
for k=1:10
   img = read(imgSets(1),k);
   bbox = step(detector,img);
   detectedImg = insertObjectAnnotation(img,'rectangle',bbox,'iris');
   figure; imshow(detectedImg);
end

