---
title: OpenTLD
template: tld.jade
comments: true
code: true
date: 2011-11-21
---

On this page you can find a C++ implementation of OpenTLD that was originally published in MATLAB by Zdenek Kalal. OpenTLD is used for
tracking objects in video streams. What makes this algorithm outstanding is that it does not make use of any training
data. This implementation is based solely on open source libraries, meaning that you do not need any commercial
products to compile or run it.

The easiest way to get started is to download the [precompiled binaries][1] that are available for Windows and Ubuntu.
If you have a webcam attached to your PC, you can simply execute tld (on Ubuntu) or tld.exe (on Windows) in order to
try it out. For other configuration options, please have a look at the [README][2] file. There is also a [discussion group][3] of the TLD community where you might get some information.
A documentation of the internals as well as other possibly helpful information is contained in this [master thesis](/publications/master_thesis/master_thesis.pdf).

The [source code](#download) of OpenTLD is published under the terms of the GNU General Public License, so feel free to dig through it.
Please understand that this software is meant as a demonstration of what state-of-the-art computer vision algorithms are currently
capable of and not as a ready-to-use product. If you find errors in the program, please report them at the [GitHub issues page][4].

## Result Videos

<iframe class="youtube" width="420" height="315" src="http://www.youtube.com/embed/PCx2tFeHPiQ"></iframe>
<iframe class="youtube" width="420" height="315" src="http://www.youtube.com/embed/qcw_R6wCG6E"></iframe>

## Download

You can download this project in either [zip][5] or [tar formats][6].
You can also browse the source code on [GitHub][2] or clone the project directly with [Git][7] by running:

```
$ git clone git://github.com/gnebehay/OpenTLD
```

## Frequently Asked Questions

### Can I use OpenTLD for multi-target tracking?</h3>
In principle OpenTLD is meant to track single objects only,
but there is nothing that stops you from employing multiple instances of OpenTLD for multi-target tracking.
It is rather difficult to implement multi-target tracking in OpenTLD itself,
as the sliding-window approach is heavily optimised for the specific dimensions of the object.
If your objects are all of the same size, it might be worthwile investigating this option.

[1]: https://github.com/gnebehay/OpenTLD/downloads
[2]: https://github.com/gnebehay/OpenTLD 
[3]: http://groups.google.com/group/opentld
[4]: https://github.com/gnebehay/OpenTLD/issues
[5]: https://github.com/gnebehay/OpenTLD/zipball/master
[6]: https://github.com/gnebehay/OpenTLD/tarball/master
[7]: http://git-scm.com
