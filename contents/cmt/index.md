title: Clustering of Static-Adaptive Correspondences for Deformable Object Tracking
comments: true
code: true

<div class="sidecolumn">
<a href="https://github.com/gnebehay/CppMT">
<img style="position: relative; top: -30px; right: -31px; border: 0;" src="http://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub">
</a>
</div>

Clustering of Static-Adaptive Correspondences for Deformable Object Tracking
(CMT) is an award-winning object tracking algorithm, initially [published](/publications/wacv_2015) under
the name Consensus-based Tracking and Matching of Keypoints for Object Tracking
at the [Winter Conference on Applications of Computer Vision 2014](http://www.wacv14.org),
where it received the Best Paper Award.
A more detailed [paper](/publications/cvpr_2015) was published at the
[Conference on Computer Vision and Pattern Recognition 2015](http://www.pamitc.org/cvpr15).
CMT is able to track a wide variety of object classes in a multitude of scenes
without the need of adapting the algorithm to the concrete scenario in any way.
Experiments have shown that CMT is able to achieve excellent results
on a dataset that is as large as 77 sequences.
A C++ implementation ([CppMT][2]) is freely available under the BSD license,
meaning that you can basically do with the code whatever you want.
Additionally, the original [Python research code](http://github.com/gnebehay/CMT) is still available for reference.

## How does it work?
The main idea behind CMT is to break down the object of interest into tiny parts, known as keypoints.
In each frame, we try to again find the keypoints that were already there
in the initial selection of the object of interest.
We do this by employing two different kind of methods.
First, we *track* keypoints from the previous frame to the current frame by estimating
what is known as its *optic flow*.
Second, we *match* keypoints globally by comparing their *descriptors*.
As both of these methods are error-prone, we employ a novel way of looking for consensus within
the found keypoints by letting each keypoint vote for the object center,
as shown in the following image:

![Voting](voting.png)

The votes are then clustered and outliers are removed:

![Consensus](consensus.png)

Based on the remaining keypoints, the new bounding box is computed and the process continues.
All the details can be found in [our publication](/publications/cvpr_2015).

## How to get it?


You can download CMT in either [zip][5] or [tar formats][6].
You can also browse the source code on [GitHub][2] or clone the project directly with [Git][7] by running:

```
$ git clone git://github.com/gnebehay/CppMT
```

If you use our algorithm in scientific work, please cite our publication
```
@inproceedings{Nebehay2015CVPR,
    author = {Nebehay, Georg and Pflugfelder, Roman},
    booktitle = {Computer Vision and Pattern Recognition},
    month = jun,
    publisher = {IEEE},
    title = {Clustering of {Static-Adaptive} Correspondences for Deformable Object Tracking},
    year = {2015}
}
```

## Dataset

You can [download the dataset][1] (~1.2GB) that we employed for evaluating our algorithm,
consisting of 60 sequences collected by [Tomas Vojir](http://cmp.felk.cvut.cz/~vojirtom/dataset/index.html).

## Results

<a href="results.html">Click here for result videos.</a>

[1]: https://www.dropbox.com/s/oogyagnrrsi9n49/cmt_dataset.7z?dl=0
[2]: https://github.com/gnebehay/CppMT
[5]: https://github.com/gnebehay/CppMT/zipball/master
[6]: https://github.com/gnebehay/CppMT/tarball/master
[7]: http://git-scm.com
