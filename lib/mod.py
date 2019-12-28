#File containing the main classes in order to sort the Album

import exifread #module to read properties from a jpeg file
import sys
import os
import fnmatch
import numpy as np

class Photo:
    
    def __init__(self, path):
        self.path = path
        f = open(path, 'rb')
        tags = exifread.process_file(f)
        f.close()
        str_date = str(tags['EXIF DateTimeOriginal'])
        self.str_date = str_date
        vec_date = str_date.split()
        date = vec_date[0].split(':') + vec_date[1].split(':')
        self.date = np.array(date, dtype=int)
        self.model = str(tags['Image Model'])
        self.set_date_order_number()
    
    def __str__(self):
        return 'path: ' + self.path + "\ndate_order_number: " + str(self.date_order_number)
            
    def set_date_order_number(self):
        self.date_order_number = (self.date[0]-2001)*31536000 + (self.date[1]-1)*2592000 + (self.date[2]-1)*86400 + \
                self.date[3]*3600 + self.date[4]*60 + self.date[5]

    def shift_date(self, shift):
	#shift has to be a numpy array like [years, months, days, hours, minutes, seconds]
        self.date += shift
        self.set_date_order_number()
        
    def rename_path(self, newpath):
        os.rename(self.path, newpath)
        self.path = newpath

class Album:
    
    def __init__(self, folder_path):
        folder_path = folder_path.strip("/") + "/"
        self.folder_path = folder_path
        self.photo_list = []
        for tempfile in os.listdir(folder_path):
            if tempfile[-4:].upper() == '.JPG':
                self.photo_list.append(Photo(folder_path + tempfile))

    def __str__(self):
        string = 'Path of this album:\n'
        string += self.folder_path + '\n'
        string += 'Photos in this album: {}\n'.format(len(self.photo_list))
	
        camera_models = self.get_camera_models()	
        string += 'Camera models used in this album: ' 
        for model in camera_models:
            string += "\""+model+"\"" + ' '
        string += "\n"
	
        lower, upper  = self.get_date_boundaries()
        string += 'Earliest date in album: {}\n'.format(lower)
        string += 'Latest date in album: {}\n'.format(upper)

        return string
    
    def get_camera_models(self):
        models = []
        for photo in self.photo_list:
            if photo.model not in models:
                models.append(photo.model)
            else:
                pass
        return models

    def get_date_boundaries(self):
        lower = self.photo_list[0]
        upper = self.photo_list[0]
        for photo in self.photo_list[1::]:
            if photo.date_order_number < lower.date_order_number:
                 lower = photo
            elif photo.date_order_number > upper.date_order_number:
                 upper = photo 
            else:
                 pass
        return lower.str_date, upper.str_date

    def shift_dates(self, model, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        shift = np.array([years, months, days, hours, minutes, seconds], dtype=int)
        for photo in self.photo_list:
            if photo.model.replace(" ", "") == model:
                photo.shift_date(shift=shift)
            else:
                pass
 
    def rename_ordered_by_date(self):
        print('Attempting to reorder all photos according to their date of origin.')
        newfolder = self.folder_path.strip("/") + "_ordered/"
        if not os.path.exists(newfolder):
            print("creating new directory")
            os.mkdir(newfolder)
        ordered_list = [self.photo_list[0]]
        for photo in self.photo_list[1:]:
            for i in range(0,len(ordered_list)):
                if photo.date_order_number < ordered_list[i].date_order_number:
                    ordered_list.insert(i,photo)
                    break
                elif i == (len(ordered_list)-1):
                    ordered_list.append(photo)
                else:
                    pass
        self.photo_list[:] = ordered_list[:]
        for i in range(0,len(self.photo_list)):
            new_path = newfolder + str(i+1) + '.jpg'
            os.rename(self.photo_list[i].path, new_path)
            self.photo_list[i].path = new_path
        os.rename(newfolder, self.folder_path)
        print('-> Renamed all photos according to their date of origin.')
