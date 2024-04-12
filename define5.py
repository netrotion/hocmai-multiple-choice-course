from PIL import Image
import os
def get_size(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    print(width,height,width/height)
    return [width,height]
files = os.listdir('assets')
image_path = 'assets/sedxtptirw.png'
#print(files)
for i in files:
    get_size('assets/'+i)