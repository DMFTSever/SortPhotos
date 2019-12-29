Photo Sorting Script 
====================
28.12.2019
----------

SortPhotos takes a folder and renames the photos with ascending numbers
corresponding to the date they were taken. It does allow to shift the
dates in case one of the cameras has the wrong date/time. However, 
internally the date is not changed, it is only shifted for the purpose
to correctly rename them with ascending numbers.
The use is on the full responsability of the user. I do not take any
responsability for the consequences following from using or downloading
this script.

Maintainer:
Severino Adler

Requirements:
-------------

  - Python3
  - python modules: exifread, argeparse, numpy, fnmatch 

Running:
--------

  1. Copy all photos into a you want to rename into a new directory so 
     so the originals do not get changed and accidentally overwritten
  2. Run the script from the folder above and give the album folder as input:

       $ python3 <path to SortPhotos.py> folder_path

       or

       $ python3 <path to SortPhotos.py> --help for help

