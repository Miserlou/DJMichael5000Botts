# DJ Michael 5000 Botts 
#  - Chopping and Screwing in Python
#  - using the EchoNest API
# Rich Jones, Music Hack Day 2010
# Copyright waived

from optparse import OptionParser
import numpy
import os
import random
import sys
import time

import soundtouch
from echonest import audio, modify

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default=False, help="Input filename", metavar="FILE")
    parser.add_option("-c", "--chop", dest="chop", default=False, help="Chop that shit up")
    parser.add_option("-s", "--screw",dest="screw", default=True, help="Screw that jam")
    (options, args) = parser.parse_args()
    options = options.__dict__
    print options['filename']
    if(options['filename'] is False and (len(args) is 0)):
        print "Enter a filename!"
        sys.exit(-1)

    in_filename = options['filename']
    out_filename = "djm-" + in_filename

    if(options['chop'] is not False):
        chop = True
        chop_times = int(options['chop'])

    screw = options['screw']
    chop = options['screw']

    st = modify.Modify()
    afile = audio.LocalAudioFile(in_filename)
    beats = afile.analysis.beats
    out_shape = (len(afile.data),)
    out_data = audio.AudioData(shape=out_shape, numChannels=1, sampleRate=44100)
    old_ad = None
    for i, beat in enumerate(beats):
        if chop:
            if(i%chop_times == 0 and old_ad is not None):
                out_data.append(new_ad)
                #new_ad = old_ad
                new_ad = afile[beat]
            else:
                new_ad = afile[beat]
        else:
            new_ad = afile[beat]
        if screw:
            new_ad = st.shiftPitchSemiTones(new_ad, -4)
        out_data.append(new_ad)
        old_ad = afile[beat]
    out_data.encode(out_filename)


if __name__ == '__main__':
    main()

