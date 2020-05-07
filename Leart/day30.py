

import os
import glob
import threading


from PIL import Image
PREFIX = 'Thumbnail'

def generate_thumbnails(infile, size, format = 'PNG'):
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('\\') + 1 :]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'
    image = Image.open(infile)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(outfile, format)

def main():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    
    for infile in glob.glob('Image/*.png'):
        for size in (32, 64, 128):
            threading.Thread(
                target=generate_thumbnails,
                args = (infile, (size,size)) 
            ).start()


if __name__ == '__main__':
    main()