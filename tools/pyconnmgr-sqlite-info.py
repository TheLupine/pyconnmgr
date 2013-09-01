#!/usr/bin/env python

"""
    title:      Python Connections Manager - sqlite3 DB Info
    
    date:       10.14.2009
    
    author:     Lupine  - http://www.thelupine.com
    
    description:    Quik script to display info about hostsfile.db
    
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
    display information about the database/tables
    """
    if (os.path.isfile(HOSTSFILE)):
        sqlconn = sqlite3.connect(HOSTSFILE)
        sqlcursor = sqlconn.cursor()
        
        #update table
        sqlcursor.execute('''PRAGMA table_info(hosts)''')
        col_name_list = sqlcursor.fetchall()
        for col_name in col_name_list:
            tab_col_found = 0
            if re.search('tab', col_name[1]):
                tab_col_found = 1
        if not tab_col_found:
            sqlcursor.execute('''alter table hosts add tab int''')
            sqlconn.commit()
        
        #commit the changes, and close the DB
        sqlconn.commit()
        sqlconn.close
        
if __name__ == "__main__":
    update_sqlhostsfile()

