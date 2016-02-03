#!/usr/bin/env python
# -*- mode: python -*- -*- coding: utf-8 -*-
from optparse import OptionParser
import os

from PIL import Image, ImageDraw

def resize(obj, width, height, mode='RGB', algorithm=Image.ANTIALIAS):

    def arrange(image, original_width, original_height, new_width, new_height):
        result = Image.new(mode, (new_width, new_height), (255, 255, 255))
        draw = ImageDraw.Draw(result)
        result.paste(image, (int((new_width - original_width) / 2),
                             int((new_height - original_height) / 2)))
        
        return result
        
    try:
        im = Image.open(obj)
    except:
        im = obj
    if im.mode != mode:
        im = im.convert(mode)
    w, h = im.size

    original_aspect = w * 1.0 / h * 1.0
    aspect = width * 1.0 / height * 1.0
    default_aspect = 1.0 * h / w

    resized = False    
    if original_aspect == aspect:
        # same aspect
        if w > width:
            resized = True
    elif original_aspect > aspect:
        # wide
        if w > width:
            resized = True
        new_h = int(w/aspect)
        new_aspect = 1.0 * new_h / w
        if new_aspect < default_aspect:
            new_h += 1 
        if w < width:
            new_w = width
            new_h = height
        else:
            new_w = w
        im = arrange(im, w, h, new_w, new_h)
    else:
        if h > height:
            resized = True
            
        new_w = int(h*aspect)
        
        # adjust
        new_aspect = 1.0 * new_w / h        
        if new_aspect > default_aspect:
            new_w -= 1
            
        if h < height:
            new_w = width
            new_h = height
        else:
            new_h = h
            
        im = arrange(im, w, h, new_w, new_h)

    # resize
    if resized:
        im.thumbnail((width, height), algorithm)

    return im

def check_args():
    usage = 'usage: %prog [options]'
    parser = OptionParser()
    parser.add_option('-w',
                      '--width',
                      type='int',
                      help='output image witdh')
    parser.add_option('-t',
                      '--height',
                      type='int',
                      help='output image height')
    parser.add_option('-s',
                      '--suffix',
                      default='_1',
                      help='output filename suffix')

    (options, args) = parser.parse_args()
    if (options.width is None) or (options.height is None):
        parser.error('require width, height')

    if not args:
        parser.error('require image filename')

    return (options, args)

if __name__ == "__main__":
    (options, args) = check_args()

    for arg in args:
        im = resize(arg, options.width, options.height)
        filename = os.path.basename(arg)
        f, e = os.path.splitext(filename)
        output = '%s%s%s' % (f, options.suffix, e)
        im.save(output)
#### resize.py ends here
