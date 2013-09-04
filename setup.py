#!/usr/bin/env python

from distutils.core import setup
import os, sys
import glob


glade_files = glob.glob("glade/*")    
setup(name = "pyconnmgr",
    version = "4.0.2",
    description = "Simple Python/Glade frontend to SSH, VNC and rdesktop commands.",
    author = "Lupine",
    author_email = "thelupine@gmail.com",
    url = "http://www.thelupine.com/pyconnmgr",
    license = "GPLv2",
    data_files=[('/usr/share/pyconnmgr/', glade_files), 
        ('/usr/share/applications', ['pyconnmgr.desktop']),
        ('/usr/share/man/man1', ['pyconnmgr.1.gz'])],
    scripts=["src/pyconnmgr"],
    long_description = """pyconnmgr is a simple Python/Glade frontend to SSH, VNC and rdesktop commands. \
It was created as a learning process for developing in Python and Glade. Even though this was \
created as a learning process, the application itself turned out to be very useful.""")
