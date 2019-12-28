#!/usr/bin/env python3

import lib.mod as mod
import sys
import argparse
import numpy as np

def dateshift(inputstr):
   model, temp1, temp2 = inputstr.split("-")
   if temp1[0] == 'm':
       temp1 = temp1.strip("m")
       shift = -np.array(temp1.split(":") + temp2.split(":"), dtype=int)
   else:
       shift = np.array(temp1.split(":") + temp2.split(":"), dtype=int)
   return [model,shift]

parser = argparse.ArgumentParser(description="This script renames the photos contained   \
                                              in the provided folder with ascending numbers\
                                              corresponding to the date they are taken")
parser.add_argument("folder_path", help="This provides the path to the photo folder. All \
                                         Photos in this folder will be renamed!", \
                    type=str)
parser.add_argument("--info", help="If this option is specified only some information \
                                    about the folder is collected and printed. No renaming\
                                    takes place", \
                    default=False, action="store_true")
parser.add_argument("--dateshift", help="Provide the camera models names and the date shifts.\
                                         <model1-yyyy:mm:dd-hh:mm:ss> <model2-yyyy:mm:dd-hh:mm:ss> \
                                         ... if the shift is negative provide myyyy, neclect all \
                                         spaces in the modelname", \
                    type=dateshift, nargs='*')
args = parser.parse_args()

album = mod.Album(folder_path=args.folder_path)

if args.info == True:
    print(album)
    quit()

if args.dateshift is not None:
    dateshift = {}
    for element in args.dateshift:
        dateshift[element[0]] = element[1]
    for model in dateshift.keys():
        if model not in [x.replace(" ", "") for x in album.get_camera_models()]:
            raise RuntimeError("Camera model {} not found in album. Please specify only existing models".format(model))
        album.shift_dates(model=model, years=dateshift[model][0], months=dateshift[model][1], \
                          days=dateshift[model][2], hours=dateshift[model][3], minutes=dateshift[model][4], \
                          seconds=dateshift[model][5])
input("Photos will be renamed now. This will override the existing names. Hit Enter to go on.")
album.rename_ordered_by_date()


