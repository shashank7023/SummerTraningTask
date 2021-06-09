# Task 4.3
# Take 2 image and combine it to form a single image.

import cv2

# Reading image of dog
dog = cv2.imread("dog.png")

# Reading image of Tiger
tiger = cv2.imread("tiger.png")

# Displaying image of Tiger
cv2.imshow("tiger", tiger)
cv2.waitKey()
cv2.destroyAllWindows()

# Displaying image of Dog
cv2.imshow("dog", dog)
cv2.waitKey()
cv2.destroyAllWindows()

# Cropping image of Tiger
crop_tiger = tiger[0:677, 0: 515]

# Displaying the cropped image of Tiger
cv2.imshow("cropped tiger image", crop_tiger)
cv2.waitKey()
cv2.destroyAllWindows()

# Cropping image of Dog
crop_dog = dog[0:677, 0:515]

# Displaying the cropped image of Dog
cv2.imshow("cropped dog image", crop_dog)
cv2.waitKey()
cv2.destroyAllWindows()

# Combining iamge of Tiger and Dog
collage = cv2.hconcat([crop_tiger, crop_dog])

# Displaying the combined image
cv2.imshow("combined image", collage)
cv2.waitKey()
cv2.destroyAllWindows()
