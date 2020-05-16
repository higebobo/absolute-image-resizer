# Absolute Image Resizer

## General

Absolute Image Resizer is resizing image with absolute image size
keeping aspect ratio for the original image.

Require Python 2.7 or Python 3.3 and Pillow

## Install

get source from the repository

    $ git clone git://github.com/higebobo/absolute-image-resizer.git

## Usage

resize image with width 640 pixel and height 480 pixcel (overwrite)

    $ python resize.py --width=640 --height=480 example.jpg

set output filename with suffix to avoid overwriting

    $ python resize.py --width=640 --height=480 --suffix=_1 example.jpg

## Release note

* 2016-09-01

    - Bug fix

* 2016-02-03

    - First release
