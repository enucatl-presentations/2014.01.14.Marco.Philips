#!/usr/bin/env python
# encoding: utf-8

import os
import h5py
import numpy as np
import matplotlib as mpl

from readimages.dpc.commandline_parser import commandline_parser
from readimages.utils.hadd import hadd

args = commandline_parser.parse_args()

from pgf_style import pgf_with_rc_fonts

mpl.rcParams.update(pgf_with_rc_fonts)

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

input_file_name = hadd(args.file)
if not os.path.exists(input_file_name):
    raise(OSError("{0} not found".format(input_file_name)))

input_file = h5py.File(input_file_name, "r")
object_name = "postprocessing/visibility_{0}".format(
        args.pixel)
input_object = input_file[object_name]
pixels = input_object[0]
visibility = input_object[1]
plt.figure(figsize=(4.6, 3))
axis = plt.axes()
plt.plot(pixels, visibility.T, linewidth=1, color='black')
plt.xlabel("pixel")
plt.ylabel("visibility")
mean_visibility = np.mean(visibility)
min_visibility = np.min(visibility)
max_visibility = np.max(visibility)
line = plt.axhline(y=mean_visibility, linewidth=1,
        color='blue', linestyle='--')
legend = plt.legend([line], ["average visibility: {0:.1f} $\\%$".format(
            mean_visibility * 100)])
legend.get_frame().set_linewidth(0)
axis.set_ylim(
        bottom=0,
        top=1.2*max_visibility)
axis.xaxis.tick_bottom()
axis.yaxis.tick_left()
axis.yaxis.set_major_formatter(FuncFormatter(
    lambda x, pos=0: "{0:.0%}".format(x)))
plt.tight_layout()
plt.savefig('visibility_{0}.png'.format(
    os.path.splitext(os.path.basename(input_file_name))[0]),
        bbox_inches='tight', dpi=400)
