

import numpy as np
from PIL import Image
im1=Image.open('lena.jpg')
im1.show()

im=np.array(Image.open('lena.jpg'))
print(im)



