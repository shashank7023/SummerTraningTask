# Task 4.2
# Take 2 image crop some part and swap it

import cv2

# Reading image of Dog
dog = cv2.imread("dog.png")

# Reading image of Tiger
tiger = cv2.imread("tiger.png")

# Display image of tiger and dog
cv2.imshow("tiger", tiger)
cv2.imshow("dog", dog)
cv2.waitKey()
cv2.destroyAllWindows()

# Croped image of Tiger's face
crop_tiger = tiger[26:380,200:510]
# Swaping the face of dog with tiger
dog[26:380,200:510] = crop_tiger

# Display the swapped image of Dog 
cv2.imshow("swaped dog", dog)
cv2.waitKey()
cv2.destroyAllWindows()

# Reading image of Dog again
dog = cv2.imread("dog.png")
# Croped image of Dog's face
crop_dog = dog[15:400,190:514]
# Swaping the face of tiger with dog
tiger[15:400,190:514] = crop_dog

# Display the swapped image of Tiger
cv2.imshow("swaped tiger", tiger)
cv2.waitKey()
cv2.destroyAllWindows()
