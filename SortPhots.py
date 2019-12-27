#!/usr/bin/env python3

import lib.mod as mod
import sys
import argparse

parser = argparse.ArgumentParser(description="This script renames the photos contained   \
                                              in the provided folder such that they appear\
                                              ordered by the date they are taken")
parser.add_argument("folder_path", help="This provides the path to the photo folder", \
                    type=str)
args = parser.parse_args()

album = mod.Album(folder_path=path)
print(album)
