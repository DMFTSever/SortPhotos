#!/usr/bin/env python3

import lib.mod as mod
import sys
import argparse
import numpy as np

def dateshift(inputstr):
   model, temp = inputstr.split("::")
   if temp[0] == 'm':
       temp = temp.strip("m")
       shift = -np.array(temp.split(":"), dtype=int)
   else:
       shift = np.array(temp.split(":"), dtype=int)
   return [model,shift]

parser = argparse.ArgumentParser(description="Dieses Programm benennt die Fotos des Zielordners \
                                              mit nach dem Aufnahmedatum geordneten Nummern um.")
parser.add_argument("zielordner", help="Pfad zum Zielordner, welcher die umzubennenden Fots enthält.", \
                    type=str)
parser.add_argument("--info", help="Gibt informationen über den Zielordner aus ohne die Fotos umzubennen.", \
                    default=False, action="store_true")
parser.add_argument("--zeitverschiebung", help="Angeben um das Aufnahmedatum aller Fotos eines oder mehrerer\
                                                Kameramodels zu Ordnungszwecken entsprechend zu verschieben.\
                                                <model1::yyyy:mm:dd:hh:mm:ss> <model2::yyyy:mm:dd:hh:mm:ss> \
                                                ... Soll die Verschiebung negativ sein muss dem Jahr ein m \
                                                vorangestellt sein: myyyy, z.B. m1997. Im Modelnamen müssen\
                                                alle Leerzeichen vernachlässigt werden. Die Modelnamen können \
                                                mit --info angezeigt werden", \
                    type=dateshift, nargs='*')
args = parser.parse_args()

album = mod.Album(folder_path=args.zielordner)

if args.info == True:
    print(album)
    quit()

if args.zeitverschiebung is not None:
    dateshift = {}
    for element in args.zeitverschiebung:
        dateshift[element[0]] = element[1]
    for model in dateshift.keys():
        if model not in [x.replace(" ", "") for x in album.get_camera_models()]:
            raise RuntimeError("Kameramodel {} nicht im Album gefunden. Bitte geben Sie einen gültiges Model an.".format(model))
        album.shift_dates(model=model, years=dateshift[model][0], months=dateshift[model][1], \
                          days=dateshift[model][2], hours=dateshift[model][3], minutes=dateshift[model][4], \
                          seconds=dateshift[model][5])

userin = input("Alle Fotos des Ordners \"{}\" werden jetzt umbennant. ".format(album.folder_path) + \
               "Die bisherigen Namen werden dabei überschrieben. Tippe J/j/Ja/ja um fortzufahren.\n")
if userin in ['J','j','Ja','ja']:
    album.rename_ordered_by_date()
else:
    print("Abbrechen....")

print("Fotos erfolgreich umbenannt.")

