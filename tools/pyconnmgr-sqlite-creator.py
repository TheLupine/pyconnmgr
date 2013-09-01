#!/usr/bin/env python

"""
    title:      Python Connections Manager - sqlite3 DB Creator
    
    date:       05.17.2009
    
    author:     Lupine  - http://www.thelupine.com
    
    description:    Quik script to convert the old hostsfile into hostsfile.db
    
"""

#python imports
import sys
import os
import subprocess
import re
import sqlite3

#Global variables
APPCONFDIR      = "/.pyconnmgr"
OLDHOSTSFILE    = os.environ["HOME"] + APPCONFDIR + "/hostsfile"
HOSTSFILE       = os.environ["HOME"] + APPCONFDIR + "/hostsfile.db"

#functions
def update_sqlhostsfile():
    """
    This function will check for the existence of a HOSTSFILE and if not found, 
    check for existence of older nonML hostfile and convert it
    """
    if (not os.path.isfile(HOSTSFILE)) and (os.path.isfile(OLDHOSTSFILE)):
        open_oldhostsfile = open(OLDHOSTSFILE,"r")
        filelines = open_oldhostsfile.readlines()
        open_oldhostsfile.close()

        #create new file/db for writing
        sqlconn = sqlite3.connect(HOSTSFILE)
        sqlcursor = sqlconn.cursor()
        
        #create table
        sqlcursor.execute('''create table hosts
                            (name text, 
                            sshport int, 
                            sshuser text,
                            sshopt text,
                            vnctrucolor int,
                            vncbgr int,
                            vncquality int,
                            vnccompresslevel int,
                            vncport int,
                            vncpassword text,
                            vncx11cur int,
                            rdpgeom text,
                            rdpuser text,
                            rdpdom text)''')


        #look through each file line, and add default values for the existing host entry
        for fileline in filelines:
            fileline = fileline.strip('\n')
            
            #update the host information
            sqlquery = "insert into hosts values ("
            sqlquery += "'" + fileline + "'"
            sqlquery += ",'22','root','-X','1','0','9','9','5900','','1','1024x768','','')"
            sqlcursor.execute(sqlquery)
        
        #commit the changes, and close the DB
        sqlconn.commit()
        sqlconn.close
        
if __name__ == "__main__":
    update_sqlhostsfile()

