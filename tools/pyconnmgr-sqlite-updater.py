#!/usr/bin/env python

"""
    title:      Python Connections Manager - sqlite3 DB Updater
    
    date:       10.14.2009
    
    author:     Lupine  - http://www.thelupine.com
    
    description:    Quik script to update hostsfile.db with new table structure
    
"""

#python imports
import sys
import os
import subprocess
import re
import sqlite3

#Global variables
APPCONFDIR      = "/.pyconnmgr"
HOSTSFILE       = os.environ["HOME"] + APPCONFDIR + "/hostsfile.db"

#functions
def update_sqlhostsfile():
    """
    This function will check for the existence of a HOSTSFILE and if found, 
    update it's table structure
    """
    if (os.path.isfile(HOSTSFILE)):
        sqlconn = sqlite3.connect(HOSTSFILE)
        sqlcursor = sqlconn.cursor()
        
        #update table
        sqlcursor.execute('''alter table hosts
                            add tab int''')
        
        #commit the changes, and close the DB
        sqlconn.commit()
        sqlconn.close
        
if __name__ == "__main__":
    update_sqlhostsfile()

