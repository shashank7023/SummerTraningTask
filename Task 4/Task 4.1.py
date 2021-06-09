# Task 4.1
# Create image by yourself using python code

import numpy as np
import cv2

# Creating a image of size 400 X 400 pixels
photo = np.zeros((400,400,3))

photo[0:100,0:100]=[44,165,255]
photo[0:100,100:200]=[255,0,0]
photo[0:100,200:300]=[0,0,255]
photo[0:100,300:400]=[0,255,0]

photo[100:200,0:100]=[255,0,0]
photo[100:200,100:200]=[0,0,255]
photo[100:200,200:300]=[0,255,0]
photo[100:200,300:400]=[255,0,255]

photo[200:300,0:100]=[0,0,255]
photo[200:300,100:200]=[0,255,0]
photo[200:400,200:300]=[64,0,128]
photo[200:300,300:400]=[0,169,200]

photo[300:400,0:100]=[0,255,0]
photo[300:400,100:200]=[64,0,128]
photo[300:400,200:300]=[0,169,200]
photo[300:400,300:400]=[0,0,0]

# Displaying image
cv2.imshow("Colorful Square", photo)
cv2.waitKey()
cv2.destroyAllWindows()
