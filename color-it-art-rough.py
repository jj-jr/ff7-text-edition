from PIL import Image
from colorit import init_colorit, background

init_colorit()
image = Image.open('/Users/jerryj/Desktop/mario.jpg')

depth_x = int(input("Write height: "))
depth_y = int(input("Write width: "))
image = image.resize((depth_x, depth_y))

for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(background(' ', image.getpixel((x, y))), end='')
    print()