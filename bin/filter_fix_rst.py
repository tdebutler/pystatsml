#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on mercredi 17 avril 2019, 11:01:21 (UTC+0200)

@author: edouard.duchesnay@gmail.com

Filter that fix rst files generated by jupyter nbconvert

It is called in the Makefile:
jupyter nbconvert --to rst --stdout $< | bin/filter_fix_rst.py > $@
"""

import sys
import re

if __name__ == "__main__":

    """
    filename = 'test.rst'
    fd = open(filename, mode='r')
    in_str = fd.read()
    fd.close()
    """
    #in_str = sys.stdin.read()
    lines = sys.stdin.readlines()
    ## FILTER 1:
    #    CONVERT
    #    :raw-latex:`\begin{align}
    #    \dot{x} & = \sigma(y-x) \\
    #    ...
    #    \end{align}`
    #
    #    TO
    #    .. raw:: latex
    #
    #    \begin{align}
    #    \dot{x} & = \sigma(y-x) \\
    #    ...
    #    \end{align}
    """
    regex = re.compile(r":raw-latex:`(.+?)`", re.MULTILINE|re.DOTALL)
    out_str = regex.sub(r'.. raw:: latex\n\n\1', in_str)
    """
    match_start = re.compile(r":raw-latex:`(.+?)$")
    match_stop = re.compile(r"`")
    indent = 0
    for i in range(len(lines)):
        #print(lines[i])
        if len(match_start.findall(lines[i])) > 0:
            #print(i, "match_start", lines[i])
            indent = 3
            lines[i] = match_start.sub(r'.. raw:: latex\n\n%s\1' % (r" " * indent), lines[i])
        elif indent and len(match_stop.findall(lines[i])) > 0:
            lines[i] =  r" " * indent + match_stop.sub(r'', lines[i])
            indent = 0
        elif indent:
            #print(i, "indent", lines[i])
            lines[i] = r" " * indent + lines[i]

    """
       :math:`\mathbf{v}_k` associated to the singular value :math:`d_k
    """
    for line in lines:
        sys.stdout.write(line)