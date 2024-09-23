import numpy as np
import cv2
from PIL import Image, ImageDraw
def pos(img):
    for x in range(512):
        for y in range(512):
            if not np.array_equal(img[x, y], [255,255,255]):
                return img[x,y], (x,y)
    return [], ()
d1 = []
c1 = []
for x in range(1, 101):
    add = './assets/Layer _.png'
    new_add = add.replace("_", str(x))
    img = cv2.imread(new_add)
    if img is not None:
        d,c = pos(img)
        d1.append(tuple(d))
        c1.append(c)
new_image = Image.new('RGB', (512, 512),color='white')
draw = ImageDraw.Draw(new_image)
for i in range(len(c1)-1):
    if c1[i] != () and c1[i+1] != ():
        draw.line([c1[i], c1[i+1]], fill=d1[i])
new_image.save("output.png")