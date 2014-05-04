GDriveUpload
============

Simple python script to upload a single file to Google Drive

```
usage:

1) Create a directory 'Dumps' in your GDrive root.

   Uploaded files will be placed in this directory.

2) Enter

   ./upload.py /upload/this/file.bin

   This will ask for your credentials and upload the file to 'Dumps'.
   Directory separators are replaced by '|'

3) If you want to save your credentials in your working directory then
   rename '_settings.yaml' to 'settings.yaml'. On your next upload
   your credentials will be saved in two files:
   'client_secrets.json' and 'credentials.json'


4) Optional:

   Create a directory '.upload.py' in your home directory.

   This directory is used to save your credential information.
   Copy '_settings.yaml' to 'settings.yaml' in this directory.
   Also copy the 'client_secrets.json' and 'credentials.json' from
   your working directory. Now you can run 'upload.py' from any directory.
```
