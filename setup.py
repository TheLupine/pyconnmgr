#!/usr/bin/env python

from distutils.core import setup
import os, sys
import glob


glade_files = glob.glob("glade/*")    
setup(name = "pyconnmgr",
    version = "2.0.0",
    description = "Simple Python/Glade frontend to SSH, VNC and rdesktop commands.",
    author = "Lupine",
    author_email = "thelupine@gmail.com",
    url = "https://launchpad.net/pyconnmgr",
    license = "GPL v2",
    data_files=[('/usr/share/pyconnmgr/', glade_files), 
        ('/usr/share/applications', ['pyconnmgr.desktop'])],
    scripts=["src/pyconnmgr"],
    long_description = """pyconnmgr is a simple Python/Glade frontend to SSH, VNC and rdesktop commands. \
It was created as a learning process for developing in Python and Glade. Even though this was \
created as a learning process, the application itself turned out to be very useful.""")
