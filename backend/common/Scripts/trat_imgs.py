import os
from PIL import Image
import re
import sys
import datetime
import shutil





class Optimize_Images:

    dimensions_size = {'thumbnail': 120,
                    'small': 200,
                    'medium': 400,
                    'large_optimazed': 800

                    }


    DIRPATH = ''

    def __init__(self, photo_url, id):
        self.folder = str(id) + ' thumbs' + 'HAMMING'
        self.filename = (str(photo_url))
        self.photo_url = photo_url
        self.img_raw = Image.open(photo_url)
        self.width, self.height = self.img_raw.size
        print('deu')



    def __calc_new_height(self, width, height, new_width):
        return round(new_width * height / width)


    def save(self, mode='HAMMING'):
        try:
            os.makedirs(self.folder)

        except:
            shutil.rmtree(self.folder)

        for new_width in self.dimensions_size:
            new_height = Optimize_Images.__calc_new_height(self, self.width, self.height, self.dimensions_size[new_width])
            print(new_height)
            print(self.dimensions_size[new_width])
            new_img = self.img_raw.resize((self.dimensions_size[new_width], new_height), Image.Resampling.HAMMING)
            new_img_path = os.path.join(self.folder, (str(new_width) + str('.png')))
            print(new_img_path)


            try:
                new_img.save(new_img_path, optimize=True, quality=30)

            except:
                raise RuntimeError('Could not convert')

            print(f'Saved ')




    def __calc_new_height(self, width, height, new_width):
        return round(new_width * height / width)

    def __is_image(self, extension):
        extension_lowercase = extension.lower()
        return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))



