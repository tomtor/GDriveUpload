#!/usr/bin/python

import sys
import os

from os.path import expanduser
home = expanduser("~")
cwd= os.getcwd()

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.settings import LoadSettingsFile

home_upload= home + os.sep + ".upload.py" + os.sep

if os.path.exists(home_upload):
    os.chdir(home_upload)

gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)
os.chdir(cwd)

file_list = drive.ListFile({'q': "'root' in parents and title='Dumps'"}).GetList()

parent = drive.CreateFile({'id': file_list[0]['id']})
file1 = drive.CreateFile()
file1['title']= sys.argv[1].replace(os.sep, '|')
file1['parents']= [parent]
file1.SetContentFile(sys.argv[1])
print "Start upload of " + file1['title']
file1.Upload()
print "Done"
