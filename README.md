# Photo Sorting Script 
=============================================================
## 28.12.2019
-------------

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

##Requirements:
---------------

  - Python3
  - python modules: exifread, argeparse, numpy, fnmatch 

##Running:
----------

  1. Copy all photos into a you want to rename into a new directory so 
     so the originals do not get changed and accidentally overwritten
  2. Run the script from the folder above and give the album folder as input

        usage: SortPhots.py [-h] [--info] [--dateshift [DATESHIFT [DATESHIFT ...]]]
                            folder_path
        
        This script renames the photos contained in the provided folder with ascending
        numbers corresponding to the date they are taken
        
        positional arguments:
          folder_path           This provides the path to the photo folder. All Photos
                                in this folder will be renamed!
        
        optional arguments:
          -h, --help            show this help message and exit
          --info                If this option is specified only some information
                                about the folder is collected and printed. No renaming
                                takes place
          --dateshift [DATESHIFT [DATESHIFT ...]]
                                Provide the camera models names and the date shifts.
                                <model1-yyyy:mm:dd-hh:mm:ss> <model2-yyyy:mm:dd-
                                hh:mm:ss> ... if the shift is negative provide myyyy,
                                neclect all spaces in the modelname

