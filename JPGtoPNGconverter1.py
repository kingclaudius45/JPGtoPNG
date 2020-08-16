from PIL import Image
import sys
import os


#grap first and second argument
image_folder= sys.argv[1]
output_folder=sys.argv[2]

#cheack id new\ exists , if not then create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)
    img.save(f'{output_folder}{filename}.png','png')
    print('all done!')