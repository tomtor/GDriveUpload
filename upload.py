#!/usr/bin/python

import sys
import os

from optparse import OptionParser
from os.path import expanduser

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.settings import LoadSettingsFile

usage= "usage: %prog [options] FILE"
parser = OptionParser(usage= usage)
parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                  help="verbose status messages", default=False)
parser.add_option("-d", "--destination", dest="destination", metavar="DEST",
                  help="destination directory (defaults to 'Dumps')",
                  default="Dumps")

(options, args) = parser.parse_args()

home = expanduser("~")
cwd= os.getcwd()

home_upload= home + os.sep + ".upload.py" + os.sep

if os.path.exists(home_upload):
    os.chdir(home_upload)

gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)
os.chdir(cwd)

file_list = drive.ListFile({'q': "title='" + options.destination + "'"}).GetList()

parent = drive.CreateFile({'id': file_list[0]['id']})
file1 = drive.CreateFile()
file1['title']= args[0].replace(os.sep, '|')
file1['parents']= [parent]
file1.SetContentFile(args[0])

if options.verbose:
  print "Start upload of " + file1['title'] + " to dir '" + options.destination + "'"
file1.Upload()
if options.verbose:
  print "Done"
