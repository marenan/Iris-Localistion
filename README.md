# DSAA

&nbsp;
&nbsp;
> ## Problem Statement
Iris recognition, the ability to recognize and distinguish individuals by their Iris
pattern, is the most reliable biometric in terms of recognition and identification
performance. However, performance of these systems is affected by factors like
focus, contrast, or brightness and with several noise factors like iris obstruction by
eyelashes and eyelids. Current Iris recognition system does not deal with the
noise data such as images in which Iris is covered with eyelashes and substantially
increase their error rates in these conditions. Hence, an attempt has been made
to work on latter problem of Iris Localization. 

&nbsp;
&nbsp;
> ## How To Use This Repo

* Folder __info__ and __positive__ contains positive image dataset used for generating ground truth.
* Folder __negative__ contains negative set of images.
* File __gTruth.mat__ is ground truth generated after manually labelling positive images.
* File __trained_model_1.xml__ is cascaded classifier obtained after training.
* File __performance.m__ checks the performance for cascaded classifier. This is done by manully checking each image.
